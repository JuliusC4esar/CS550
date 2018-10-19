# Kai
# Mandelbrot Set First Attempt

from PIL import Image

import math

image = Image.new("RGB",(512,512))

for x in range(-2,3):

	for y in range(-2,3):

		c = complex(x,y) # changing C value

		z = 0 # Define Z at 0

		for r in range(3):  # 3 iterations

			z = (z*z) + c # Mandelbrot calculation

			if abs(z) >= 2:    # If it breaks off, color the pixel a certain shade of red depending on number of iterations

				image.putpixel((x+200,y+200),(255/(r+1),0,0))

				break

image.save("mandelbrot","PNG")