import asyncio
import yfinance as yf


async def main():
    data = await asyncio.gather(
        yf.async_download("AAPL", period="1d"),
        yf.async_download("MSFT", period="1d"),
    )
    for df in data:
        print(df.head())


if __name__ == "__main__":
    asyncio.run(main())

