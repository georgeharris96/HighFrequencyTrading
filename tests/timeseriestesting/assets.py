class Assets(object):
    def __init__(self, money=0, shares=0):
        self.money = money
        self.shares = shares
        self.shares_history = [shares]
        self.money_history = [money]

    def buy(self, open_price):
        self.shares = self.money / open_price
        self.shares_history.append(self.shares)
        self.money = 0
        self.money_history.append(self.money)
        pass

    def sell(self, close_price):
        self.money = close_price * self.shares
        self.money_history.append(self.money)
        self.shares = 0
        pass

    def closure(self, close_price):
        self.money = close_price * self.shares
        self.money_history.append(self.money)
        self.shares = 0
        self.shares_history.append(0)
        pass

    def get_history(self):
        return self.money_history, self.shares_history
