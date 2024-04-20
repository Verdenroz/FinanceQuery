from pydantic import BaseModel, Field
from decimal import Decimal


class Stock(BaseModel):
    symbol: str = Field(..., example="AAPL", description="Stock symbol")
    name: str = Field(..., example="Apple Inc.", description="Company name")
    price: Decimal = Field(..., example=145.00, description="Last traded price of the stock")
    change: str = Field(..., example="+1.00", description="Change in the stock price")
    percent_change: str = Field(..., example="+0.69%", description="Percentage change in the stock price")