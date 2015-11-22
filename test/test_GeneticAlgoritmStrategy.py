import unittest
import json, re
from strategy.GeneticAlgorithmStrategy import GeneticAlgorithmStrategy

class Test(unittest.TestCase):

	def test_getSingleLimit_1(self):
		ga = GeneticAlgorithmStrategy()
		value = ga.getSingleLimit()
		self.assertTrue(value > 0.0 and value < 1.0)

	def test_getSingleLimit_2(self):
		ga = GeneticAlgorithmStrategy()
		value1 = ga.getSingleLimit()
		ga.mutate(0.1)
		value2 = ga.getSingleLimit()
		self.assertTrue(value1 != value2)

	def test_getMutateAmounts_1(self):
		ga = GeneticAlgorithmStrategy()
		ga.mutateAmounts(0.1)
		self.assertTrue(True)



def main():
    unittest.main()

if __name__ == '__main__':
    main()


