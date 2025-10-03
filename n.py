import unittest
from utils import validate_input

class TestUtils(unittest.TestCase):
    def test_validate_input(self):
        valid_input = {'username': 'testuser', 'password': 'testpass'}
        self.assertIsNone(validate_input(valid_input))

        invalid_input = {'username': 'testuser'}
        with self.assertRaises(ValueError):
            validate_input(invalid_input)

if __name__ == '__main__':
    unittest.main()