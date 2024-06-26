# Laptop Investment Optimizer

## Опис
Це застосування обчислює максимальний капітал, який можна отримати, купуючи, ремонтуя та продаючи ноутбуки. Програма обирає оптимальні ноутбуки для купівлі, щоб максимізувати прибуток.

## Як запустити
1. Встановіть Python 3.6 або вище.
2. Збережіть код у файл `laptop_investment_optimizer.py`.
3. Запустіть програму, передавши кількість продуктів, початковий капітал, список цін та список прибутків:
   ```bash
   python laptop_investment_optimizer.py <num_products> <initial_capital> "<prices>" "<profits>"
    ```
   
    Наприклад:
    ```bash
   python laptop_investment_optimizer.py 2 1000 "[500, 200, 800, 300]" "[600, 300, 900, 400]"
    ```
   
Аргументи
1. `num_products`: Кількість ноутбуків, які можна купити.
2. `initial_capital`: Початковий капітал.
3. `prices`: Список цін на ноутбуки у форматі [p1,p2,...].
4. `profits`: Список прибутків від продажу ноутбуків у форматі [g1,g2,...].

Примітка
1. Переконайтеся, що списки цін і прибутків мають однакову довжину.
2. Використовуйте форматування списків у вигляді рядків з квадратними дужками та комами.

# Пояснення коду
## Основні функції
### Клас Profit
Цей клас представляє логіку для обчислення прибутку від купівлі та продажу ноутбуків.

```python
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
```

### Алгоритм роботи:

#### Ініціалізація (`__init__`):
1. Зберігає початковий капітал та кількість продуктів, які можна купити.
2. Сортує продукти за різницею між прибутком і ціною у порядку спадання.
#### Обчислення прибутку (`calculate_profit`):
1. Обирає продукти з максимальним прибутком, доки є можливість купити їх за наявний капітал і в межах дозволеної кількості продуктів.
2. Використовує жадібний алгоритм для вибору продуктів з найбільшим співвідношенням прибуток/ціна.
3. Якщо не вистачає капіталу для покупки продукту, відкладає його у чергу для повторної спроби після покупки інших продуктів.
#### Обробка відкладених продуктів (`try_delayed_products`):
1. Перевіряє відкладені продукти і намагається купити їх, якщо вистачає капіталу після обробки основних продуктів.

## Чому моє рішення ефективне
Моє рішення є ефективним завдяки використанню жадібного алгоритму та сортування продуктів:

#### Жадібний алгоритм: Дозволяє спочатку обирати продукти з найбільшим прибутком.
#### Сортування продуктів: Забезпечує, що найбільш вигідні продукти будуть розглянуті першими, що максимізує загальний прибуток.
### Класифікація у Big O нотації
1. Ініціалізація та сортування продуктів: O(N log N), де N - кількість продуктів.
2. Обчислення прибутку та обробка відкладених продуктів: O(N), де N - кількість продуктів, оскільки кожен продукт перевіряється лише один раз.
3. Загальна складність алгоритму: O(N log N), що є ефективним для обробки великої кількості продуктів і максимізації прибутку від їх купівлі та продажу.
