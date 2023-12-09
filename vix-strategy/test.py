import backtrader as bt
import os

class Mydata(bt.feeds.GenericCSVData):

    # vix.csv
    # params = (
    #     ('nullvalue', float('NaN')),
    #     # ('dtformat', '%Y-%m-%d'),
    #     ('dtformat', '%m/%d/%Y'),
    #     # ('tmformat', '%H:%M:%S'),
    #     # ('datetime', 0),
    #     # ('time', -1),
    #     # ('open', 1),
    #     # ('high', 2),
    #     # ('low', 3),
    #     # ('close', 4),
    #     # ('volume', 5),
    #     # ('openinterest', 6),
    #     ('date', 0),
    #     ('vixopen', 1),
    #     ('vixhigh', 2),
    #     ('vixlow', 3),
    #     ('vixclose', 4),
    #     ('volume', -1),
    #     ('openinterest', -1)
    # )

    lines = ('spyopen', 'spyhigh', 'spylow', 'spyclose', 'spyadjclose', 'spyvolume', 'vixopen'
            , 'vixhigh', 'vixlow', 'vixclose')

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', -1),
        ('spyopen', 1),
        ('spyhigh', 2),
        ('spylow', 3),
        ('spyclose', 4),
        ('spyadjclose', 5),
        ('spyvolume', 6),
        ('vixopen', 7),
        ('vixhigh', 8),
        ('vixlow', 9),
        ('vixclose', 10)
    )

csv_file = os.path.dirname(os.path.realpath(__file__)) + "/spy_vix.csv"

data = Mydata(dataname=csv_file)

# print(data.lines)
# print(data.params)

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.run()

cerebro.plot()