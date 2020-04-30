import unittest
import main

class TestMain(unittest.TestCase):
	def setUp(self):
		print('about to test a function')

	def tearDown(self):
		print('about to tearDown a function')

	def test_do_stuff(self):
		'''
		HI!!!!!
		'''
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'rrr'
		'''
		HI!!!!!
		'''
		'rrrrrr'
		result = main.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, 'please enter num')

if __name__ == '__main__':
	unittest.main()
