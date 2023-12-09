import backtrader as bt
import datetime 

class FearGreedStrategy(bt.Strategy):

    def __init__(self):
        self.fear_greed = self.datas[0].fear_greed
        self.close = self.datas[0].close
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        size = int(self.broker.getcash() / self.close[0])

        if self.fear_greed[0] < 10 and not self.position:
            self.log(">>> buy {}".format(self.broker.getcash()), self.datas[0].datetime.date(0))
            # self.log(self.position)
            self.buy(size=size)
        if self.fear_greed[0] > 90 and self.position.size > 0:
            # self.log(self.position)
            self.log("<<< sell ")
            self.sell(size=self.position.size)
            # self.log("<<< sell {}".format(self.position.size * self.close[0]))
