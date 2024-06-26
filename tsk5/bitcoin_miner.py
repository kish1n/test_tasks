import csv
import time
import psutil
import sys

class Transaction:
    def __init__(self, tx_id, size, fee):
        self.tx_id = tx_id
        self.size = int(size)
        self.fee = int(fee)
        self.fpb = self.fee / self.size

def load_transactions(file_path):
    transactions = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                tx_id, size, fee = row
                transactions.append(Transaction(tx_id, size, fee))
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    return transactions

def construct_block(transactions, max_block_size=1000000):
    transactions.sort(key=lambda x: x.fpb, reverse=True)

    total_size = 0
    total_fee = 0
    block_transactions = []

    for tx in transactions:
        if total_size + tx.size <= max_block_size:
            block_transactions.append(tx)
            total_size += tx.size
            total_fee += tx.fee
        if total_size >= max_block_size:
            break

    return block_transactions, total_size, total_fee

def main(file_path):
    start_time = time.time()

    transactions = load_transactions(file_path)
    block, block_size, total_fee = construct_block(transactions)

    end_time = time.time()

    process = psutil.Process()
    memory_usage = process.memory_info().rss

    print(f"Constructed Block:")
    for tx in block:
        print(f"Transaction ID: {tx.tx_id}, Size: {tx.size} bytes, Fee: {tx.fee} satoshis")

    print(f"Amount of transactions in the block: {len(block)}")
    print(f"Block size: {block_size} bytes")
    print(f"Total extracted fee: {total_fee} satoshis")
    print(f"Construction time: {end_time - start_time} seconds")
    print(f"Max memory usage: {memory_usage} bytes")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bitcoin_miner.py <path_to_csv>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
