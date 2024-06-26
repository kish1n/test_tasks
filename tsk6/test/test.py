import unittest
from tsk6.utxo_chain import Transaction, Blockchain, load_transactions_from_file


class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = load_transactions_from_file('transactions_test.txt')

    def test_load_transactions(self):
        transactions = self.blockchain.transactions
        self.assertEqual(len(transactions), 11)
        self.assertEqual(transactions[0].txid, 'tx1')
        self.assertEqual(transactions[0].inputs, [('genesis', 0)])
        self.assertEqual(transactions[0].outputs, [('A', 0.5), ('B', 0.5)])

    def test_filter_transactions(self):
        filtered_txs = self.blockchain.filter_transactions()
        self.assertEqual(len(filtered_txs), 11)  # Все транзакции удовлетворяют условию фильтрации

    def test_build_graph(self):
        filtered_txs = self.blockchain.filter_transactions()
        graph = self.blockchain.build_graph(filtered_txs)
        expected_graph = {
            'tx1': ['tx2', 'tx3'],
            'tx2': ['tx4', 'tx5'],
            'tx3': ['tx6', 'tx7'],
            'tx4': ['tx8'],
            'tx5': ['tx9'],
            'tx6': ['tx10'],
            'tx7': ['tx11']
        }
        self.assertEqual(graph, expected_graph)

    def test_find_longest_chain(self):
        filtered_txs = self.blockchain.filter_transactions()
        graph = self.blockchain.build_graph(filtered_txs)
        longest_chains = self.blockchain.find_longest_chain(graph)

        expected_chains = [
            ['tx1', 'tx2', 'tx4', 'tx8'],
            ['tx1', 'tx2', 'tx5', 'tx9'],
            ['tx1', 'tx3', 'tx6', 'tx10'],
            ['tx1', 'tx3', 'tx7', 'tx11']
        ]

        # Проверка всех цепочек
        self.assertTrue(any(chain in expected_chains for chain in longest_chains))


if __name__ == '__main__':
    unittest.main()
