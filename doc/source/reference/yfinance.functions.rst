=========================
Functions and Utilities
=========================

.. currentmodule:: yfinance
   
Download Market Data
~~~~~~~~~~~~~~~~~~~~~
The `download` function allows you to retrieve market data for multiple tickers at once.
An asynchronous variant `async_download` is also available for use with ``asyncio``.

.. autosummary:: 
   :toctree: api/

   download
   async_download

Example usage::

   import asyncio
   import yfinance as yf

   async def main():
       data = await asyncio.gather(
           yf.async_download("AAPL", period="1d"),
           yf.async_download("MSFT", period="1d"),
       )
       for df in data:
           print(df.head())

   asyncio.run(main())

Enable Debug Mode
~~~~~~~~~~~~~~~~~
Enables logging of debug information for the `yfinance` package.

.. autosummary:: 
   :toctree: api/

   enable_debug_mode

Set Timezone Cache Location
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sets the cache location for timezone data.

.. autosummary:: 
   :toctree: api/

   set_tz_cache_location
