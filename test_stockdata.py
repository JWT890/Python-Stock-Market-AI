import unittest
from stock import get_stock_data

class TestStockData(unittest.TestCase):
    def test_get_stock_data(self):
        company_symbol = 'AAPL'
        stock_data = get_stock_data(company_symbol)
        self.assertIsNotNone(stock_data)

if __name__ == '__main__':
    unittest.main()