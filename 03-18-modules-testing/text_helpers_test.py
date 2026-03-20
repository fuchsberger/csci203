import unittest
from text_helpers import *

class TestTextHelpers(unittest.TestCase):

    def test_slug(self):
        self.assertEqual(slug("Hello World!", "hello_world"), "abcde")


suite = unittest.TestLoader().loadTestsFromTestCase(TestTextHelpers)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')
