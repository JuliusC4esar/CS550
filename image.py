from PIL import Image


imgx = 512

imgy = 512


image = Image.new("RGB",(imgx,imgy))


for x in range(imgx):

	for y in range(imgy):

		image.putpixel((x,y),((x*3%255),0,0))

image.save("demo_image.png","PNG") 