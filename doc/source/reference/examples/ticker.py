import yfinance as yf

dat = yf.Ticker("MSFT")

# get historical market data
dat.history(period='1mo')
# request multi-week 1m data
dat.history(period='14d', interval='1m', span=True)

# options
dat.option_chain(dat.options[0]).calls

# get financials
dat.balance_sheet
dat.quarterly_income_stmt

# dates
dat.calendar

# general info
dat.info

# analysis
dat.analyst_price_targets

# websocket
dat.live()
