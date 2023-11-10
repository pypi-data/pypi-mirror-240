# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
__all__ = ("is_none",)
import awkward as ak
from awkward._behavior import behavior_of
from awkward._dispatch import high_level_function
from awkward._layout import maybe_posaxis, wrap_layout
from awkward._nplikes.numpy_like import NumpyMetadata
from awkward._regularize import is_integer, regularize_axis
from awkward.errors import AxisError

np = NumpyMetadata.instance()


@high_level_function()
def is_none(array, axis=0, *, highlevel=True, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        axis (int): The dimension at which this operation is applied. The
            outermost dimension is `0`, followed by `1`, etc., and negative
            values count backward from the innermost: `-1` is the innermost
            dimension, `-2` is the next level up, etc.
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Returns an array whose value is True where an element of `array` is None;
    False otherwise (at a given `axis` depth).
    """
    # Dispatch
    yield (array,)

    # Implementation
    return _impl(array, axis, highlevel, behavior)


def _impl(array, axis, highlevel, behavior):
    axis = regularize_axis(axis)
    layout = ak.operations.to_layout(array)
    behavior = behavior_of(array, behavior=behavior)

    if not is_integer(axis):
        raise TypeError(f"'axis' must be an integer, not {axis!r}")

    def action(layout, depth, lateral_context, **kwargs):
        posaxis = maybe_posaxis(layout, axis, depth)

        if posaxis is not None and posaxis + 1 == depth:
            if layout.is_union or layout.is_record:
                return None

            elif layout.is_option:
                return ak.contents.NumpyArray(layout.mask_as_bool(valid_when=False))

            else:
                nplike = layout._backend.nplike
                return ak.contents.NumpyArray(
                    nplike.zeros(layout.length, dtype=np.bool_)
                )

        elif layout.is_leaf:
            raise AxisError(f"axis={axis} exceeds the depth of this array ({depth})")

    out = ak._do.recursively_apply(layout, action, behavior, numpy_to_regular=True)

    return wrap_layout(out, behavior, highlevel)
