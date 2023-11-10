# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
__all__ = ("nan_to_none",)
import awkward as ak
from awkward._behavior import behavior_of
from awkward._dispatch import high_level_function
from awkward._layout import wrap_layout
from awkward._nplikes.numpy_like import NumpyMetadata

np = NumpyMetadata.instance()


@high_level_function()
def nan_to_none(array, *, highlevel=True, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Converts NaN ("not a number") into None, i.e. missing values with option-type.

    See also #ak.nan_to_num to convert NaN or infinity to specified values.
    """
    # Dispatch
    yield (array,)

    # Implementation
    return _impl(array, highlevel, behavior)


def _impl(array, highlevel, behavior):
    def action(layout, continuation, **kwargs):
        if isinstance(layout, ak.contents.NumpyArray) and issubclass(
            layout.dtype.type, np.floating
        ):
            mask = layout.backend.nplike.isnan(layout.data)
            return ak.contents.ByteMaskedArray(
                ak.index.Index8(mask, nplike=layout.backend.index_nplike),
                layout,
                valid_when=False,
            )

        elif (layout.is_option or layout.is_indexed) and (
            isinstance(layout.content, ak.contents.NumpyArray)
            and issubclass(layout.content.dtype.type, np.floating)
        ):
            return continuation()

        else:
            return None

    layout = ak.operations.to_layout(
        array, allow_record=False, allow_unknown=False, primitive_policy="error"
    )
    behavior = behavior_of(array, behavior=behavior)
    out = ak._do.recursively_apply(layout, action, behavior)
    return wrap_layout(out, behavior, highlevel)
