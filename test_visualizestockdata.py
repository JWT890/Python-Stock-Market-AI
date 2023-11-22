import unittest
from stock import visualize_stock_data

class TestVisualizeStockData(unittest.TestCase):
    def test_visualize_stock_data(self):
        # Mock data for testing
        data = {
            '2021-01-01': {'4. close': '100.00'},
            '2021-01-02': {'4. close': '110.00'},
            '2021-01-03': {'4. close': '120.00'}
        }
        
        # Call the function to be tested
        visualize_stock_data(data)
        
        # Assert that the plot is displayed without raising any exceptions
        # You can't really test the visualization output itself, but you can test that it doesn't error
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()