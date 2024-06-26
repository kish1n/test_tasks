import csv
import argparse
from datetime import datetime
from collections import defaultdict
from typing import List, Set, Dict

class Struct:
    def __init__(self, user_id: int, product_id: int, timestamp: datetime):
        self.user_id = user_id
        self.product_id = product_id
        self.timestamp = timestamp

def read_csv(file_path: str) -> List[Struct]:
    records = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            record = Struct(
                int(row['user_id']), int(row['product_id']),
                datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            )
            records.append(record)
    return records

def get_visits(records: List[Struct]) -> Dict[int, Set[int]]:
    visits = defaultdict(set)
    for record in records:
        visits[record.user_id].add(record.product_id)
    return visits

def find_same_page(day1: Dict[int, Set[int]], day2: List[Struct]) -> Set[int]:
    res = set()
    for record in day2:
        if record.user_id in day1 and record.product_id in day1[record.user_id]:
            res.add(record.user_id)
    return res

def find_new_visits(day1: Dict[int, Set[int]], day2_rec: List[Struct]) -> Set[int]:
    day2 = get_visits(day2_rec)
    res = set()
    for user_id, products in day2.items():
        if user_id in day1:
            for product_id in products:
                if product_id not in day1[user_id]:
                    res.add(user_id)
                    break
    return res

def main():
    parser = argparse.ArgumentParser(description='Analyze website visits.')
    parser.add_argument('day1', type=str, help='Path to the first day CSV file')
    parser.add_argument('day2', type=str, help='Path to the second day CSV file')
    args = parser.parse_args()

    day1_records = read_csv(args.day1)
    day2_records = read_csv(args.day2)

    day1_visits = get_visits(day1_records)

    users_visited_same_page = find_same_page(day1_visits, day2_records)
    users_with_new_visits = find_new_visits(day1_visits, day2_records)

    print("Users who visited the same pages on both days:")
    print(users_visited_same_page)

    print("\nUsers who visited new pages on the second day:")
    print(users_with_new_visits)

if __name__ == "__main__":
    main()
