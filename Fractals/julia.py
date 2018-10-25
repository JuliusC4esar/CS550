# Kai
# Julia Set
# On my honor, I have neither given nor recieved unauthorised aid

# Sources:
# Colorsys: https://docs.python.org/2/library/colorsys.html

# Description: This is a zoom-in of the Julia set. My goal for this work, on an aesthetic front, was to make the set look cartoony and reflect modern art with vibrant colors and waves.


from PIL import Image

import colorsys

imgx = 512   # Image size

imgy = 512

image = Image.new("RGB",(imgx,imgy))

iterations = 500  


xmax = -0.575  # Define the ranges

xmin = -0.615

ymax = -0.1

ymin = -0.14


for x in range(imgx):

	for y in range(imgy):

		image.putpixel((x,y),(0,255,255))     # Color the entire screen




for z in range(imgx-50):    # Color the screen as a checkerboard

	for r in range(imgy-50):

		if r%50 == 0:

			for x in range(25):

				for y in range(25):

					if z%50 == 0:

						image.putpixel((x+r,y+z),(255,255,255))

						image.putpixel((x+r+25,y+z+25),(255,255,255))

for x in range(imgx):

	for y in range(imgy): 

		complexx = x * (xmax-xmin)/(imgx-1) + xmin    # Set the relative graph values to the pixel values

		complexy = y * (ymax-ymin)/(imgy-1) + ymin

		z = complex(complexx,complexy)   # Define the z value of the equation

		c = complex(-0.624,0.435)    # Define the C value of the equation

		for r in range(iterations):

			z = (z**2) + c   

			if abs(z) >= 2:

				c1 = (255-r)/(r**2+1)    # Define the vanilla colors

				c2 = r*5

				c3 = r**3

				if r > 5:

					c1, c2, c3 = colorsys.rgb_to_hsv(c1,c2,c3)   # Convert the values of the colors to a different coloring system if a specific parameter is met

				if r > 10:

					c1, c2, c3 = colorsys.rgb_to_yiq(c1,c2,c3) 

					c1 = c1/2

				image.putpixel((x,y),(int(c1),int(c2),int(c3)))

				break


image.save("julia","PNG")

