import backtrader as bt
import datetime 

class VIXStrategy(bt.Strategy):

    def __init__(self):
        # print(self.datas[0].lines.getlinealiases())
        # print(self.datas[1].lines.getlinealiases())

        # self.vix = self.datas[0].vixclose
        self.vix = self.datas[1].close
        self.spyopen = self.datas[0].open
        self.spyclose = self.datas[0].close

        self.invest = 0.0

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.vix[0] > 35:
            self.log('Previous VIX, %.2f' % self.vix[0])
            self.log('SPY Open, %.2f' % self.spyopen[0])

            if not self.position or self.broker.getcash() > 1000:
                size = int(self.broker.getcash() / self.spyopen[0])
                print("Buying {} SPY at {}".format(size, self.spyopen[0]))
                self.buy(size=size)
            
        if len(self.spyopen) % 20 == 0:
           self.log("Adding 1000 in cash, never selling. I now have {} in cash on the sidelines, invest: {}".format(self.broker.getcash(), self.invest))
           self.broker.add_cash(1000)
           self.invest += 1000

        if self.vix[0] < 12 and self.position:
           self.close()
