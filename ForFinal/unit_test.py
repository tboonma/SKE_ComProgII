import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self):
        self.mainTest = main()
        pass

    def test_a(self):
        self.assertEqual(main.a, False)


if __name__ == '__main__':
    unittest.main()