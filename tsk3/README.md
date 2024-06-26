# Website Analytics

## Опис
Це застосування аналізує відвідування сторінок на вебсайті. Програма отримує два CSV файли, кожен з яких містить дані про відвідування сторінок за один день. Завдання полягає у визначенні користувачів, які:
- Відвідували одні й ті самі сторінки обидва дні.
- Відвідували нові сторінки на другий день, яких не відвідували на перший день.

## Як запустити
1. Встановіть Python 3.6 або вище.
2. Збережіть код у файл `website_analytics.py`.
3. Підготуйте два CSV файли з даними про відвідування за кожен день. Формат файлів:
4. Запустіть програму, передавши шляхи до файлів CSV:
```bash
python website_analytics.py day1.csv day2.csv
```
Приклад: python website_analytics.py day1.csv day2.csv

## Формат CSV файлів
1. `user_id`: Ідентифікатор користувача.
2. `product_id`: Ідентифікатор продукту (сторінки).
3. `timestamp`: Час відвідування у форматі YYYY-MM-DD HH:MM:SS

## Пояснення коду
#### Основні функції

1. `read_csv(file_path: str) -> List[Struct]:` Зчитує дані з CSV файлу та повертає список записів.
2. `get_visits(records: List[Struct]) -> Dict[int, Set[int]]:` Створює словник відвідувань, де ключ - це user_id, а значення - множина product_id.
3. `find_same_page(day1: Dict[int, Set[int]], day2: List[Struct]) -> Set[int]:` Знаходить користувачів, які відвідували ті самі сторінки обидва дні.
4. `find_new_visits(day1: Dict[int, Set[int]], day2_rec: List[Struct]) -> Set[int]:` Знаходить користувачів, які відвідували нові сторінки на другий день

## Чому моє рішення ефективне
Моє рішення є ефективним завдяки використанню структур даних, які забезпечують швидкий доступ і маніпулювання даними:

1. Словники і множини: Використання словників (dict) та множин (set) дозволяє швидко перевіряти наявність елементів та виконувати операції об'єднання, перетину та різниці.
2. Алгоритм: Читання та обробка даних виконується в один прохід по файлу, що робить процес ефективним за часом.

## Класифікація у Big O нотації
1. Читання CSV файлів: O(N), де N - кількість записів у файлі.
2. Створення словника відвідувань: O(N), де N - кількість записів.
3. Пошук користувачів, які відвідували ті самі сторінки обидва дні: O(M), де M - кількість записів на другий день.
4. Пошук користувачів, які відвідували нові сторінки на другий день: O(M), де M - кількість записів на другий день.

Загальна складність алгоритму: O(N + M), де N - кількість записів у першому файлі, а M - кількість записів у другому файлі. Це забезпечує ефективну обробку навіть для великих обсягів даних.

