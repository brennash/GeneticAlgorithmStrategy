import json
import random
import collections

class GeneticAlgorithmStrategy:

	def __init__(self):
		random.seed()
		self.params = {}

		self.params['SingleLimit'] = random.random()
		self.params['DoubleLimit'] = random.random()
		self.params['TrebleLimit'] = random.random()
		self.params['AccumLimit'] = random.random()

		self.params['SingleAmount'] = 0.25
		self.params['DoubleAmount'] = 0.25
		self.params['TrebleAmount'] = 0.25
		self.params['AccumAmount'] = 0.25

	def mutate(self, limit):
		if limit > 0.0 and limit < 1.0:
			self.mutateParam('SingleLimit', limit)
			self.mutateParam('DoubleLimit', limit)
			self.mutateParam('TrebleLimit', limit)
			self.mutateParam('AccumLimit', limit)
	
	
	def mutateAmounts(self, limit):
		""" Adjusts the stake split such that the total split 
		    sums to 1.0 across all amounts. That way the breakdown
		    of amounts will be valid.
		"""

		keys = ['SingleAmount', 'DoubleAmount', 'TrebleAmount', 'AccumAmount']

		values = []
		values.append((0.5-random.random())/len(keys))
		values.append((0.5-random.random())/len(keys))
		values.append((0.5-random.random())/len(keys))
		total = sum(values)
		values.append(-1.0*total)
		
		randomValues = random.sample(values, len(values))

		for index, key in enumerate(keys):
			self.params[key] += values[index]
			if self.params[key] < 0.0:
				self.params[key] = 0.0
			elif self.params[key] > 1.0:
				self.params[key] = 1.0

			print self.params[key],key

	def mutateParam(self, key, limit):
		self.params[key] += (random.random()*limit) - (limit/2.0)
		if self.params[key] < 0.0:
			self.params[key] = 0.0
		elif self.params[key] > 1.0:
			self.params[key] = 1.0

	def getSingleLimit(self):
		return self.params['SingleLimit']
