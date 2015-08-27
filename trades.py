#!/bin/python
import sys

class MarketGame():

    def __init__(self, prices):
        self.profitable_sells = []
        self.bought_stock_at = None
        self.prices = prices

    def total_profits(self, total_trade_limit):
        if len(self.profitable_sells) < total_trade_limit:
            return sum(self.profitable_sells)

        self.profitable_sells.sort()
        best_sells = self.profitable_sells[len(self.profitable_sells)-total_trade_limit:]
        return sum(best_sells)

    def sell(self, selling_price):
        if not self.currently_have_stock():
            # We don't have any stock to sell, just return
            return

        print "Selling with a profit of " + str(selling_price - self.bought_stock_at)

        self.profitable_sells.append(selling_price - self.bought_stock_at)
        self.bought_stock_at = None

    def buy(self, price):
        if self.currently_have_stock():
            # We already have stock!
            print ("We can't buy stock, we already own some")
            return

        self.bought_stock_at = price

    def currently_have_stock(self):
        return self.bought_stock_at is not None

    def maximum_profits(self, total_trade_limit):
        if self.prices is None or len(self.prices) == 0:
            return 0

        if total_trade_limit is None == 0:
            return 0

        for i in range(0, len(self.prices)):
            todays_price = self.prices[i]
            print "Today's Price:" + str(todays_price)

            if i+1 == len(self.prices):
                # last day, we must sell
                if self.currently_have_stock():
                    self.sell(todays_price)
            else:
                tomorrows_price = self.prices[i+1]

                if tomorrows_price > todays_price:
                    # stock goes higher tomorrow
                    if self.currently_have_stock():
                        # don't sell yet
                        continue
                    else:
                        self.buy(todays_price)
                else:
                    # stock went lower
                    # sell at the higher price
                    if self.currently_have_stock():
                        self.sell(todays_price)

        return self.total_profits(total_trade_limit)


def main():
    prices = [223600, 220980, 220450, 223480, 226680, 224675, 222424, 223000, 221878, 221510, 223615, 222636, 220895, 224915, 223751, 224184, 221511, 217160, 219998, 215865]
    game = MarketGame(prices)
    max_profit = game.maximum_profits(sys.maxint)
    print "Maximum Profit with unlimited trades: " + str(max_profit) + "\n\n"

    game = MarketGame(prices)
    max_profit = game.maximum_profits(2)
    print "Maximum Profit with 2 trades: " + str(max_profit)

if __name__ == "__main__":
    main()
