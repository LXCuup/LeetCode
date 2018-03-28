#--coding:utf-8--
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
#测试name_function.py
	def test_first_last_name(self):
		#正确地处理Janis Joplin 这样的名字
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()