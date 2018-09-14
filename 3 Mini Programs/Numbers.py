# Kai Joseph
# Sept. 13, 2018
# Takes three numbers from the command line and tells whether the series is increasing, decreasing, or neither.
# Source: https://docs.python.org/3/tutorial/controlflow.html

import sys

x = float(sys.argv[1])

y = float(sys.argv[2])

z = float(sys.argv[3])

if x>y>z:
	print("\nDecreasing order.\n")
elif x<y<z:
	print("\nIncreasing order.\n")
else:
	print("\nNeither increasing nor decreasing order.\n")