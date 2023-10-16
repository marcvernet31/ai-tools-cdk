import unittest

from index import handler

class TestStringMethods(unittest.TestCase):

    def test(self):
        handler({'url': 'https://www.youtube.com/watch?v=cPJKOwj4_x8'}, {})

if __name__ == '__main__':
    unittest.main()