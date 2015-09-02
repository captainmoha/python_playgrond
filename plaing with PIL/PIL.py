# PIL module

import Image
import ImageFilter


def createImg():
    size = width, height = 320, 240
    # new method takes mode, size as a tuple and color
    img = Image.new('RGB', size, 'rgb(205, 100, 59)')
    img.show()


def openImg():
    file_name = '1.jpg'
    img = Image.open(file_name)
    img.show()


def blendImgs():
    size = (300, 300)
    file_name1 = '1.jpg'
    file_name2 = '2.png'

    img_1 = Image.open(file_name1).resize(size)
    img_2 = Image.open(file_name2).resize(size)
    # blend method takes 2 images and an alpha channel value
    img_blended = Image.blend(img_1, img_2, 0.4)
    img_blended.show()


def compositeImgs():
    size = (300, 300)
    file_name1 = '1.jpg'
    file_name2 = '2.png'
    # new method takes mode, size as a tuple and color
    mask = Image.new('L', size, 'green')
    img_1 = Image.open(file_name1).resize(size).convert('RGB')
    img_2 = Image.open(file_name2).resize(size).convert('RGB')
    # composite method takes 2 images and a transparency mask
    img_composited = Image.composite(img_1, img_2, mask)
    img_composited.show()


def convertImg():
    file_name = '1.jpg'
    img = Image.open(file_name)
    # convrting the image to black and white with mode 1
    # mode L would be grayscale
    bNwImg = img.convert('L')
    bNwImg.show()


def cropImg():
    file_name = '1.jpg'
    img = Image.open(file_name)
    # crop method takes a tuple of 4 elements each couple represent a point in
    # the image
    crop_area = (300, 300, 700, 700)
    cropped_img = img.crop(crop_area)
    cropped_img.show()


def filterImg():
    file_name = '1.jpg'
    img = Image.open(file_name)
    # different effects
    blured_img = img.filter(ImageFilter.BLUR)
    edge_enhanced_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    contoured_img = img.filter(ImageFilter.CONTOUR)
    embossed_img = img.filter(ImageFilter.EMBOSS)
    findEdges_img = img.filter(ImageFilter.FIND_EDGES)
    smoothed_img = img.filter(ImageFilter.SMOOTH_MORE)
    smoothed_img.show()


def imgInfo():
    file_name = '1.jpg'
    img = Image.open(file_name)

    # get size of the image with the size attribute which returns a tuple
    size = width, height = img.size
    print ("image size is: " + str(width) + ' x ' + str(height) + ' px')


def getColor():
    file_name = '1.jpg'
    img = Image.open(file_name)
    size = width, height = img.size
    # get color method takes a max color value here it's the size of the image
    print img.getcolors(width * height)
    img.show()


def getPxl():
    file_name = '1.jpg'
    img = Image.open(file_name)
    size = width, height = img.size
    # getpixel method takes a coordinate in the image and returns a tuple of
    # bands of color in that pixel
    coordinate = x, y = 180, 69
    print img.getpixel(coordinate)


def getData():
    file_name = '1.jpg'
    img = Image.open(file_name)
    size = width, height = img.size
    data_file = open('data.txt', 'w')
    data = img.getdata()
    data_file.write(str(list(data)))
    data_file.close()


def thumbnail():
    file_name = '1.jpg'
    img = Image.open(file_name)
    size = width, height = img.size
    # thumbnail takes a tuple of the size and an optional filter
    # it replaces the original image in memory
    img.thumbnail((128, 128), Image.ANTIALIAS)
    img.show()

def rotate():
	file_name = '1.jpg'
	img = Image.open(file_name)
	size = width, height = img.size
	color_to_find = (0, 0, 0);
	color_to_replace = (255, 255, 255)

	rotated_img = img.rotate(45)
	new_image_data = []

	for color in list(rotated_img.getdata()):
		if (color == color_to_find):
			new_image_data += [color_to_replace]
		else:
			new_image_data += [color]
	
	rotated_img.putdata(new_image_data)
	rotated_img.save('rotated_1.jpg')
	rotated_img.show()

def putPxl():
	file_name = '1.jpg'
	img = Image.open(file_name)
	size = width, height = img.size

	for x in range(width):
		img.putpixel((x, x), (0, 0, 0, 255))
	img.save('modified_'+ file_name)


# invokes

# createImg()
# openImg()
# blendImgs()
# compositeImgs()
# convertImg()
# cropImg()
# filterImg()
# imgInfo()
# getColor()
# getPxl()
# getData()
# thumbnail()
# rotate()
putPxl()