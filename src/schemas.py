from pydantic import BaseModel, Field
from decimal import Decimal


class Stock(BaseModel):
    symbol: str = Field(..., example="AAPL", description="Stock symbol")
    name: str = Field(..., example="Apple Inc.", description="Company name")
    price: Decimal = Field(..., example=145.00, description="Last traded price of the stock")
    change: str = Field(..., example="+1.00", description="Change in the stock price")
    percent_change: str = Field(..., example="+0.69%", description="Percentage change in the stock price")


class News(BaseModel):
    title: str = Field(..., example="New iPhone released!", description="Title of the news article")
    link: str = Field(..., example="https://www.example.com", description="Link to the news article")
    source: str = Field(..., example="CNN", description="Source of the news article")
    time: str = Field(..., example="1 day ago", description="Time relative to current time when the news was published")


class Quote(BaseModel):
    symbol: str = Field(..., example="AAPL", description="Stock symbol")
    name: str = Field(..., example="Apple Inc.", description="Company name")
    price: Decimal = Field(..., example=145.00, description="Last traded price of the stock")
    after_hours_price: Decimal = Field(..., example=145.50, description="After hours price of the stock")
    change: str = Field(..., example="+1.00", description="Change in the stock price")
    percent_change: str = Field(..., example="+0.69%", description="Percentage change in the stock price")
    open: Decimal = Field(..., example=144.00, description="Opening price of the stock")
    high: Decimal = Field(..., example=146.00, description="Highest day price of the stock")
    low: Decimal = Field(..., example=143.00, description="Lowest day price of the stock")
    year_high: Decimal = Field(..., example=150.00, description="52-week high price of the stock")
    year_low: Decimal = Field(..., example=100.00, description="52-week low price of the stock")
    volume: int = Field(..., example=1000000, description="Volume of the stock")
    avg_volume: int = Field(..., example=2000000, description="Average volume of the stock")
    market_cap: str = Field(..., example="2.5T", description="Market capitalization of the stock")
    beta: Decimal = Field(..., example=1.23, description="Beta of the stock")
    pe: Decimal = Field(..., example=30.00, description="Price to earnings ratio of the stock")
    eps: Decimal = Field(..., example=4.50, description="Earnings per share of the stock")
    dividend: Decimal = Field(..., example=0.82, description="Dividend yield of the stock")
    earnings_date: str = Field(..., example="Apr 23, 2024", description="Next earnings date of the stock")
    about: str = Field(...,
                       example="Apple Inc. designs, manufactures, and markets smartphones, personal computers, "
                               "tablets, wearables, and accessories worldwide.",
                       description="About the company")
    sector: str = Field(..., example="Technology", description="Sector of the company")
    industry: str = Field(..., example="Consumer Electronics", description="Industry of the company")
    similar_stocks: list[Stock] = Field(...,
                                        example=[{"symbol": "MSFT", "name": "Microsoft Corporation", "price": 300.00}],
                                        description="List of similar stocks")
    news: list[News] = Field(...,
                             example=[
                                 {"title": "New iPhone released!", "link": "https://www.example.com", "source": "CNN",
                                  "time": "1 day ago"}],
                             description="List of news articles")


class Index(BaseModel):
    name: str = Field(..., example="S&P 500", description="Name of the index")
    value: Decimal = Field(..., example=4300.00, description="Current value of the index")
    change: str = Field(..., example="+10.00", description="Change in the index value")
    percent_change: str = Field(..., example="+0.23%", description="Percentage change in the index value")


class MarketMover(BaseModel):
    symbol: str = Field(..., example="AAPL", description="Stock symbol")
    name: str = Field(..., example="Apple Inc.", description="Company name")
    price: Decimal = Field(..., example=145.00, description="Last traded price of the stock")
    change: str = Field(..., example="+1.00", description="Change in the stock price")
    percent_change: str = Field(..., example="+0.69%", description="Percentage change in the stock price")
