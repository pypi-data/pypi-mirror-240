from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Self
import pkg_resources

import sass
import re
import copy

from great_tables._gt_data import GTData

# Main gt imports ----
from great_tables import _utils

# Rewrite main gt imports to use relative imports of APIs ----
from great_tables._tbl_data import TblDataAPI
from great_tables._body import body_reassemble
from great_tables._boxhead import BoxheadAPI
from great_tables._footnotes import FootnotesAPI
from great_tables._formats import (
    FormatsAPI,
    fmt_number,
    fmt_percent,
    fmt_integer,
    fmt_scientific,
    fmt_currency,
    fmt_engineering,
)
from great_tables._heading import HeadingAPI
from great_tables._locale import LocaleAPI
from great_tables._options import OptionsAPI
from great_tables._row_groups import RowGroupsAPI
from great_tables._source_notes import tab_source_note
from great_tables._spanners import tab_spanner, cols_move
from great_tables._stub import reorder_stub_df
from great_tables._stubhead import StubheadAPI


# from ._helpers import random_id
# from ._body import Body
from ._text import StringBuilder, _process_text
from ._utils import _as_css_font_family_attr, _unique_set
from ._tbl_data import n_rows, _get_cell


# from ._body import Context


__all__ = ["GT"]

# Architecture of GT:
# 1. GT class for holding all user specified directives (internally
#    implemented using multiple smaller modules)
# 2. Build step that performs mostly-context-agnostic pre-rendering tasks.
#    State from GT class is transformed into input for the render step.
# 3. Render into final output.


# =============================================================================
# GT class
# =============================================================================
class GT(
    GTData,
    TblDataAPI,
    BoxheadAPI,
    RowGroupsAPI,
    HeadingAPI,
    StubheadAPI,
    FootnotesAPI,
    LocaleAPI,
    FormatsAPI,
    OptionsAPI,
):
    """
    Create a gt Table object.

    Methods
    -------
        render: Renders and returns the HTML table.

    Examples
    --------
        >>> from gt import *
        >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20}])
        >>> x
        >>> print(x)
    """

    def _repr_html_(self):
        return self.render(context="html")

    def __init__(
        self,
        data: Any,
        locale: str = "",
        rowname_col: str | None = None,
        groupname_col: str | None = None,
    ):
        # This is a bad idea ----
        gtdata = GTData.from_data(
            data, locale=locale, rowname_col=rowname_col, groupname_col=groupname_col
        )
        super().__init__(**gtdata.__dict__)

    # TODO: Refactor API methods -----
    fmt_number = fmt_number
    fmt_percent = fmt_percent
    fmt_integer = fmt_integer
    fmt_scientific = fmt_scientific
    fmt_currency = fmt_currency
    fmt_engineering = fmt_engineering

    tab_spanner = tab_spanner
    tab_source_note = tab_source_note
    cols_move = cols_move

    # -----

    def _get_has_built(self: GT) -> bool:
        return self._has_built

    def _render_formats(self, context: str) -> GT:
        self._body.render_formats(self._tbl_data, self._formats, context)
        return self

    def _build_data(self, context: str):
        # Build the body of the table by generating a dictionary
        # of lists with cells initially set to nan values
        built = copy.copy(self)
        built._body = self._body.__class__(self._tbl_data.copy())
        built._render_formats(context)
        # built._body = _migrate_unformatted_to_output(body)

        # built._perform_col_merge()
        built._body = body_reassemble(built._body, self._row_groups, self._stub, self._boxhead)

        # Reordering of the metadata elements of the table

        built._stub = reorder_stub_df(self._stub, self._row_groups)
        # self = self.reorder_footnotes()
        # self = self.reorder_styles()

        # Transformations of individual cells at supported locations

        # self = self.perform_text_transforms()

        # ...

        return built

    def render(self, context: str) -> str:
        self = self._build_data(context=context)

        self._has_built = True

        html_table = self._render_as_html()
        return html_table

    # =============================================================================
    # Building
    # =============================================================================

    # def _body_build(self, data: Table):
    #     return self
    #     # data.cells[(1, 3)].set_cell_value("foo")

    # def _migrate_unformatted_to_output(self, body: Dict[Column, Any]):

    #     # Get the dictionary keys from the body as these serve as column names
    #     colnames = body.keys()

    #     for column in colnames:
    #         body[column]

    #     return body

    # =============================================================================
    # HTML Rendering
    # =============================================================================
    def _render_as_html(self) -> str:
        heading_component = _create_heading_component(self)
        column_labels_component = _create_column_labels_component(self)
        body_component = _create_body_component(self)
        source_notes_component = _create_source_notes_component(self)
        footnotes_component = _create_footnotes_component(self)

        html_table = f"""<table class=\"gt_table\">
{heading_component.make_string()}
{column_labels_component}
{body_component}
{source_notes_component}
{footnotes_component}
</table>
"""

        # Get a string of compiled CSS
        css = _compile_scss(data=self)

        # Obtain the `table_id` value (might be set, might be None)
        table_id = self._options._options["table_id"].value

        # Obtain options set for overflow and container dimensions
        overflow_x = self._options._options["container_overflow_x"].value
        overflow_y = self._options._options["container_overflow_y"].value
        width = self._options._options["container_width"].value
        height = self._options._options["container_height"].value

        if table_id is None:
            id_attr_str = ""
        else:
            id_attr_str = f'id="{table_id}"'

        finalized_table = f"""<div {id_attr_str} style="overflow-x:{overflow_x};overflow-y:{overflow_y};width:{width};height:{height};">
<style>
{css}
</style>
{html_table}
</div>
        """

        return finalized_table


# =============================================================================
# End of GT class
# =============================================================================


# =============================================================================
# GT Getter/Setter Functions
# =============================================================================


def _set_has_built(gt: GT, value: bool) -> GT:
    gt._has_built = value
    return gt


def _get_column_labels(gt: GT, context: str) -> List[str]:
    gt_built = gt._build_data(context=context)
    column_labels = [x.column_label for x in gt_built._boxhead]
    return column_labels


def _get_column_of_values(gt: GT, column_name: str, context: str) -> List[str]:
    gt_built = gt._build_data(context=context)
    tbl_data = gt_built._body.body
    cell_values: List[str] = []

    for i in range(n_rows(tbl_data)):
        cell_content: Any = _get_cell(tbl_data, i, column_name)
        cell_str: str = str(cell_content)
        cell_values.append(cell_str)

    return cell_values


# =============================================================================
# Table Structuring Functions
# =============================================================================


def _create_heading_component(data: GT) -> StringBuilder:
    result = StringBuilder()

    title = data._heading.title
    subtitle = data._heading.subtitle

    has_title = _utils.heading_has_title(title=title)
    has_subtitle = _utils.heading_has_subtitle(subtitle=subtitle)

    # If there is no title or heading component, then return an empty string
    if not has_title and not has_subtitle:
        return result

    title = _process_text(title)
    subtitle = _process_text(subtitle)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns()

    result.append(
        f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_title gt_font_normal">{title}
  </tr>"""
    )

    if has_subtitle:
        subtitle_row = f"""  <tr>
    <th colspan="{n_cols_total}" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">{subtitle}
  </tr>"""
        result.append(f"\n{subtitle_row}")

    return StringBuilder('<thead class="gt_header">', result, "</thead>")


def _create_column_labels_component(data: GT) -> str:
    column_names = data._boxhead._get_column_labels()

    th_cells = "".join([f"  <th>{x}</th>\n" for x in column_names])

    column_names_str = f"<tr>\n{th_cells}</tr>"

    return column_names_str


def _create_body_component(data: GT):
    import pandas as pd

    # for now, just coerce everything in the original data to a string
    # so we can fill in the body data with it
    _str_orig_data = data._tbl_data.applymap(lambda x: str(x) if not pd.isna(x) else x)

    tbl_data = data._body.body.fillna(_str_orig_data)

    column_names = data._boxhead._get_visible_columns()

    body_rows: List[str] = []

    for i in range(n_rows(tbl_data)):
        body_cells: List[str] = []

        for name in column_names:
            cell_content: Any = _get_cell(tbl_data, i, name)
            cell_str: str = str(cell_content)

            body_cells.append('  <td class="gt_row">' + cell_str + "</td>")

        body_rows.append("<tr>\n" + "\n".join(body_cells) + "\n</tr>")

    all_body_rows = "\n".join(body_rows)

    return f'<tbody class="gt_table_body">\n{all_body_rows}\n</tbody>'


def _get_stub_layout(data: GT) -> List[str]:
    # Determine which stub components are potentially present as columns
    stub_rownames_is_column = _stub_rownames_has_column(data=data)
    stub_groupnames_is_column = _stub_group_names_has_column(data=data)

    # Get the potential total number of columns in the table stub
    n_stub_cols = stub_rownames_is_column + stub_groupnames_is_column

    # Resolve the layout of the stub (i.e., the roles of columns if present)
    if n_stub_cols == 0:
        # If summary rows are present, we will use the `rowname` column
        # for the summary row labels
        if _summary_exists(data=data):
            stub_layout = ["rowname"]
        else:
            stub_layout = []

    else:
        stub_layout = [
            label
            for label, condition in [
                ("group_label", stub_groupnames_is_column),
                ("rowname", stub_rownames_is_column),
            ]
            if condition
        ]

    return stub_layout


# Determine whether the table should have row labels set within a column in the stub
def _stub_rownames_has_column(data: GT) -> bool:
    return "row_id" in _get_stub_components(data=data)


# Determine whether the table has any row labels or row groups defined and provide
# a simple list that contains at a maximum two components
def _get_stub_components(data: GT):
    # TODO: we should be using `row_id` instead of `rowname`
    # Obtain the object that describes the table stub
    tbl_stub = data._stub

    # Get separate lists of `group_id` and `row_id` values from the `_stub` object
    group_id_vals = [tbl_stub[i].group_id for i in range(len(tbl_stub))]
    rowname_vals = [tbl_stub[i].rowname for i in range(len(tbl_stub))]

    stub_components: list[str] = []

    if any(x is not None for x in group_id_vals):
        stub_components.append("group_id")

    if any(x is not None for x in rowname_vals):
        stub_components.append("row_id")

    return stub_components


# Determine whether the table should have row group labels set within a column in the stub
def _stub_group_names_has_column(data: GT) -> bool:
    # If there aren't any row groups then the result is always False
    if len(_row_groups_get(data=data)) < 1:
        return False

    # Given that there are row groups, we need to look at the option `row_group_as_column` to
    # determine whether they populate a column located in the stub; if set as True then that's
    # the return value
    row_group_as_column = data._options._get_option_value(option="row_group_as_column")

    row_group_as_column: Any
    if not isinstance(row_group_as_column, bool):
        raise TypeError("Variable type mismatch. Expected bool, got something entirely different.")

    return row_group_as_column


def _row_groups_get(data: GT) -> List[str]:
    return data._row_groups._d


def _create_source_notes_component(data: GT) -> str:
    source_notes = data._source_notes

    # If there are no source notes, then return an empty string
    if source_notes == []:
        return ""

    # Obtain the `multiline` and `separator` options from `_options`
    multiline = data._options.source_notes_multiline.value
    separator = cast(str, data._options.source_notes_sep.value)

    # Get the effective number of columns, which is number of columns
    # that will finally be rendered accounting for the stub layout
    n_cols_total = data._boxhead._get_effective_number_of_columns()

    # Handle the multiline source notes case (each note takes up one line)
    if multiline:
        # Create the source notes component as a series of `<tr><td>` (one per
        # source note) inside of a `<tfoot>`

        source_notes_tr: List[str] = []

        for note in source_notes:
            source_notes_tr.append(
                f"""
  <tr>
    <td class="gt_sourcenote" colspan="{n_cols_total}">{note}</td>
  </tr>
"""
            )

        source_notes_joined = "\n".join(source_notes_tr)

        source_notes_component = f"""  <tfoot class="gt_sourcenotes">
  {source_notes_joined}
</tfoot>"""

        return source_notes_component

    # TODO: Perform HTML escaping on the separator text and
    # transform space characters to non-breaking spaces

    # Create the source notes component as a single `<tr><td>` inside
    # of a `<tfoot>`

    source_notes_str_joined = separator.join(source_notes)

    source_notes_component = f"""<tfoot>
  <tr class="gt_sourcenotes">
    <td class="gt_sourcenote" colspan="{n_cols_total}">
      <div style="padding-bottom:2px;">{source_notes_str_joined}</div>
    </td>
  </tr>
</tfoot>
    """

    return source_notes_component


def _create_footnotes_component(data: GT):
    return ""


# TODO: Port the SCSS compilation routine from the R implementation here
def _compile_scss(data: GT) -> str:
    # Obtain the SCSS options dictionary
    gt_options_dict = data._options._options

    # Get collection of parameters that pertain to SCSS
    scss_params = [
        f"${x.parameter}: {x.value};"
        for x in gt_options_dict.values()
        if x.scss is True and x.value is not None
    ]
    scss_params_str = "\n".join(scss_params) + "\n"

    # Obtain the `table_id` value (might be set, might be None)
    table_id = gt_options_dict["table_id"].value

    # TODO: need to implement a function to normalize color (`html_color()`)

    # Get the unique list of fonts from `gt_options_dict`
    font_list = _unique_set(gt_options_dict["table_font_names"].value)

    # Generate a `font-family` string
    if font_list is not None:
        font_family_attr = _as_css_font_family_attr(fonts=font_list)
    else:
        font_family_attr = ""

    gt_styles_default_file = open(
        pkg_resources.resource_filename("great_tables", "css/gt_styles_default.scss")
    )

    gt_styles_default = gt_styles_default_file.read()
    gt_styles_default = re.sub(r"\s+", " ", gt_styles_default, 0, re.MULTILINE)
    gt_styles_default = re.sub(r"}", "}\n", gt_styles_default, 0, re.MULTILINE)

    gt_colors_file = open(pkg_resources.resource_filename("great_tables", "css/gt_colors.scss"))

    gt_colors = gt_colors_file.read()

    scss = scss_params_str + gt_colors + gt_styles_default

    compiled_css = cast(str, sass.compile(string=scss))
    if table_id is not None:
        compiled_css = re.sub(r"\.gt_", f"#{table_id} .gt_", compiled_css, 0, re.MULTILINE)

    finalized_css = f"""html {{
      {font_family_attr}
}}

{compiled_css}"""

    return finalized_css
