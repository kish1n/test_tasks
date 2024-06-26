import argparse

class Transaction:
    def __init__(self, txid, inputs, outputs):
        self.txid = txid
        self.inputs = inputs  # Список входов (каждый вход - это (txid, index))
        self.outputs = outputs  # Список выходов (каждый выход - это (address, amount))

class Blockchain:
    def __init__(self):
        self.transactions = []
        self.utxo_pool = {}

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
        for i, out in enumerate(transaction.outputs):
            self.utxo_pool[(transaction.txid, i)] = out

    def filter_transactions(self):
        filtered = []
        for tx in self.transactions:
            if len(tx.inputs) == 1 and len(tx.outputs) == 2:
                filtered.append(tx)
        return filtered

    def build_graph(self, filtered_txs):
        graph = {}

        for tx in filtered_txs:
            tx_outputs = [(tx.txid, i) for i in range(len(tx.outputs))]
            for tx_out in tx_outputs:
                for next_tx in filtered_txs:
                    if tx_out in next_tx.inputs:
                        if tx.txid not in graph:
                            graph[tx.txid] = []
                        graph[tx.txid].append(next_tx.txid)
        return graph

    def find_longest_chain(self, graph):
        visited = set()
        longest_chains = []
        longest_length = 0

        def dfs(txid, path):
            nonlocal longest_chains
            nonlocal longest_length
            path.append(txid)
            visited.add(txid)

            if len(path) > longest_length:
                longest_length = len(path)
                longest_chains = [path[:]]  # Сбросить список, если нашли более длинную цепочку
            elif len(path) == longest_length:
                longest_chains.append(path[:])  # Добавить цепочку, если она такой же длины

            for neighbor in graph.get(txid, []):
                if neighbor not in visited:
                    dfs(neighbor, path)

            path.pop()
            visited.remove(txid)

        for txid in graph:
            dfs(txid, [])

        return longest_chains

def load_transactions_from_file(file_path):
    blockchain = Blockchain()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            txid, rest = line.split(': ')
            inputs, outputs = rest.split(' -> ')
            input_txid, input_index = inputs.split(', ')
            input_index = int(input_index)
            inputs = [(input_txid, input_index)]
            outputs = outputs.split('; ')
            outputs = [tuple(output.split(', ')) for output in outputs]
            outputs = [(address, float(amount)) for address, amount in outputs]
            blockchain.add_transaction(Transaction(txid, inputs, outputs))
    return blockchain

def main():
    parser = argparse.ArgumentParser(description="Find the longest UTXO chain in the blockchain.")
    parser.add_argument('file', type=str, help="Path to the transaction file")
    args = parser.parse_args()

    blockchain = load_transactions_from_file(args.file)
    filtered_txs = blockchain.filter_transactions()
    graph = blockchain.build_graph(filtered_txs)
    longest_chains = blockchain.find_longest_chain(graph)

    print("Longest UTXO chains:", longest_chains)

if __name__ == "__main__":
    main()