import math
from django.http import Http404
def hex2rgb(value):
	try:
		if(len(value)==3 ):
			value = value+value
			lv = len(value)
			return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))
		elif(len(value)==6):
			lv = len(value)
			return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))
		else:
			raise Http404("Page Not Found...")
	except(Exception):
		raise Http404("Page Not Found...")


def getBrightness(color):
	color = hex2rgb(color)
	red = color[0]
	green = color[1]
	blue = color[2]
	brightness=math.sqrt(
		(0.241*red*red)+
		(0.691*green*green)+
		(0.068*blue*blue)
		)
	return brightness/255*100

def fontColor(color):
	if(getBrightness(color)<50):
		return hex2rgb("ffffff")
	else:
		return hex2rgb("000000")


