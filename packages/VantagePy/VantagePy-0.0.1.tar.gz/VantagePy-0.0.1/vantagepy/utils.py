from enum import Enum

__all__ = (
    "APIFunction",
    "DataType",
    "InvalidAPIKey",
    "Interval",
    "parse_url",
    "OutputSize",
)


def parse_url(url: str, **kwargs) -> str:
    new_url = url
    for i, (key, value) in enumerate(kwargs.items()):
        converted_value = value
        if type(value) == bool:
            converted_value = "true" if value else "false"
        else:
            converted_value = value
        if i != 0:
            new_url += "&"
        new_url += f"{key}={converted_value}"
    return new_url


class InvalidAPIKey(ValueError):
    pass


class EnumStr(Enum):
    def __str__(self) -> str:
        return self.value


class APIFunction(EnumStr):
    TIME_SERIES_INTRADAY = "TIME_SERIES_INTRADAY"
    TIME_SERIES_DAILY = "TIME_SERIES_DAILY"
    TIME_SERIES_WEEKLY = "TIME_SERIES_WEEKLY"
    TIME_SERIES_MONTHLY = "TIME_SERIES_MONTHLY"
    SYMBOL_SEARCH = "SYMBOL_SEARCH"


class Interval(EnumStr):
    ONE_MIN = "1min"
    FIVE_MINS = "5min"
    FIFTEEN_MINS = "15min"
    THIRTY_MINS = "30min"
    SIXTY_MINS = "60min"


class OutputSize(EnumStr):
    COMPACT = "compact"
    FULL = "full"


class DataType(EnumStr):
    JSON = "json"
    CSV = "csv"
