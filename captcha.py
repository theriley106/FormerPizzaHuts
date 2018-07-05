from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
TEMPLATE_IMAGE = "captchatemplate.png"
TILE_WIDTH = 120
TILE_HEIGHT = 120
START_X = 7
START_Y = 156
TEXT_START_X = 32
TEXT_START_Y = 36
TEXT_SIZE_X = 380
TEXT_SIZE_Y = 35
CAPTCHA_IMAGE_HEIGHT = TILE_HEIGHT * 4
CAPTCHA_IMAGE_WIDTH = TILE_WIDTH * 4
QUESTION_TEXT = "Select all squares with restaurants."
FONT_FILE = "Univers-Bold.otf"
# Contains the font file used in the image
#120x119+7+157
def generateCaptcha(daysList, imageCount=1, saveAs="test.png"):
	# Create 1 square per image
	im = Image.open(TEMPLATE_IMAGE).convert('RGB')
	t_width, t_height = im.size
	rect = Image.new("RGB", (TEXT_SIZE_X, TEXT_SIZE_Y), (77, 144, 226))
	im.paste(rect, (TEXT_START_X, TEXT_START_Y))
	# This clear out the previous text from the "Template" image
	draw = ImageDraw.Draw(im,'RGBA')
	# Allows you to "draw" text on the image
	font = ImageFont.truetype(FONT_FILE, 25)
	# Sets font to arial / whatever font you want to use
	draw.text((TEXT_START_X, TEXT_START_Y), QUESTION_TEXT, (255, 255, 255, 0), font=font)
	# "Draws" the text onto the template
	im2 = resizeImage("20.jpg")
	currentX = START_X
	currentY = START_Y
	for i in range(4):
		for e in range(4):
			im.paste(im2, (currentX, currentY))
			currentX += 121
		currentX = 7
		currentY += 121
	im.save(saveAs, "PNG")

def createSingleImageCaptcha(imageFile, heightVal=4, widthVal=4):
	captchaTemplate = Image.open(TEMPLATE_IMAGE).convert('RGB')
	rect = Image.new("RGB", (TEXT_SIZE_X, TEXT_SIZE_Y), (77, 144, 226))
	captchaTemplate.paste(rect, (TEXT_START_X, TEXT_START_Y))
	# This clear out the previous text from the "Template" image
	draw = ImageDraw.Draw(captchaTemplate,'RGBA')
	# Allows you to "draw" text on the image
	font = ImageFont.truetype(FONT_FILE, 25)
	# Sets font to arial / whatever font you want to use
	draw.text((TEXT_START_X, TEXT_START_Y), QUESTION_TEXT, (255, 255, 255, 0), font=font)
	# "Draws" the text onto the template
	im = resizeImage(imageFile, (CAPTCHA_IMAGE_WIDTH, CAPTCHA_IMAGE_HEIGHT))
	til = Image.new(mode='RGBA',size=(1000,1000),color=(255,255,255,0))
	toCrop = []
	currentX = 0
	currentY = 0
	for i in range(heightVal):
		for e in range(widthVal):
			area = (currentX, currentY, currentX+TILE_WIDTH, currentY+TILE_HEIGHT)
			toCrop.append(area)
			currentX += TILE_WIDTH
		currentY += TILE_HEIGHT
		currentX = 0
	currentX = START_X
	currentY = START_Y
	f = 0
	for i in range(4):
		for e in range(4):
			im2 = im.crop(toCrop[f])
			captchaTemplate.paste(im2, (currentX, currentY))
			#print currentY
			currentX += 121
			f += 1
		currentX = 7
		currentY += 121
	captchaTemplate.save('test2.png')


def resizeImage(imageFile, size=(TILE_WIDTH, TILE_HEIGHT)):
	im = Image.open(imageFile)
	im.thumbnail(size, Image.ANTIALIAS)
	return im



if __name__ == '__main__':
	#resizeImage("20.jpg")
	#generateTweet("")
	createSingleImageCaptcha("50.jpg")

