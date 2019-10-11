from random import randint, choice
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-x", dest="ntx", default="5")
parser.add_option("-i", dest="nint", default="5")
parser.add_option("-t", "--ntime", dest="ntime", default="10")
parser.add_option("-v", "--nvar", dest="nvar", default="2")
options, parser = parser.parse_args()

ntx = int(options.ntx)
nint = int(options.nint)
ntime = int(options.ntime)
nvar = int(options.nvar)

operations = ['W', 'R']

print(ntx)
for transaction in range(ntx):
	num_instructions = randint(1, nint)
	timestamp = randint(0, ntime)
	print(num_instructions, timestamp)

	for instruction in range(num_instructions):
		print(choice(operations), randint(0, nvar))