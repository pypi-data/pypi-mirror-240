"""GDP data and query params."""
from datetime import date as dateType
from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class GDPRealQueryParams(QueryParams):
    """Real GDP query."""

    units: Literal["idx", "qoq", "yoy"] = Field(
        default="yoy",
        description=QUERY_DESCRIPTIONS.get("units", "")
        + " Either idx (indicating 2015=100), "
        + "qoq (previous period) "
        + "or yoy (same period, previous year).)",
    )
    start_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class GDPRealData(Data):
    """Real GDP data."""

    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    value: Optional[float] = Field(
        default=None, description="Nominal GDP value on the date."
    )


QUERY_DESCRIPTIONS
