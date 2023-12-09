import backtrader as bt
import datetime

class BuyLowSellHigh(bt.Strategy):

    def __init__(self):
        self.spyopen = self.datas[0].open
        self.spyclose = self.datas[0].close

        self.order = None

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if not self.position:
            size = int(self.broker.getcash() / self.spyopen[0])
            print("Buying {} SPY at {}".format(size, self.spyopen[0]))
            self.order = self.buy(size=size)
        else:
            # cerebro.broker.setcommission(commission=0.005)
            cur_open = self.spyopen[0]
            if self.order.status == bt.Order.Completed and (cur_open - self.order.executed.price) > 0.01 * cur_open:
                self.close()


