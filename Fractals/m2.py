# Kai

# Mandelbrot Image 2

# On my honor, I have neither given nor received unauthorised aid

# Sources:
# Colorsys: https://docs.python.org/2/library/colorsys.html

# Description: This is a zoom-in of the Mandelbrot set. For this image, my intention was to create a vibrant pattern that reflected modern art.

from PIL import Image

import colorsys

imgx = 512    # Image size

imgy = 512

xmin = 0.13180555555555568   # Define the ranges
 
xmax = 0.14541666666666668

ymin = 0.63659722222222222

ymax = 0.65020833333333332

image = Image.new("RGB",(imgx,imgy))    

iterations = 256

for x in range(imgx):

	for y in range(imgy):

		image.putpixel((x,y),(255,255,255))    # Color the entire screen

for x in range(imgx):

	for y in range(imgy): 

		complexx = x * (xmax-xmin)/(imgx-1) + xmin    # Determine the graph values relative to the pixels
		complexy = y * (ymax-ymin)/(imgy-1) + ymin

		c = complex(complexx,complexy)    # Define the C value relative to the pixels

		z = 0

		for r in range(iterations):

			z = (z*z) + c   # Mandelbrot calculation

			if abs(z) >= 2:

				red = r     # Vanilla color setup
				g = r*6
				b = 256%r 

				if r < 50:

					red, g, b = colorsys.rgb_to_hsv(red,g,b)    # Color system alteration

				elif r < 75:

					red, g, b = colorsys.rgb_to_yiq(red,g,b)

				elif r < 130:

					red, g, b = colorsys.rgb_to_hls(red,g,b)

				image.putpixel((x,y),(int(red),int(g),int(b)))

				break


image.rotate(90).save("mandelbrot2","PNG")    # Image rotation by 90 degrees

