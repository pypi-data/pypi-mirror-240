"""FMP Stock Splits Calendar fetcher."""


from datetime import date
from typing import Any, Dict, List, Optional

from dateutil.relativedelta import relativedelta
from openbb_fmp.utils.helpers import create_url, get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_splits import (
    StockSplitCalendarData,
    StockSplitCalendarQueryParams,
)


class FMPStockSplitCalendarQueryParams(StockSplitCalendarQueryParams):
    """FMP Stock Split Calendar query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-split-calendar-api/
    """


class FMPStockSplitCalendarData(StockSplitCalendarData):
    """FMP Stock Split Calendar data."""


class FMPStockSplitCalendarFetcher(
    Fetcher[
        FMPStockSplitCalendarQueryParams,
        List[FMPStockSplitCalendarData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPStockSplitCalendarQueryParams:
        """Transform the query params. Start and end dates are set to a 1 year interval."""
        transformed_params = params

        now = date.today()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FMPStockSplitCalendarQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: FMPStockSplitCalendarQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        query_str = f"from={query.start_date}&to={query.end_date}"
        url = create_url(3, f"stock_split_calendar?{query_str}", api_key)

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPStockSplitCalendarQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPStockSplitCalendarData]:
        """Return the transformed data."""
        return [FMPStockSplitCalendarData.model_validate(d) for d in data]
