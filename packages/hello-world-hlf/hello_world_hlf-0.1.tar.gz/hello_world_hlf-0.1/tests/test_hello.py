import unittest
from io import StringIO
from unittest.mock import patch
from hello_world import say_hello

class TestHelloWorld(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_say_hello(self, mock_stdout):
        say_hello()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
