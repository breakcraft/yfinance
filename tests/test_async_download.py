import asyncio
import unittest
import pandas as pd

from tests.context import yfinance as yf, session_gbl


class TestAsyncDownload(unittest.TestCase):
    def test_async_download(self):
        data = asyncio.run(yf.async_download("MSFT", period="1d", session=session_gbl))
        self.assertIsInstance(data, pd.DataFrame)

    def test_async_download_concurrent(self):
        async def run():
            return await asyncio.gather(
                yf.async_download("AAPL", period="1d", session=session_gbl),
                yf.async_download("MSFT", period="1d", session=session_gbl),
            )

        results = asyncio.run(run())
        for df in results:
            self.assertIsInstance(df, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()

