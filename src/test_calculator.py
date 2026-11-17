import unittest
from calculator import calculator


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator function."""
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(calculator('add', 5, 3), 8)
        self.assertEqual(calculator('add', -5, 3), -2)
        self.assertEqual(calculator('add', 0, 0), 0)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(calculator('subtract', 5, 3), 2)
        self.assertEqual(calculator('subtract', 3, 5), -2)
        self.assertEqual(calculator('subtract', 0, 0), 0)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(calculator('multiply', 5, 3), 15)
        self.assertEqual(calculator('multiply', -5, 3), -15)
        self.assertEqual(calculator('multiply', 0, 100), 0)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(calculator('divide', 10, 2), 5)
        self.assertEqual(calculator('divide', 9, 3), 3)
        self.assertAlmostEqual(calculator('divide', 7, 2), 3.5)
    
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator('divide', 10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_invalid_operation(self):
        """Test that invalid operation raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator('power', 2, 3)
        self.assertIn("Unsupported operation", str(context.exception))


if __name__ == '__main__':
    unittest.main()
