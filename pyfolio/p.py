import pyfolio as pf
import datetime
start=datetime.datetime(2018,1,1)
stock_rets = pf.utils.get_symbol_rets('FB',start)
pf.create_returns_tear_sheet(stock_rets)