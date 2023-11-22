import unittest
from unittest.mock import patch
from stock import main

class TestMain(unittest.TestCase):
    @patch('stock.get_stock_data')  # Mocking the get_stock_data function
    @patch('stock.visualize_stock_data')  # Mocking the visualize_stock_data function
    def test_main(self, mock_visualize, mock_get_stock):
        # Mocking user input
        with patch('builtins.input', return_value='AAPL'):
            main()

        # Asserting that get_stock_data and visualize_stock_data were called
        mock_get_stock.assert_called_once_with('AAPL')
        mock_visualize.assert_called_once()

if __name__ == '__main__':
    unittest.main()