class Order:
    def __init__(self, user_id, amount, price, side):
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.side = side


class BalanceChange:
    def __init__(self, user_id, value, currency):
        self.user_id = user_id
        self.value = value
        self.currency = currency

    def __str__(self):
        return f'User: {self.user_id}, Value: {self.value}, Currency: {self.currency}'


class OrderBook:
    def __init__(self):
        self.buys = []
        self.sells = []

    def add_order(self, order):
        if order.side == 'buy':
            self.buys.append(order)
            self.buys.sort(key=lambda x: x.price, reverse=True)
        else:
            self.sells.append(order)
            self.sells.sort(key=lambda x: x.price)
        self.match_orders()

    def match_orders(self):
        while self.buys and self.sells and self.buys[0].price >= self.sells[0].price:
            buy_order = self.buys[0]
            sell_order = self.sells[0]

            if buy_order.user_id == sell_order.user_id:
                self.buys.pop(0)
                continue

            matched_amount = min(buy_order.amount, sell_order.amount)
            total_price = matched_amount * sell_order.price

            print(
                f'Match found: Buyer {buy_order.user_id} buys {matched_amount} UAH '
                f'from Seller {sell_order.user_id} at price {sell_order.price} USD/UAH'
            )
            print(BalanceChange(buy_order.user_id, -total_price, 'USD'))
            print(BalanceChange(buy_order.user_id, matched_amount, 'UAH'))
            print(BalanceChange(sell_order.user_id, total_price, 'USD'))
            print(BalanceChange(sell_order.user_id, -matched_amount, 'UAH'))

            buy_order.amount -= matched_amount
            sell_order.amount -= matched_amount

            if buy_order.amount == 0:
                self.buys.pop(0)
            if sell_order.amount == 0:
                self.sells.pop(0)


def main():
    order_book = OrderBook()

    while True:
        try:
            user_input = input("Enter order (user_id, amount, price, side): ")
            if not user_input:
                break

            user_input = user_input.replace(" ", "")
            user_id, amount, price, side = user_input.split(',')

            user_id = int(user_id)
            amount = int(amount)
            price = float(price)
            side = side.lower()

            if side not in ['buy', 'sell']:
                print("Invalid side. Please enter 'buy' or 'sell'.")
                continue

            order_book.add_order(Order(user_id, amount, price, side))
        except ValueError:
            print("Invalid input. Please enter the order in the format: user_id, amount, price, side")


if __name__ == "__main__":
    main()
