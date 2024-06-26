import unittest
from main import Profit

class TestProfit(unittest.TestCase):

    def test_scenario_1(self):
        capital = 50
        num_products = 3
        prices = [50, 60, 300, 110, 1111, 250]
        profits = [120, 70, 400, 290, 2222, 3455]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 3505)

    def test_scenario_2(self):
        capital = 100
        num_products = 2
        prices = [50, 200, 150, 400]
        profits = [70, 300, 200, 500]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 120)

    def test_scenario_3(self):
        capital = 500
        num_products = 1
        prices = [100, 200, 300]
        profits = [150, 250, 350]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 550)

    def test_scenario_4(self):
        capital = 1000
        num_products = 4
        prices = [50, 500, 300, 200]
        profits = [60, 600, 400, 250]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 1260)

    def test_scenario_5(self):
        capital = 50
        num_products = 0
        prices = [50, 60, 70]
        profits = [80, 90, 100]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 50)

    def test_scenario_6(self):
        capital = 100
        num_products = 10
        prices = [50, 1000, 100, 450, 100, 25, 1500, 200, 3300, 50, 200, 100]
        profits = [100, 1100, 110, 800, 110, 35, 110, 200, 310, 100, 450, 300]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 1130)

    def test_negative_profits(self):
        capital = 100
        num_products = 3
        prices = [50, 60, 70, 80]
        profits = [40, 50, 60, 70]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 100)  # No purchase should be made due to negative profits

    def test_equal_prices_different_profits(self):
        capital = 200
        num_products = 2
        prices = [100, 100, 100]
        profits = [150, 200, 250]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 450)  # Should pick the two highest profits

    def test_large_delayed_queue(self):
        capital = 50
        num_products = 3
        prices = [100, 200, 300, 400, 500]
        profits = [150, 250, 350, 450, 550]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 50)  # Should eventually buy the first three profitable items

    def test_dynamic_capital_increase(self):
        capital = 100
        num_products = 3
        prices = [50, 200, 50, 100, 400]
        profits = [60, 250, 70, 150, 500]
        profit = Profit(capital, num_products, prices, profits)
        final_capital = profit.calculate_profit()
        self.assertEqual(final_capital, 180)


if __name__ == '__main__':
    unittest.main()