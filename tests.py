import unittest
from tbot.commands import calculate, translate


class CommandsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate_command(self):
        self.assertEqual(calculate('5*5'), 'Result: 25')

    def test_translate_command(self):
        self.assertEqual(translate('Ahmed'), 'أحمد')


if __name__ == "__main__":
    unittest.main()
