# Kai Joseph
# Sept. 13, 2018
# This program, as stated in the homework assignment description, will take 2 arguments from the command line and input them into an equation to produce the wind chill.

import sys

temperature = float(sys.argv[1])

windspeed = float(sys.argv[2])

print("Wind chill: " + str((35.74+(0.6215*temperature)+((0.4275*temperature)-35.75)*windspeed**0.16)))