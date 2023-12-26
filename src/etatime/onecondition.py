from dataclasses import dataclass
from typing import Any


@dataclass
class Test:
    @staticmethod
    def type(value: Any, value_type: type) -> bool:
        return type(value) is value_type

    @staticmethod
    def instance(value: Any, value_type: type) -> bool:
        return isinstance(value, value_type)

    @staticmethod
    def positive(value: int | float) -> bool:
        return value > 0

    @staticmethod
    def negative(value: int | float) -> bool:
        return value < 0

    @staticmethod
    def non_positive(value: int | float) -> bool:
        return value <= 0

    @staticmethod
    def non_negative(value: int | float) -> bool:
        return value >= 0

    @staticmethod
    def range_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> bool:
        return minimum <= value <= maximum

    @staticmethod
    def range_non_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> bool:
        return minimum < value < maximum

    @staticmethod
    def gt(first: int | float, second: int | float) -> bool:
        return first > second

    @staticmethod
    def gte(first: int | float, second: int | float) -> bool:
        return first >= second

    @staticmethod
    def lt(first: int | float, second: int | float) -> bool:
        return first < second

    @staticmethod
    def lte(first: int | float, second: int | float) -> bool:
        return first <= second


class ValidationError(ValueError):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(message)


@dataclass
class Validate:
    @staticmethod
    def type(value: Any, value_type: type) -> None:
        if not Test.type(value, value_type):
            raise ValidationError(f"Value '{value}' must be of type {value_type}, not {type(value)}")

    @staticmethod
    def instance(value: Any, value_type: type) -> None:
        if not Test.instance(value, value_type):
            raise ValidationError(f"Value '{value}' must be an instance of {value_type}, not a {type(value)}")

    @staticmethod
    def positive(value: int | float) -> None:
        if not Test.positive(value):
            raise ValidationError(f"Value '{value}' must be positive (non-zero)")

    @staticmethod
    def negative(value: int | float) -> None:
        if not Test.negative(value):
            raise ValidationError(f"Value '{value}' must be negative (non-zero)")

    @staticmethod
    def non_positive(value: int | float) -> None:
        if not Test.non_positive(value):
            raise ValidationError(f"Value '{value}' must not be positive")

    @staticmethod
    def non_negative(value: int | float) -> None:
        if not Test.non_negative(value):
            raise ValidationError(f"Value '{value}' must not be negative")

    @staticmethod
    def range_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> None:
        if not Test.range_inclusive(value, minimum, maximum):
            raise ValidationError(f"Value '{value}' must be between {minimum} and {maximum} (inclusive)")

    @staticmethod
    def range_non_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> None:
        if not Test.range_non_inclusive(value, minimum, maximum):
            raise ValidationError(f"Value '{value}' must be between {minimum} and {maximum} (non-inclusive)")

    @staticmethod
    def not_range_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> None:
        if Test.range_inclusive(value, minimum, maximum):
            raise ValidationError(f"Value '{value}' must not be between {minimum} and {maximum} (inclusive)")

    @staticmethod
    def not_range_non_inclusive(value: int | float, minimum: int | float, maximum: int | float) -> None:
        if Test.range_non_inclusive(value, minimum, maximum):
            raise ValidationError(f"Value '{value}' must not be between {minimum} and {maximum} (non-inclusive)")

    @staticmethod
    def gt(first: int | float, second: int | float) -> None:
        if not Test.gt(first, second):
            raise ValidationError(f"Value '{first}' must be greater than '{second}'")

    @staticmethod
    def gte(first: int | float, second: int | float) -> None:
        if not Test.gte(first, second):
            raise ValidationError(f"Value '{first}' must be greater than or equal to '{second}'")

    @staticmethod
    def lt(first: int | float, second: int | float) -> None:
        if not Test.lt(first, second):
            raise ValidationError(f"Value '{first}' must be less than '{second}'")

    @staticmethod
    def lte(first: int | float, second: int | float) -> None:
        if not Test.lte(first, second):
            raise ValidationError(f"Value '{first}' must be less than or equal to '{second}'")
