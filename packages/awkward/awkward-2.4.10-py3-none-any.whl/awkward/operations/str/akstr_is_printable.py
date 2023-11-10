# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

__all__ = ("is_printable",)

import awkward as ak
from awkward._behavior import behavior_of
from awkward._dispatch import high_level_function
from awkward._layout import wrap_layout


@high_level_function(module="ak.str")
def is_printable(array, *, highlevel=True, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Replaces any string-valued data with True if the string is non-empty and
    consists only of printable Unicode characters, False otherwise.

    Replaces any bytestring-valued data with True if the string is non-empty
    and consists only of printable ASCII characters, False otherwise.

    Note: this function does not raise an error if the `array` does not
    contain any string or bytestring data.

    Requires the pyarrow library and calls
    [pyarrow.compute.utf8_is_printable](https://arrow.apache.org/docs/python/generated/pyarrow.compute.utf8_is_printable.html)
    or
    [pyarrow.compute.ascii_is_printable](https://arrow.apache.org/docs/python/generated/pyarrow.compute.ascii_is_printable.html)
    on strings and bytestrings, respectively.
    """
    # Dispatch
    yield (array,)

    # Implementation
    return _impl(array, highlevel, behavior)


def _impl(array, highlevel, behavior):
    from awkward._connect.pyarrow import import_pyarrow_compute

    pc = import_pyarrow_compute("ak.str.is_printable")
    behavior = behavior_of(array, behavior=behavior)

    out = ak._do.recursively_apply(
        ak.operations.to_layout(array),
        ak.operations.str._get_ufunc_action(
            pc.utf8_is_printable, pc.ascii_is_printable, bytestring_to_string=True
        ),
        behavior,
    )

    return wrap_layout(out, behavior, highlevel)
