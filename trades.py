#!/bin/python
import sys

class MarketGame():
    total_profits = 0
    bought_stock_at = None
    prices = None

    def __init__(self, prices):
        self.prices = prices

    def sell(self, selling_price):
        if self.bought_stock_at is None:
            # We don't have any stock to sell, just return
            return

        print "Selling with a profit of " + str(selling_price - self.bought_stock_at)

        self.total_profits += selling_price - self.bought_stock_at
        self.bought_stock_at = None

    def buy(self, price):
        if self.bought_stock_at is not None:
            # We already have stock!
            print ("We can't buy stock, we already own some")
            return

        self.bought_stock_at = price

    def currently_have_stock(self):
        return self.bought_stock_at is not None

    def maximum_profits(self, prices, total_trade_limit):
        if prices is None or len(prices) == 0:
            return total_profits

        if total_trade_limit is None == 0:
            return total_profits

        for i in range(0, len(prices)):
            todays_price = prices[i]
            print "Today's Price:" + str(todays_price)

            if i+1 == len(prices):
                # last day, we must sell
                if self.currently_have_stock():
                    print "Must sell for the last day"
                    self.sell(todays_price)
                else:
                    print "Don't need to sell on the last day"
            else:
                tomorrows_price = prices[i+1]

                if tomorrows_price > todays_price:
                    # stock goes higher tomorrow
                    if self.currently_have_stock():
                        # don't sell yet
                        continue
                    else:
                        self.buy(todays_price)
                else:
                    # stock went lower
                    # sell at the higher price, we can buy tomorrow at the lower price
                    if self.currently_have_stock():
                        self.sell(todays_price)

        return self.total_profits

def main():
    prices = [223600, 220980, 220450, 223480, 226680, 224675, 222424, 223000, 221878, 221510, 223615, 222636, 220895, 224915, 223751, 224184, 221511, 217160, 219998, 215865]
    game = MarketGame(prices)
    max_profit = game.maximum_profits(prices, sys.maxint)
    print "Maximum Profit with unlimited trades: " + str(max_profit)
    #maximum_profits(prices, 4)

if __name__ == "__main__":
    main()
