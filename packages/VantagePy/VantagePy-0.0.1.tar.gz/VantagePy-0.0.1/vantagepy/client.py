import requests

from .utils import APIFunction, DataType, Interval, InvalidAPIKey, OutputSize, parse_url

__all__ = ("Client",)


class Client:
    BASE_URL = "https://www.alphavantage.co/query?"

    def __init__(self, api_key: None = "") -> None:
        self.apikey = api_key

    def intraday(
        self,
        symbol: str,
        interval: Interval,
        adjusted: bool = False,
        os: OutputSize = OutputSize.COMPACT,
        dt: DataType = DataType.JSON,
        apikey: str = None,
    ) -> dict | str:
        apikey = apikey or self.apikey
        if apikey is None:
            raise InvalidAPIKey("Missing API Key")

        url = parse_url(
            self.BASE_URL,
            function=APIFunction.TIME_SERIES_INTRADAY,
            symbol=symbol,
            interval=interval,
            adjusted=adjusted,
            outputsize=os,
            datatype=dt,
            apikey=apikey,
        )

        r = requests.get(url)

        if dt == DataType.JSON:
            return r.json()
        return r.text

    def daily(
        self,
        symbol: str,
        os: OutputSize = OutputSize.COMPACT,
        dt: DataType = DataType.JSON,
        apikey: str = None,
    ) -> dict | str:
        apikey = apikey or self.apikey
        if apikey is None:
            raise InvalidAPIKey("Missing API Key")

        url = parse_url(
            self.BASE_URL,
            function=APIFunction.TIME_SERIES_INTRADAY,
            symbol=symbol,
            outputsize=os,
            datatype=dt,
            apikey=apikey,
        )
        r = requests.get(url)
        if dt == DataType.JSON:
            return r.json()
        return r.text

    def weekly(
        self, symbol: str, dt: DataType = DataType.JSON, apikey: str = None
    ) -> dict | str:
        apikey = apikey or self.apikey
        if apikey is None:
            raise InvalidAPIKey("Missing API Key")

        url = parse_url(
            self.BASE_URL,
            function=APIFunction.TIME_SERIES_WEEKLY,
            symbol=symbol,
            datatype=dt,
            apikey=apikey,
        )
        r = requests.get(url)
        if dt == DataType.JSON:
            return r.json()
        return r.text

    def monthly(
        self, symbol: str, dt: DataType = DataType.JSON, apikey: str = None
    ) -> dict | str:
        apikey = apikey or self.apikey
        if apikey is None:
            raise InvalidAPIKey("Missing API Key")

        url = parse_url(
            self.BASE_URL,
            function=APIFunction.TIME_SERIES_MONTHLY,
            symbol=symbol,
            datatype=dt,
            apikey=apikey,
        )
        r = requests.get(url)
        if dt == DataType.JSON:
            return r.json()
        return r.text

    def search(
        self, keywords: str, dt: DataType = DataType.JSON, apikey: str = None
    ) -> dict | str:
        apikey = apikey or self.apikey
        if apikey is None:
            raise InvalidAPIKey("Missing API Key")

        url = parse_url(
            self.BASE_URL,
            function=APIFunction.SYMBOL_SEARCH,
            keywords=keywords,
            datatype=dt,
            apikey=apikey,
        )
        r = requests.get(url)
        if dt == DataType.JSON:
            return r.json()
        return r.text
