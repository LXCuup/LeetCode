import unittest
from name_function_2 import get_formatted_name

class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name_2 = get_formatted_name('q','w')
		self.assertEqual(formatted_name_2,'Q W')

	def test_first_Last_middle_name(self):
		formatted_name_3 = get_formatted_name('a','d','s')
		self.assertEqual(formatted_name_3,'A S D')
unittest.main()