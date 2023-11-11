import dataclasses
import importlib.resources
import warnings
from typing import Generic, Optional, Type

import numpy as np
import pint
import pint.facets
import pint_pandas

from . import errors
from .data_types import (
    ParamDataT,
    Magnitude,
    Scalar,
    PintQuantity as PintQuantityType,
    ParamDataType,
)
from .quantity_types import QuantityType
from .unit_types import UnitsT


# Global Pint UnitRegistry, settings and classes
UNITS_DEFINITIONS_FILE = importlib.resources.files(__package__) \
    .joinpath('pint_units.txt')
ureg = pint.UnitRegistry(
    default_as_delta=True,
    autoconvert_offset_to_baseunit=True,
    auto_reduce_dimensions=True,
    system='SI',
    cache_folder=':auto:'
)
with importlib.resources.as_file(UNITS_DEFINITIONS_FILE) as def_path:
    ureg.load_definitions(def_path)
pint_pandas.PintType.ureg = ureg  # Use global UnitsRegistry for new instances
ureg.default_format = '~'  # Short, not pretty (e.g. '1.5e-3 m ** 2')
PintQuantity = ureg.Quantity


class Quantity(Generic[UnitsT]):
    """
    A units and type-aware physical quantity
    """

    CAST_TYPE = float

    @classmethod
    def as_dataclass_field(
            cls,
            quantity_type: Type[QuantityType],
            description: str = '',
            default_magnitude: Optional[Magnitude] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        Return a dataclasses field with a default.
        Use this instead of passing objects of this class as or initializing it in field defaults directly.
        If the normal constructor (__init__) is used for a default value inside a dataclass,
        the identical object is referred in all instances of the dataclass.
        :param quantity_type: Type of the quantity e.g., 'Power'.
        :param description: Description of the quantity.
        :param default_magnitude: Default magnitude of the quantity.
        :param default_units: Default units of the quantity. Must be always
                              applied, if default_magnitude is set.
        :param value_comment: Comment for the given default quantity value
            (e.g. a reference)
        :return: The dataclass field
        """
        return dataclasses.field(
            default_factory=lambda: cls(
                quantity_type=quantity_type, description=description,
                default_magnitude=default_magnitude, default_units=default_units,
                value_comment=value_comment))

    def __init__(
            self,
            quantity_type: Type[QuantityType],
            description: str = '',
            default_magnitude: Optional[Magnitude] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        :param quantity_type: Type of the quantity e.g., 'Power'.
        :param description: Description of the quantity.
        :param default_magnitude: Default magnitude of the quantity.
            Must be given together with default_units.
        :param default_units: Default units of the quantity.
            Must be given together with default_magnitude.
        :param value_comment: Comment for the given default quantity value
            (e.g. a reference)
        """
        self._quantity: Optional[PintQuantityType] = None
        self.quantityType: Type[QuantityType] = quantity_type
        self.description: str = description
        self.valueComment: str = ''

        # Field to be set, when loading quantities
        if any(default is not None for default in [default_magnitude, default_units]):
            self.set(magnitude=default_magnitude, units=default_units,
                     value_comment=value_comment)

    def __repr__(self):
        return f'Quantity({self._quantity})'

    @property
    def quantity(self) -> Optional[PintQuantityType]:
        """
        Getter for the quantity
        :return: The quantity
        """
        if not hasattr(self, "_quantity"):
            msg = f"Value of this quantity is accessed before it " \
                  f"was set and no default value is available."
            warnings.warn(msg)
        return self._quantity

    @quantity.setter
    def quantity(self, quantity_: PintQuantityType):
        """
        Set the quantity.
        Check for units compatibility.
        :param quantity_: The quantity to set
        """
        try:
            # Cast quantity's magnitude to defined data_type
            quantity_ = PintQuantity(self.CAST_TYPE(quantity_.magnitude), quantity_.units)
        except ValueError:
            if not isinstance(quantity_.magnitude, self.CAST_TYPE):
                msg = f"Type of the given quantity ({type(quantity_.magnitude)}) is " \
                      f"not compatible with the defined data type ({self.CAST_TYPE})."
                raise errors.QuantityValueError(msg)
            else:
                raise
        try:
            # Convert to internal unit
            self._quantity = quantity_.to(self.quantityType.internal_units)  # type: ignore[misc]
        except pint.errors.DimensionalityError as err:
            msg = f"Unit of the given quantity ('{err.units1}' {err.dim1}) " \
                  f"does not fit to the predefined quantity unit " \
                  f"('{err.units2}' {err.dim2})."
            raise errors.QuantityUnitsError(msg)

    def set(self,
            quantity: Optional[PintQuantityType] = None,
            magnitude: Optional[Magnitude] = None,
            units: Optional[UnitsT] = None,
            value_comment: Optional[str] = None):
        """
        Set a quantity value by declaring magnitude and units.
        :param quantity: Value of the quantity.
            If None, magnitude and units are used to create a PintQuantity.
        :param magnitude: Magnitude of the quantity.
        :param units: Units of the quantity.
        :param value_comment: Comment for the quantity value (e.g. a reference)
        """
        if (quantity is not None) and (magnitude is None) and (units is None):
            self.quantity = quantity
        elif (quantity is None) and (magnitude is not None) and (units is not None):
            self.quantity = PintQuantity(magnitude, units)
        else:
            msg = f"Cannot set quantity. Either give a Pint quantity OR magnitude and units."
            raise errors.QuantityError(msg)
        if value_comment is not None:
            self.valueComment = value_comment

    def magnitude(self, units: UnitsT) -> Magnitude:
        """
        Return the magnitude of the quantity in given units
        :param units: Units in which the magnitude should be returned.
            If None, the default unit will be used.
        :return: Magnitude of the quantity
        """
        if self.quantity is not None:
            try:
                magnitude = self.quantity.m_as(units=units)
            except pint.errors.DimensionalityError as err:
                msg = f"Demanded unit ('{err.units2}'{err.dim2}) " \
                      f"does not fit to the predefined quantity units " \
                      f"('{err.units1}'{err.dim1})."
                raise errors.QuantityUnitsError(msg)
        else:
            magnitude = self.quantity
        return magnitude

    @property
    def internal_magnitude(self) -> Magnitude:
        """
        Return the magnitude of the quantity as internal units.
        """
        return self.magnitude(units=self.quantityType.internal_units)  # type: ignore[misc]

    @property
    def display_magnitude(self) -> Magnitude:
        """
        Return the magnitude of the quantity as default display units.
        If the quantity type does not define default display units,
        the magnitude is returned as internal units.
        """
        if self.quantityType.default_display_units is None:
            display_magnitude = self.internal_magnitude
        else:
            display_magnitude = self.magnitude(units=self.quantityType.default_display_units)
        return display_magnitude


class VectorQuantity(Quantity[UnitsT]):
    """
    A vector of unit-aware quantities
    """

    @classmethod
    def as_dataclass_field(
            cls,
            quantity_type: Type[QuantityType],
            description: str = '',
            default_magnitude: Optional[Magnitude] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        Return a dataclasses field with a default.
        Use this instead of passing objects of this class as or initializing it in field defaults directly.
        If the normal constructor (__init__) is used for a default value inside a dataclass,
        the identical object is referred in all instances of the dataclass.
        :param quantity_type: Type of the quantity e.g., 'Power'.
        :param description: Description of the quantity.
        :param default_magnitude: Default list of magnitudes of the vector.
        :param default_units: Default units of the vector. Must be always
                              applied, if default_magnitude is set.
        :param value_comment: Comment for the given default vector value
            (e.g. a reference)
        """
        return dataclasses.field(
            default_factory=lambda: cls(
                quantity_type=quantity_type, description=description,
                default_magnitude=default_magnitude, default_units=default_units,
                value_comment=value_comment))

    def __init__(
            self,
            quantity_type: Type[QuantityType],
            description: str = '',
            default_magnitude: Optional[Magnitude] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        :param quantity_type: Type of the quantity e.g., 'Power'.
        :param description: Description of the quantity.
        :param default_magnitude: Default list of magnitudes of the vector.
        :param default_units: Default units of the vector. Must be always
                              applied, if default_magnitude is set.
        :param value_comment: Comment for the given default vector value
            (e.g. a reference)
        """
        super().__init__(
            quantity_type=quantity_type, description=description,
            default_magnitude=default_magnitude, default_units=default_units,
            value_comment=value_comment)

    def __repr__(self):
        return f'VectorQuantity({self._quantity})'

    def set(self, quantity: Optional[PintQuantityType] = None,
            magnitude: Optional[Magnitude] = None,
            units: Optional[UnitsT] = None,
            value_comment: Optional[str] = None):
        """
        Set a quantity as a pint list by declaring magnitudes list and units.
        :param quantity: Value as a pint list of the vector.
            If None, magnitudes list and units are used to create a pint list.
        :param magnitude: List of magnitudes of the vector.
        :param units: Units of the vector.
        :param value_comment: Comment for the given vector value
        """
        super().set(quantity=quantity, magnitude=magnitude, units=units,
                    value_comment=value_comment)

    @property
    def quantity(self) -> Optional[PintQuantityType]:
        """
        Getter for the quantity
        :return: The quantity
        """
        return super().quantity

    @quantity.setter
    def quantity(self, quantity_: PintQuantityType):
        """
        Set the vector value.
        Check for units compatibility.
        :param quantity_: The quantity to set
        """
        try:
            # Cast value's magnitude to defined data_type
            quantity_ = PintQuantity(quantity_.magnitude.astype(self.CAST_TYPE),
                                     quantity_.units)
        except (ValueError, AttributeError):
            if not isinstance(quantity_.magnitude, np.ndarray):
                msg = f"Type of the given value ({type(quantity_.magnitude)}) is " \
                      f"not identical with the defined vector data type " \
                      f"({self.CAST_TYPE})."
                raise errors.QuantityValueError(msg)
            else:
                raise

        try:
            # Convert to internal unit
            self._quantity: PintQuantityType = quantity_.to(self.quantityType.internal_units)  # type: ignore[misc]
        except pint.errors.DimensionalityError as err:
            msg = f"Unit of the given value ('{err.units1}' {err.dim1}) " \
                  f"does not fit to the predefined quantity unit " \
                  f"('{err.units2}' {err.dim2})."
            raise errors.QuantityUnitsError(msg)


class Parameter(Generic[ParamDataT, UnitsT]):
    """
    A scalar parameter with either a unit-naive basic value or a unit-aware quantity value
    """
    def __init__(
            self,
            data_type: ParamDataType,
            quantity_type: Optional[Type[QuantityType[UnitsT]]] = None,
            description: str = '',
            default_magnitude: Optional[ParamDataT] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        :param data_type: Data type of the parameter.
        :param quantity_type: Type of the parameter's quantity e.g., 'Power'.
            A given quantity type's data type will override the given data type.
        :param description: Description of the parameter/quantity.
        :param default_magnitude: Default magnitude of the quantity.
            Must be given together with default_units.
        :param default_units: Default units of the quantity.
            Must be given together with default_magnitude.
        :param value_comment: Comment for the given default quantity value
            (e.g. a reference)
        """
        if data_type is None and quantity_type is None:
            err_msg = 'For parameter instantiation, either give a data type, or a quantity type.'
            raise errors.ParameterError(err_msg)

        self.dataType: ParamDataType
        self.quantityType: Optional[Type[QuantityType]] = quantity_type
        # The value of a units-aware parameter
        self._quantity: Optional[Quantity[UnitsT]]
        if quantity_type is None:
            self.dataType = data_type
            self._quantity = None
        else:
            self.dataType = Quantity.CAST_TYPE
            self._quantity = Quantity(quantity_type=quantity_type, description=description)

        # The value of a units-naive parameter
        self._value: Optional[ParamDataT] = None
        self.description: str = description
        self.valueComment: str = ''

        # Try initializing the value with given defaults
        if any(default is not None for default in [default_magnitude, default_units]):
            self.set(
                magnitude=default_magnitude, units=default_units,
                value_comment=value_comment)

    @property
    def quantity(self) -> Optional[PintQuantityType]:
        """
        Return the underlying quantity value, if applicable
        """
        if self.quantityType is None:
            msg = f'Cannot get parameter quantity. {self} does not define a quantity type.'
            raise errors.ParameterError(msg)
        else:
            return self._quantity.quantity

    @quantity.setter
    def quantity(self, quantity_: PintQuantityType):
        """
        Set the underlying quantity value, if applicable
        """
        if self.quantityType is None:
            msg = f'Cannot set parameter quantity. {self} does not define a quantity type.'
            raise errors.ParameterError(msg)
        else:
            self._quantity.quantity = quantity_

    def set(
            self,
            magnitude: Optional[ParamDataT] = None,
            units: Optional[UnitsT] = None,
            value_comment: Optional[str] = None):
        """
        Set the parameter value by declaring magnitude and units
        :param magnitude: Magnitude to be set
        :param units: Optional units for the magnitude
        :param value_comment: Comment for the quantity value (e.g. a reference)
        """
        if self.quantityType is None:
            if magnitude is None:
                self._value = magnitude
            else:
                try:
                    self._value = self.dataType(magnitude)
                except ValueError as e:
                    msg = f"Cannot cast given magnitude" \
                          f" ({magnitude}, type {type(magnitude)})" \
                          f" to the parameter's data type ({self.dataType})."
                    raise errors.ParameterValueError(msg) from e
            if units is not None:
                msg = f'Units f({units} given when setting units-naive parameter ({repr(self)}).)'
                warnings.warn(msg)
        else:
            self._quantity.set(
                magnitude=magnitude, units=units,
                value_comment=value_comment)

    def magnitude(self, units: Optional[UnitsT] = None) -> ParamDataT:
        """
        Return the magnitude (scalar value) of the parameter.
        For units-aware parameters, convert to given units.
        :param units: Units in which the quantity magnitude should be returned
        :return: Magnitude of the parameter.
        """
        if self.quantityType is None:
            return self._value
        else:
            if units is None:
                err_msg = 'Cannot convert magnitude of units-aware parameter.' \
                          ' No target units given.'
                raise errors.ParameterConversionError(err_msg)
            return self._quantity.magnitude(units=units)

    @property
    def internal_magnitude(self) -> ParamDataT:
        """
        Return the magnitude (scalar value) of the parameter.
        For units-aware parameters, convert to internal units.
        """
        if self.quantityType is None:
            return self._value
        else:
            return self._quantity.internal_magnitude

    @property
    def display_magnitude(self) -> ParamDataT:
        """
        Return the magnitude (scalar value) of the parameter.
        For units-aware parameters, convert to display units.
        """
        if self.quantityType is None:
            return self._value
        else:
            return self._quantity.display_magnitude


# ToDo @Olessya adjust comments
class VectorParameter(Parameter[ParamDataT, UnitsT]):
    """
    A vector parameter with either a unit-naive basic value or a unit-aware quantity value
    """
    CAST_TYPE = float

    def __init__(
            self,
            data_type: Optional[Type[ParamDataT]] = None,
            quantity_type: Optional[Type[QuantityType[UnitsT]]] = None,
            description: str = '',
            default_magnitude: Optional[ParamDataT] = None,
            default_units: Optional[UnitsT] = None,
            value_comment: str = ""):
        """
        :param data_type: Data type of the parameter.
        :param quantity_type: Type of the parameter's quantity e.g., 'Power'.
            A given quantity type's data type will override the given data type.
        :param description: Description of the parameter/quantity.
        :param default_magnitude: Default magnitude of the quantity.
            Must be given together with default_units.
        :param default_units: Default units of the quantity.
            Must be given together with default_magnitude.
        :param value_comment: Comment for the given default quantity value
            (e.g. a reference)
        """
        super().__init__(
            data_type=data_type, quantity_type=quantity_type, description=description,
            default_magnitude=default_magnitude, default_units=default_units,
            value_comment=value_comment)

        # The value of a units-aware vector parameter
        if quantity_type is not None:
            self._quantity = VectorQuantity(quantity_type=quantity_type, description=description)

    def set(
            self,
            magnitude: Optional[Magnitude] = None,
            units: Optional[UnitsT] = None,
            value_comment: Optional[str] = None):
        """
        Set the parameter value by declaring magnitude and units
        :param magnitude: Magnitude to be set
        :param units: Optional units for the magnitude
        :param value_comment: Comment for the quantity value (e.g. a reference)
        """
        super().set(magnitude=magnitude, units=units, value_comment=value_comment)

    @Parameter.quantity.setter
    def quantity(self, quantity_: PintQuantity):
        """
        Set the underlying quantity value, if applicable
        """
        if self.quantityType is None:
            msg = f'Cannot set parameter quantity. {self} does not define a quantity type.'
            raise errors.ParameterError(msg)
        else:
            try:
                quantity_ = PintQuantity(quantity_.magnitude.astype(self.CAST_TYPE),
                                         quantity_.units)
                self._quantity.quantity = quantity_
            except ValueError:
                if type(quantity_.magnitude) is not self.CAST_TYPE:
                    msg = f"Type of the given quantity ({type(quantity_.magnitude)}) is " \
                      f"not compatible with the defined data type ({self.CAST_TYPE})."
                    raise errors.QuantityValueError(msg)
