import argparse
from typing import List
from collections import deque

class Pinatas:
    def __init__(self, pinats: List[int]):
        self.pinats = pinats
        self.length = len(pinats)
        self.products = [self.calc_sum(i) for i in range(self.length)]

    def calc_sum(self, i: int):
        left = self.pinats[i - 1] if i > 0 else self.pinats[0]
        right = self.pinats[i + 1] if i < self.length - 1 else self.pinats[0]
        return self.pinats[i] * left * right

    def max_sum(self):
        res = 0

        while self.length > 0:

            if res < 0:
                return 0

            min_value = min(self.pinats)
            min_index = self.pinats.index(min_value)
            res += self.products[min_index]

            self.pinats.pop(min_index)
            self.length -= 1

            if self.length == 0:
                break

            self.products.pop(min_index)

            if self.length == 1:
                self.products[0] = self.calc_sum(0)
            elif min_index == 0:
                self.products[0] = self.calc_sum(0)
                self.products[-1] = self.calc_sum(self.length-1)
                self.products[1] = self.calc_sum(1)
            elif min_index == self.length-1:
                self.products[self.length - 1] = self.calc_sum(self.length - 1)
                self.products[0] = self.calc_sum(self.length-2)
            else:
                self.products[min_index] = self.calc_sum(min_index)
                self.products[min_index - 1] = self.calc_sum(min_index - 1)
                self.products[min_index + 1] = self.calc_sum(min_index + 1)

        return res

def main():

    parser = argparse.ArgumentParser(description="Calculate the maximum amount of candies from smashing pinatas.")
    parser.add_argument('pinatas', metavar='N', type=int, nargs='+', help='List of pinata values')
    args = parser.parse_args()

    pinatas = Pinatas(args.pinatas)
    result = pinatas.max_sum()

    print("Max amount of candies:", result)

if __name__ == "__main__":
    main()


