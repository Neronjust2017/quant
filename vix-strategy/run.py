import backtrader as bt
import os
from VIXStrategy import VIXStrategy
import datetime

cerebro = bt.Cerebro()
cerebro.broker.setcash(10000)

# class SPYVIXData(bt.feeds.GenericCSVData):
#     # lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose',)
#     #
#     # params = (
#     #     ('dtformat', '%Y-%m-%d'),
#     #     ('date', 0),
#     #     ('spyopen', 1),
#     #     ('spyhigh', 2),
#     #     ('spylow', 3),
#     #     ('spyclose', 4),
#     #     ('spyadjclose', 5),
#     #     ('spyvolume', 6),
#     #     ('vixopen', 7),
#     #     ('vixhigh', 8),
#     #     ('vixlow', 9),
#     #     ('vixclose', 10)
#     # )
#
#     lines = ('spyopen', 'spyhigh', 'spylow', 'spyclose', 'spyadjclose', 'spyvolume', 'vixopen'
#              , 'vixhigh', 'vixlow', 'vixclose')
#
#     params = (
#         ('dtformat', '%Y-%m-%d'),
#         ('date', 0),
#         ('open', 1),
#         ('high', 2),
#         ('low', 3),
#         ('close', 4),
#         ('volume', 5),
#         ('openinterest', -1),
#         ('spyopen', 1),
#         ('spyhigh', 2),
#         ('spylow', 3),
#         ('spyclose', 4),
#         ('spyadjclose', 5),
#         ('spyvolume', 6),
#         ('vixopen', 7),
#         ('vixhigh', 8),
#         ('vixlow', 9),
#         ('vixclose', 10)
#     )
#
# class VIXData(bt.feeds.GenericCSVData):
#         params = (
#         ('dtformat', '%m/%d/%Y'),
#         ('date', 0),
#         ('vixopen', 1),
#         ('vixhigh', 2),
#         ('vixlow', 3),
#         ('vixclose', 4),
#         ('volume', -1),
#         ('openinterest', -1)
#     )

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

class VIXData(bt.feeds.GenericCSVData):
    params = (
        ('fromdate', datetime.datetime(2015, 1, 1)),
        ('todate', datetime.datetime(2023, 12, 1)),
        ('dtformat', '%m/%d/%Y'),
        ('datetime', 0),
        ('time', -1),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', -1),
        ('openinterest', -1),
    )

csv_file = os.path.dirname(os.path.realpath(__file__)) + "/SPY.csv"
vix_csv_file = os.path.dirname(os.path.realpath(__file__)) + "/VIX.csv"

spyVixDataFeed = SPYData(dataname=csv_file)
vixDataFeed = VIXData(dataname=vix_csv_file)
cerebro.adddata(spyVixDataFeed)
cerebro.adddata(vixDataFeed)

# print(spyVixDataFeed)
# print(vixDataFeed)

cerebro.addstrategy(VIXStrategy)

cerebro.run()
cerebro.plot(volume=False)
