from typing import TypeVar, Union

import numpy as np
import pint.facets

# Type aliases
Scalar = pint.facets.plain.quantity.Scalar
Magnitude = pint.facets.plain.quantity.Magnitude
PintQuantity = pint.facets.plain.quantity.PlainQuantity
ParamDataType = Union[
    type[bool],
    type[str],
    type[float],
    type[int],
    type[np.number],
    type[np.ndarray],
]

# TypeVars
ParamDataT = TypeVar("ParamDataT", bound=Union[bool, str, Scalar, Magnitude])
