# Kai 
# Sept. 13, 2018
# Takes three console arguments. The month, the date, and the year. It then prints out the day of the week from an array of strings.
# Source of Arrays: https://www.w3schools.com/python/python_arrays.asp
# Ethan told me that the formula uses floored division instead of standard division. I do not know his last name, so know that I am referring to the only Ethan in the class that I am in.

import sys

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

m = int(sys.argv[1])

d = int(sys.argv[2])

y = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0)//12) % 7

print(days[d0])