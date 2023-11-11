from __future__ import annotations

from ._gt_data import GTData


def tab_source_note(data: GTData, source_note: str):
    """
    Add a source note citation.

    Add a source note to the footer part of the gt table. A source note is
    useful for citing the data included in the table. Several can be added to the
    footer, simply use multiple calls of `tab_source_note()` and they will be
    inserted in the order provided. We can use Markdown formatting for the note,
    or, if the table is intended for HTML output, we can include HTML formatting.

    Parameters
    ----------
    source_note (str)
        Text to be used in the source note. We can optionally use the `md()` or
        `html()` helper functions to style the text as Markdown or to retain HTML
        elements in the text.

    Returns
    -------
    GT
        Result of the table operation.

    Examples
    --------
        >>> from gt import *
        >>> x = GT([{"a": 5, "b": 10}, {"a": 15, "b": 20}])
        >>>     .tab_source_note(source_note="Source note for the table.")
        >>> x
        >>> print(x)
    """

    return data._replace(_source_notes=data._source_notes + [source_note])
