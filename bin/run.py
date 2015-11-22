#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath('..'))
from optparse import OptionParser
from strategy.GeneticAlgorithmStrategy import GeneticAlgorithmStrategy

def main(argv):
	parser = OptionParser(usage="Usage: python run.py")
	#parser.add_option("-j", "--json",
	#	action="store_true",
	#	dest="json_flag",
	#	default=False,
	#	help="take JSON-formatted feature data")

	#parser.add_option("-c", "--csv",
	#	action="store_true", 
	#	dest="csv_flag",
	#	default=False,
	#	help="take CSV-formatted features data")

	#parser.add_option("-m", "--model",
	#	action="store_true", 
	#	dest="model_flag",
	#	default=False,
	#	help="load previously generated model")

	(options, filenames) = parser.parse_args()

	ga = GeneticAlgorithmStrategy()
	print ga.getSingleLimit()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
