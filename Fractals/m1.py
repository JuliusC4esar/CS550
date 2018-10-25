# Kai

# Mandelbrot Image 1

# On my honor, I have neither given nor received unauthorised aid

# Sources:
# Colorsys: https://docs.python.org/2/library/colorsys.html

# Description: This is a zoom-in of the Mandelbrot set. For this image, my goal was to produce an image that visually reflected a neural network. 


from PIL import Image

import colorsys

imgx = 512   # Image size

imgy = 512

xmin = -0.11481481481481    # Define ranges

xmax = -0.09351851851851

ymin = 0.913888888888888

ymax = 0.935185185185185

image = Image.new("RGB",(imgx,imgy))

iterations = 256

for x in range(imgx):

	for y in range(imgy):

		image.putpixel((x,y),(175,255,255))

for x in range(imgx):

	for y in range(imgy): 

		complexx = x * (xmax-xmin)/(imgx-1) + xmin    # Define graph values relative to pixel values
		complexy = y * (ymax-ymin)/(imgy-1) + ymin

		c = complex(complexx,complexy)   # Define c value relative to pixels

		z = 0

		for r in range(iterations):

			z = (z*z) + c   # Mandelbrot calculation

			if abs(z) >= 2:

				red = r*2   # Vanilla color setup
				g = r/2
				b = r*6 

				if r < 10:

					red, g, b = colorsys.hsv_to_rgb(red,g,b)       # Color system alteration

				elif r < 60:

					red, g, b = colorsys.rgb_to_yiq(red,g,b)

				elif r < 120:

					red, g, b = colorsys.rgb_to_hls(red,g,b)

				image.putpixel((x,y),(int(red),int(g),int(b)))

				break


image.rotate(180).save("mandelbrot1","PNG")   # Image rotation by 180 degrees

