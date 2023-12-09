import backtrader as bt
import os
from BuyLowSellHighStrategy import BuyLowSellHigh
import datetime

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)
cerebro.broker.setcommission(0.005)

class SPYData(bt.feeds.GenericCSVData):
    params = (
        ('fromdate', datetime.datetime(2015, 1, 1)),
        ('todate', datetime.datetime(2023, 12, 1)),
        ('dtformat', '%Y-%m-%d'),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', 6),
    )

csv_file = "/Users/nero/codes/trading/vix-strategy/BuyLowSellHighStrategy/NIO.csv"

spyDataFeed = SPYData(dataname=csv_file)

cerebro.adddata(spyDataFeed)

cerebro.addstrategy(BuyLowSellHigh)

cerebro.run()
cerebro.plot(volume=False)
