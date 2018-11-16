from PIL import Image
import sys


i = sys.argv[1]

try:

	image = Image.open(i)

	image.load()

except:

	print("No Image Found.")


x, y = image.size


for w in range(x):

	for h in range(y):

		r,g,b = image.getpixel((w,h))

		a = (r+g+b)/3

		a = int(a)

		if a > 110:

			a = 255 

		elif a > 50:

			a = 100

		else:

			a = 0

		image.putpixel((w,h),(a,a,a))

image.save("filteredimage","PNG")



	
