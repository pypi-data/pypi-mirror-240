from great_tables._spanners import spanners_print_matrix
from ._gt_data import GTData
from great_tables.gt_data._options import _get_option_value
from great_tables.gt_data._boxhead.BoxheadAPI import _get_boxhead_get_alignment_by_var
from typing import List, Any
from htmltools import Tag, TagAttrs, TagAttrValue, TagChild, css, tags, HTML
from itertools import groupby
import pandas as pd


def create_columns_component_h(data: GTData) -> str:
    """
    Returns the HTML text fragment for the column/spanner labels.
    """

    # Should the column labels be hidden?
    column_labels_hidden: bool = _get_option_value(data=data, option="column_labels_hidden")

    if column_labels_hidden:
        return ""

    # Get necessary data objects for composing the column labels and spanners
    stubh = data._stubhead
    # TODO: skipping styles for now
    # styles_tbl = dt_styles_get(data = data)
    boxhead = data._boxhead

    # TODO: The body component of the table is only needed for determining RTL alignment
    # is needed in the corresponding column labels
    body = data._body

    # Get vector representation of stub layout
    stub_layout = _get_stub_layout(data=data)

    # Determine the finalized number of spanner rows
    spanner_row_count = _get_spanners_matrix_height(data=data, omit_columns_row=True)

    # Get the column alignments and also the alignment class names
    col_alignment = boxhead._get_visible_alignments()

    # TODO: Modify alignments for RTL support
    # Detect any RTL script characters within the visible columns;
    # this creates a vector the same length as `col_alignment`
    rtl_detect = [
        any(char in rtl_modern_unicode_charset() for char in str(body[x])) for x in range(len(body))
    ]

    # For any columns containing characters from RTL scripts; we
    # will transform a 'left' alignment to a 'right' alignment
    for i in range(len(rtl_detect)):
        if (rtl_detect[i] and col_alignment[i] != "center"):
            col_alignment[i] = "right"

    # Get the column headings
    headings_vars = boxhead._get_visible_columns()
    headings_labels = boxhead._get_visible_column_labels()

    # TODO: Skipping styles for now
    # Get the style attrs for the stubhead label
    # stubhead_style_attrs = subset(styles_tbl, locname == "stubhead")
    # Get the style attrs for the spanner column headings
    # spanner_style_attrs = subset(styles_tbl, locname == "columns_groups")
    # Get the style attrs for the spanner column headings
    # column_style_attrs = subset(styles_tbl, locname == "columns_columns")

    # If columns are present in the stub, then replace with a set stubhead label or nothing
    if len(stub_layout) > 0 and len(stubh.label) > 0:
        headings_labels = _insert_into_list(headings_labels, stubh.label)
        headings_vars = _insert_into_list(headings_vars, "::stub")
    elif len(stub_layout) > 0:
        headings_labels = _insert_into_list(headings_labels, "")
        headings_vars = _insert_into_list(headings_vars, "::stub")

    # Set a default alignment for the stubhead label
    stubhead_label_alignment = "left"

    # Initialize the column headings list
    table_col_headings = []

    # If there are no spanners, then we have to create the cells for the stubhead label
    # (if present) and for the column headings
    if spanner_row_count < 1:
        # Create the cell for the stubhead label
        if len(stub_layout) > 0:
            stubhead_style = None
            # FIXME: Ignore styles for now
            # if stubhead_style_attrs is not None and len(stubhead_style_attrs) > 0:
            #    stubhead_style = stubhead_style_attrs[0].html_style

            table_col_headings.append(
                tags.th(
                    class_=" ".join(
                        [
                            "gt_col_heading",
                            "gt_columns_bottom_border",
                            f"gt_{stubhead_label_alignment}",
                        ]
                    ),
                    rowspan=1,
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=headings_labels[0],
                    contents=HTML(headings_labels[0]),
                )
            )

        # Remove the first element from `headings_vars` and `headings_labels`
        headings_vars.pop(0)
        headings_labels.pop(0)

    #
    # Create the headings in the case where there are no spanners at all -------------------------
    #
    for i in range(len(headings_vars)):

        # NOTE: Ignore styles for now
        # styles_column = subset(column_style_attrs, colnum == i)
        #
        # Convert the code above this comment from R to valid python
        # if len(styles_column) > 0:
        #    column_style = styles_column[0].html_style
        column_style = None

        table_col_headings.append(
            tags.th(
                class_=" ".join(
                    ["gt_col_heading", "gt_columns_bottom_border", f"gt_{col_alignment[i]}"]
                ),
                rowspan=1,
                colspan=1,
                style=column_style,
                scope="col",
                id=headings_labels[i],
                contents=HTML(headings_labels[i]),
            )
        )

    table_col_headings = tags.tr(class_="gt_col_headings", contents=table_col_headings)

    #
    # Create the spanners in the case where there *are* spanners ---------------------------------
    #

    if spanner_row_count > 0:

        spanners = spanners_print_matrix(
            spanners = spanners,
            boxhead = boxhead,
            include_hidden = False
          )

        spanner_ids = spanners_print_matrix(
            spanners = spanners,
            boxhead = boxhead,
            include_hidden = False,
            ids = True
          )

        level_1_index = len(spanners) - 1

        # A list of <th> elements that will go in the first level; this
        # includes spanner labels and column labels for solo columns (don't
        # have spanner labels above them)
        level_1_spanners = []

        # A list of <th> elements that will go in the second row. This is
        # all column labels that DO have spanners above them.
        spanned_column_labels = []

        # Create the cell for the stubhead label
        if len(stub_layout) > 0:

            # NOTE: Ignore styles for now
            # if len(stubhead_style_attrs) > 0:
            #     stubhead_style = stubhead_style_attrs.html_style
            # else:
            #     stubhead_style = None
            stubhead_style = None

            level_1_spanners.append(
                tags.th(
                    class_=" ".join(
                        [
                            "gt_col_heading",
                            "gt_columns_bottom_border",
                            f"gt_{stubhead_label_alignment}",
                        ]
                    ),
                    rowspan=2,
                    colspan=len(stub_layout),
                    style=stubhead_style,
                    scope="colgroup" if len(stub_layout) > 1 else "col",
                    id=headings_labels[0],
                    contents=HTML(headings_labels[0]),
                )
            )

            headings_vars.pop(0)
            headings_labels.pop(0)


        # NOTE: Run-length encoding treats missing values as distinct from each other; in other
        # words, each missing value starts a new run of length 1
        spanners_rle = [(k, len(list(g))) for k, g in groupby(list(spanner_ids[level_1_index, :]))]

        # The `sig_cells` vector contains the indices of spanners' elements where the value is
        # either None, or, is different than the previous value; because None values are
        # distinct, every element that is None will be present in `sig_cells`
        sig_cells = [1] + [i+1 for i, (k, _) in enumerate(spanners_rle[:-1]) if k is None or k != spanners_rle[i-1][0]]

        # `colspans` matches `spanners` in length; each element is the number of columns that the
        # <th> at that position should span; if 0, then skip the <th> at that position
        colspans = [spanners_rle[j][1] if (j+1) in sig_cells else 0 for j in range(len(spanner_ids[level_1_index, :]))]

        for i, _ in enumerate(headings_vars):

            if spanner_ids[level_1_index][i] == {}:
                # NOTE: Ignore styles for now
                # styles_heading = filter(
                #     lambda x: x.get('locname') == "columns_columns" and x.get('colname') == headings_vars[i],
                #     styles_tbl if 'styles_tbl' in locals() else []
                # )
                #
                # heading_style = next(styles_heading, {}).get('html_style', None)
                heading_style = None

                # Get the alignment for the current column
                first_set_alignment = boxhead._get_boxhead_get_alignment_by_var(var=headings_vars[i])

                level_1_spanners.append(
                    tags.th(
                        class_=" ".join(
                            [
                                "gt_col_heading",
                                "gt_columns_bottom_border",
                                f"gt_{first_set_alignment}"
                            ]
                        ),
                        rowspan=2,
                        colspan=1,
                        style=heading_style,
                        scope="col",
                        id=headings_labels[i],
                        contents=HTML(headings_labels[i])
                            )
                    )

            elif spanner_ids[level_1_index][i] is not None:

                # If colspans[i] == 0, it means that a previous cell's
                # `colspan` will cover us
                if colspans[i] > 0:

                    # NOTE: Ignore styles for now
                    # FIXME: this needs to be rewritten
                    # styles_spanners = filter(
                    #    spanner_style_attrs,
                    #    locname == "columns_groups",
                    #    grpname == spanner_ids[level_1_index, ][i]
                    #  )
                    #
                    # spanner_style =
                    #   if (nrow(styles_spanners) > 0) {
                    #     styles_spanners$html_style
                    #   } else {
                    #     NULL
                    #   }
                    spanner_style = None

                    level_1_spanners.append(
                        tags.th(
                            class_=" ".join(
                                [
                                    "gt_center",
                                    "gt_columns_top_border",
                                    "gt_column_spanner_outer"
                                ]
                            ),
                            rowspan=1,
                            colspan=colspans[i],
                            style=spanner_style,
                            scope="colgroup" if colspans[i] > 1 else "col",
                            id=str(spanners[level_1_index][i]),
                            contents=tags.span(class_="gt_column_spanner", contents=HTML(spanners[level_1_index][i]))
                        )
                    )

        solo_headings = headings_vars[pd.isna(spanner_ids[level_1_index])]
        remaining_headings = headings_vars[~(headings_vars.isin(solo_headings))]

        remaining_headings_labels = boxhead
        remaining_headings_labels = remaining_headings_labels[remaining_headings_labels["var"].isin(remaining_headings)]
        remaining_headings_labels = remaining_headings_labels["column_label"].tolist()

        col_alignment = col_alignment[1:][~(headings_vars.isin(solo_headings))]

        if len(remaining_headings) > 0:

            spanned_column_labels = []

            for j in range(len(remaining_headings)):

                # Skip styles for now
                # styles_remaining = styles_tbl[
                #     (styles_tbl["locname"] == "columns_columns") &
                #     (styles_tbl["colname"] == remaining_headings[j])
                # ]
                #
                # remaining_style = (
                #     styles_remaining["html_style"].values[0]
                #     if len(styles_remaining) > 0
                #     else None
                # )
                remaining_style = None

                remaining_alignment = boxhead._get_boxhead_get_alignment_by_var(var=remaining_headings[j])

                spanned_column_labels.append(
                    tags.th(
                        class_=" ".join(
                            [
                                "gt_col_heading",
                                "gt_columns_bottom_border",
                                f"gt_{remaining_alignment}"
                            ]
                        ),
                        rowspan=1,
                        colspan=1,
                        style=remaining_style,
                        scope="col",
                        id=remaining_headings_labels[j],
                        contents=HTML(remaining_headings_labels[j])
                    )
                )

            table_col_headings = tags.tagList(
                tags.tr(
                  class = "gt_col_headings gt_spanner_row",
                  level_1_spanners
                ),
                tags.tr(
                  class = "gt_col_headings",
                  spanned_column_labels
                )
              )

        else:
        # Create the `table_col_headings` HTML component
            table_col_headings = tags.tr(
                class_="gt_col_headings gt_spanner_row",
                contents=level_1_spanners
            )

    if _get_spanners_matrix_height(data=data) > 2:

        higher_spanner_rows_idx = seq_len(nrow(spanner_ids) - 2)

        higher_spanner_rows = tags.tagList()

        for i in higher_spanner_rows_idx:

            spanner_ids_row = spanner_ids[i]
            spanners_row = spanners[i]
            spanners_vars = list(set(spanner_ids_row[~np.isnan(spanner_ids_row)].tolist()))

            # Replace NA values in spanner_ids_row with an empty string
            spanner_ids_row[np.isnan(spanner_ids_row)] = ""

            spanners_rle = [(k, len(list(g))) for k, g in groupby(list(spanner_ids_row))]

            sig_cells = [1] + [i+1 for i, (k, _) in enumerate(spanners_rle[:-1]) if k is None or k != spanners_rle[i-1][0]]

            colspans = [spanners_rle[j][1] if (j+1) in sig_cells else 0 for j in range(len(spanner_ids_row))]

            level_i_spanners = []

            for j in range(len(colspans)):

                if colspans[j] > 0:

                    # Skip styles for now
                    # styles_spanners = styles_tbl[
                    #     (styles_tbl["locname"] == "columns_groups") &
                    #     (styles_tbl["grpname"] in spanners_vars)
                    # ]
                    #
                    # spanner_style = (
                    #     styles_spanners["html_style"].values[0]
                    #     if len(styles_spanners) > 0
                    #     else None
                    # )
                    spanner_style = None

                    level_i_spanners.append(
                      tags.th(
                        class = paste(
                          c(
                            "gt_center",
                            "gt_columns_top_border",
                            "gt_column_spanner_outer"
                          ),
                          collapse = " "
                        ),
                        rowspan = 1,
                        colspan = colspans[j],
                        style = spanner_style,
                        scope = ifelse(colspans[j] > 1, "colgroup", "col"),
                        id = spanners_row[j],
                        if (spanner_ids_row[j] != "") {
                          tags.span(
                            class = "gt_column_spanner",
                            HTML(spanners_row[j])
                          )
                        }
                      )
                    )

            if len(stub_layout) > 0 and i == 1:

                level_i_spanners = tags.tagList(
                    tags.th(
                      rowspan = max(higher_spanner_rows_idx),
                      colspan = len(stub_layout),
                      scope = ifelse(length(stub_layout) > 1, "colgroup", "col")
                    ),
                    level_i_spanners
                  )

            higher_spanner_rows = tags.tagList(
                  higher_spanner_rows,
                  tags.tagList(
                    tags.tr(
                      class_="gt_col_headings gt_spanner_row",
                      level_i_spanners
                    )
                  )
                )

        table_col_headings = tags.tagList(
            higher_spanner_rows,
            table_col_headings,
            )

    table_col_headings

def rtl_modern_unicode_charset() -> str:
    """
    Returns a string containing a regular expression that matches all characters
    from RTL scripts that are supported by modern web browsers.
    """
    # The Hebrew Unicode character set (112 code points)
    hebrew_unicode_charset = r"[\u0590-\u05FF]"

    # The Arabic Unicode character set (256 code points)
    arabic_unicode_charset = r"[\u0600-\u06FF]"

    # The Syriac Unicode character set (80 code points)
    syriac_unicode_charset = r"[\u0700-\u074F]"

    # The Thaana Unicode character set (64 code points)
    thaana_unicode_charset = r"[\u0780-\u07BF]"

    # The Samaritan Unicode character set (61 code points)
    samaritan_unicode_charset = r"[\u0800-\u083F]"

    # The Mandaic Unicode character set (32 code points)
    mandaic_unicode_charset = r"[\u0840-\u085F]"

    # The combination of these RTL character sets
    rtl_modern_unicode_charset = (
        hebrew_unicode_charset + "|" +
        arabic_unicode_charset + "|" +
        syriac_unicode_charset + "|" +
        thaana_unicode_charset + "|" +
        samaritan_unicode_charset + "|" +
        mandaic_unicode_charset
    )

    return rtl_modern_unicode_charset

def _insert_into_list(lst: List[Any], el: Any) -> List[Any]:
    """
    Inserts an element into the beginning of a list and returns the updated list.

    Args:
        lst (List[Any]): The list to insert the element into.
        el (Any): The element to insert.

    Returns:
        List[Any]: The updated list with the element inserted at the beginning.
    """
    lst.insert(0, el)
    return lst


def _get_spanners_matrix_height(
    data: GTData, include_hidden: bool = False, omit_columns_row: bool = False
) -> int:
    """
    Returns the height of the spanners matrix.

    Args:
        data (GTData): The data to be used for rendering the table.
        include_hidden (bool, optional): Whether to include hidden columns in the table. Defaults to False.
        omit_columns_row (bool, optional): Whether to omit the columns row in the table. Defaults to False.

    Returns:
        int: The height of the spanners matrix.
    """
    spanners_matrix = spanners_print_matrix(
        spanners=data._spanners,
        boxhead=data._boxhead,
        include_hidden=include_hidden,
        omit_columns_row=omit_columns_row,
    )

    return len(spanners_matrix)


# Determine whether the table has any row labels or row groups defined and provide
# a simple list that contains at a maximum two components
def _get_stub_components(data: GTData):
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


def _get_stub_layout(data: GTData) -> List[str]:
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
def _stub_rownames_has_column(data: GTData) -> bool:
    return "row_id" in _get_stub_components(data=data)


# Determine whether the table should have row group labels set within a column in the stub
def _stub_group_names_has_column(data: GTData) -> bool:
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


def _row_groups_get(data: GTData) -> List[str]:
    return data._row_groups._d


def _summary_exists(data: GTData):
    return False
