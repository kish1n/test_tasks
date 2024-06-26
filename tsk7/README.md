# Pinata Candy Maximizer

## Опис
Це застосування обчислює максимальну кількість цукерок, які можна отримати, розбиваючи піньяти у правильному порядку. Користувач може вказати список значень піньят, і програма обчислить максимальну кількість цукерок, яку можна отримати.

## Як запустити
1. Встановіть Python 3.6 або вище.
2. Збережіть код у файл `pinata_candy_maximizer.py`.
3. Запустіть програму, передавши список значень піньят:
   ```bash
   python pinata_candy_maximizer.py <pinata_value1> <pinata_value2> ... <pinata_valueN>
    ```
Приклад 
    ```bash
    python pinata_candy_maximizer.py 3 1 5 8
    ```
## Пояснення коду
### Основні функції
#### Клас Pinatas
Цей клас представляє логіку для обчислення максимальної кількості цукерок
    
```python
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
```

## Алгоритм роботи:

### Ініціалізація (__init__):
1. Зберігає список значень піньят.
2. Обчислює початкові продукти (к-сть цукерок) для кожної піньяти.
### Обчислення кількості цукерок (calc_sum):
1. Обчислює продукт (кількість цукерок) для даної піньяти з урахуванням її сусідів.
### Максимізація кількості цукерок (max_sum):
1. Починає з 0 цукерок і поступово додає продукти від піньят, які розбиває.
2. Кожного разу обирає піньяту з найменшою вартістю, щоб максимізувати кількість цукерок від сусідів. 
3. Оновлює значення продуктів для сусідів після кожного розбивання.

## Чому моє рішення ефективне
Моє рішення є ефективним завдяки використанню жадібного алгоритму для вибору піньят з найменшою вартістю:

1. Жадібний алгоритм: Дозволяє максимізувати кількість цукерок на кожному кроці, вибираючи найменш вигідну піньяту для розбивання.
2. Оновлення продуктів: Після кожного розбивання оновлює продукти для сусідів, забезпечуючи, що кожен вибір є оптимальним для поточної ситуації.
# Класифікація у Big O нотації
1. Ініціалізація та обчислення початкових продуктів: O(N), де N - кількість піньят.
2. Максимізація кількості цукерок: O(N^2), оскільки кожного разу потрібно обирати мінімальну піньяту і оновлювати продукти для сусідів.