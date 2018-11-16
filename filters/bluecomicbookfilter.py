from PIL import Image
import numpy as np
import colorsys
import sys


i = sys.argv[1]

try:

	image = Image.open(i)

	image.load()

except:

	print("No Image Found.")


xlen,ylen = image.size

for x in range(xlen):

	for y in range(ylen):

		image.convert("RGB")

		r,g,b = image.getpixel((x,y))

		r,g,b = colorsys.rgb_to_hsv(r,g,b)

		image.convert("HSV")

		image.putpixel((x,y),(int(r),int(g),int(b)))

		if (x+1)%2 == 0 and (y+1) % 2 == 0:

			if x < xlen-1:

				image.putpixel((x,y),(0,0,0))

image.save("filteredimage","PNG")