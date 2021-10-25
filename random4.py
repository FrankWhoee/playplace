from random import randint
import sys
import math
import numpy as np

randoms = []
for i in range(int(sys.argv[1])):
	randoms.append(randint(0,100) * 4)
for i in randoms:
	print("""
	            .long 0    # student ID
		    .long 0      # grade 0
		    .long 0      # grade 1
		    .long 0      # grade 2
		    .long {}      # grade 3
		    .long 0       # computed average
	""".format(i))
print(np.asarray(randoms)/4)
randoms.sort()
print(np.asarray(randoms)/4)
print("median: {}".format(randoms[math.ceil(len(randoms)/2) - 1]/4))
