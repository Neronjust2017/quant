import backtrader as bt
import datetime 

class BuyAndHoldStrategy(bt.Strategy):

    def __init__(self):
        self.close = self.datas[0].close

    def next(self):
        size = int(self.broker.getcash() / self.close[0])

        if not self.position:
            self.buy(size=size)
