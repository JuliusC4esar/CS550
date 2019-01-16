# Kai
# Jan. 15, 2019
# Monte Carlo Simulation Project
# On my honor, I have neither given nor received unauthorised aid.
'''

Description:
For this project, I chose to program a cool mathematical simulation. The problem, while extremely advanced, has a surprisingly elegant solution. 
The problem is as follows. If you have a sphere (in this case of a 1-unit radius, though it does not really matter), and you randomly select four points on the SURFACE AREA of the sphere and connect the four points
to form a tetrahedron, what is the probability that the tetrahedron contains the center of the sphere? This algorithm solves the problem by generating a series of tetrahedrons and recording the results. If you increase
the number of loops, you will notice that the values get closer and more consistent to 1/8, or 12.5%. This is a 1/8 simulator.

'''

# Source: http://steve.hollasch.net/cgindex/geometry/ptintet.html (how to mathematically check if point is inside of tetrahedron)
# Source: https://matplotlib.org/ (matplotlib information)
# Source: http://www.numpy.org/ (numpy information)


import random
import numpy
import matplotlib.pyplot as plt

inside = 0 # Number of times the center of the sphere is inside of the random tetrahedron.

loops = 10000 # Number of loops

for i in range(loops):

	points = [[] for x in range(5)] # Reset the array that contains vertices of random tetrahedron. 5 lists in the array; 4 positions of vertices and 1 normalizing matrix for the upcoming calculations.

	for r in range(4): # Four vertices

		# Instantiate three values for the point (x,y,z). Ensure that the three values always result in a net distance of 1 unit from the center of the sphere so that it is on the surface area of a 1-unit radius sphere.
		dim1 = random.uniform(0,1)
		dim2 = random.uniform(0,(1-dim1**2)**0.5)
		dim3 = (1-(dim1**2)-(dim2**2))**0.5


		# Randomize the sign of the (x,y,z) values.
		dim1 = dim1*random.choice([-1,1])
		dim2 = dim2*random.choice([-1,1])
		dim3 = dim3*random.choice([-1,1])


		# Shuffle the (x,y,z) values to ensure a fully random point on the surface area of the sphere.
		dimensions = [dim1,dim2,dim3]
		random.shuffle(dimensions)


		# Assign the (x,y,z) values to three variables
		x = dimensions[0]
		y = dimensions[1]
		z = dimensions[2]


		# Add the position of the now fully completed and randomized tetrahedron vertex to the list of tetrahedron vertices.
		points[r].append(x)
		points[r].append(y)
		points[r].append(z)

		# Add a value of 1 as it is necessary for the upcoming matrix calculations.
		points[r].append(1)


	# Add the aforementioned normalizing values to the fifth and final list in the points array.
	for x in  range(3):
		points[4].append(0)

	points[4].append(1)


	# Perform determinant calculations with arrays formed by individual elements taken from the points array to calculate if the tetrahedron contains the center of the sphere.
	determinant1 = numpy.linalg.det([points[0],points[1],points[2],points[3]])
	determinant2 = numpy.linalg.det([points[4],points[1],points[2],points[3]])
	determinant3 = numpy.linalg.det([points[0],points[4],points[2],points[3]])
	determinant4 = numpy.linalg.det([points[0],points[1],points[4],points[3]])
	determinant5 = numpy.linalg.det([points[0],points[1],points[2],points[4]]) 


	# If the five determinants have the same sign, then the center of the sphere is inside of the tetrahedron.
	if numpy.sign(determinant1) == numpy.sign(determinant2) and numpy.sign(determinant1) == numpy.sign(determinant3) and numpy.sign(determinant1) == numpy.sign(determinant4) and numpy.sign(determinant1) == numpy.sign(determinant5):

		inside = inside + 1




finalcalculationpercentage = round(((inside/loops)*100),4) # Find the percentage of tetrahedrons that contain center of sphere




# Basic matplotlib graph of results (not necessary but just for fun)

possibilities = ["Tetrahedron contains center","Tetrahedron does not contain center"] # Pie chart categories
results = [inside,loops-inside] # Pie chart values

plt.pie(results)

plt.title("How Often Does the Randomly Generated Tetrahedron Contain the Center of the Sphere?")

plt.text(-1.6,-1.3,str(finalcalculationpercentage)+"%"+" of the random tetrahedrons contained the center of the sphere!")

plt.legend(possibilities)


# Results display.
print("\n"+str(finalcalculationpercentage)+"%"+" chance that the center of the sphere is inside the tetrahedron!\n")

plt.show()







	












