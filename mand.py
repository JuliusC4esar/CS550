# Kai
# Mandelbrot Set Working Attempt

from PIL import Image

imgx = 512

imgy = 512

image = Image.new("RGB",(imgx,imgy))

iterations = 256

for x in range(imgx):

	for y in range(imgy): 

		complexx = -2+(x*(4/imgx))

		complexy = -2+(y*(4/imgy))

		c = complex(complexx,complexy)

		z = 0

		for r in range(iterations):

			z = (z*z) + c

			if abs(z) >= 2:

				image.putpixel((x,y),(255,0,0))

				break


image.save("mandelbrot","PNG")

