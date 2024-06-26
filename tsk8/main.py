import argparse
from typing import List
from collections import deque

class Profit:
    def __init__(self, capital: int, num_products: int, prices: List[int], profits: List[int]):
        self.capital = capital
        self.num_products = num_products
        self.products = sorted(zip(prices, profits), key=lambda x: x[1] - x[0], reverse=True)
        self.queue = deque()

    def calculate_profit(self):
        while self.products and self.num_products > 0:
            price, gain = self.products.pop(0)

            if price >= gain:
                continue

            if self.capital >= price:
                while self.try_delayed_products() and self.num_products > 0:
                    pass

                if self.num_products <= 0:
                    break

                self.capital -= price
                self.capital += gain
                self.num_products -= 1

            else:
                self.queue.append((price, gain))

        while self.num_products > 0 and self.try_delayed_products():
            pass

        return self.capital

    def try_delayed_products(self):
        self.queue = deque(sorted(self.queue, key=lambda x: x[1] - x[0], reverse=True))
        for _ in range(len(self.queue)):
            price, gain = self.queue.popleft()

            if self.capital >= price and self.num_products > 0:
                self.capital -= price
                self.capital += gain
                self.num_products -= 1

                if self.num_products <= 0:
                    return False

                return True
            else:
                self.queue.append((price, gain))

        return False

def main():
    parser = argparse.ArgumentParser(description='Calculate final capital after buying and selling laptops.')
    parser.add_argument('num_products', type=int, help='Number of products you can buy')
    parser.add_argument('initial_capital', type=int, help='Initial capital')
    parser.add_argument('prices', type=str, help='List of product prices in the format [p1,p2,...]')
    parser.add_argument('profits', type=str, help='List of product profits in the format [g1,g2,...]')

    args = parser.parse_args()

    try:
        prices = eval(args.prices)
        profits = eval(args.profits)
    except:
        print("Invalid format for prices or profits. Please use the format [p1,p2,...] for both.")
        return

    if len(prices) != len(profits):
        print("The number of prices must match the number of profits.")
        return

    profit = Profit(args.initial_capital, args.num_products, prices, profits)
    final_capital = profit.calculate_profit()
    print(f'Final capital: {final_capital}')

if __name__ == '__main__':
    main()