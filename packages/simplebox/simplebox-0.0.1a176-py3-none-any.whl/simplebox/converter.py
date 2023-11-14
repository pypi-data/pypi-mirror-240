#!/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum

from ._handler._converter_handler._calculator import _Converter, _NumericType
from .enums import EnhanceEnum
from .number import Integer


class _UnitEnum(EnhanceEnum):
    """
    unit tools base class
    """
    def of(self, num: int or float) -> '_Converter':
        """
        Convert the input num to the selected enumeration
        """
        return _Converter(num, self.value)

    def to(self, unit: Enum) -> _NumericType:
        """
        equal call _UnitEnum.of(1).to(unit)
        """
        return self.of(1).to(unit)


class StorageUnit(_UnitEnum):
    """
    Storage unit conversion tool
    """
    BIT = Integer(1)
    BYTE = Integer(1 << 3)
    KB = Integer(1 << 13)
    MB = Integer(1 << 23)
    GB = Integer(1 << 33)
    TB = Integer(1 << 43)
    PB = Integer(1 << 53)
    EB = Integer(1 << 63)
    ZB = Integer(1 << 73)
    YB = Integer(1 << 83)
    BB = Integer(1 << 93)
    NB = Integer(1 << 103)
    DB = Integer(1 << 113)


class TimeUnit(_UnitEnum):
    """
    Time unit conversion tool
    """
    PICO_SECOND = Integer(1)
    NANO_SECOND = Integer(1 * 1000)
    MICRO_SECOND = Integer(1 * 1000 * 1000)
    MILLI_SECOND = Integer(1 * 1000 * 1000 * 1000)
    SECOND = Integer(1 * 1000 * 1000 * 1000 * 1000)
    MINUTE = Integer(1 * 1000 * 1000 * 1000 * 1000 * 60)
    HOUR = Integer(1 * 1000 * 1000 * 1000 * 1000 * 60 * 60)
    DAY = Integer(1 * 1000 * 1000 * 1000 * 1000 * 60 * 60 * 24)
