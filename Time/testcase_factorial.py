import unittest 
from fact import factorial
from twoPn import fibonacci
from ologn import sort

class Time_Complexity_Test(unittest.TestCase):

	def testFactrial(self):
		result = factorial(5)
		excepted = 120
		self.assertEqual(result,excepted)
	
	def testFibonacci(self):
		result = fibonacci(5)
		self.assertEqual(result,5)

	def testSort(self):
		result = sort([5,4,2,3,1])
		self.assertEqual(result,[1,2,3,4,5])

	def test_Factorial(self):
		result = factorial(5)
		self.assertNotEqual(result,119)

	def test_Fibonacci(self):
		result = fibonacci(5)
		self.assertNotEqual(result,4)

	def test_Sort(self):
		result = sort([5,4,2,3,1])
		self.assertNotEqual(result,[1,2,4,3,5])	

	def test_factorial(self):
		result = factorial(5)
		self.assertTrue(result,120)	

	def test_fibonacci(self):
		result = fibonacci(5)
		self.assertTrue(result,5)

	def test_sort(self):
		result = sort([5,4,2,3,1])
		self.assertTrue(result,[1,2,3,4,5])

	def testfactorial(self):
		result = factorial(5)
		self.assertFalse(result,119)

	def testfibonacci(self):
		result = fibonacci(5)
		self.assertFalse(result,4)

	def testsort(self):
		result = sort([5,4,2,3,1])
		self.assertFalse(result,[1,2,4,3,5])	

		

						

if __name__ == '__main__':
    unittest.main()	