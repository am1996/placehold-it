from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from utils import hex2rgb,fontColor
from django.views.decorators.http import etag
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.staticfiles.templatetags.staticfiles import static
import hashlib

def generate_etag(request,width,height):
	content = "placeholder: {0}x{1}".format(width,height)
	return hashlib.sha1(content.encode("utf-8")).hexdigest()

def index(request):
	return render(request,"index.html")

@etag(generate_etag)
def generate_image(request,width,height):
	if(width<=3500 or height<=3500):
		raise Http404("Page Not Found...")
	width = int(width)
	height= int(height)
	color= request.GET.get("color",False) if(request.GET.get("color",False)) else "9e9e9e"
	img =  Image.new("RGB", (width, height), hex2rgb(color))
	draw = ImageDraw.Draw(img)
	fontsize= (width*height)/((width+height)*5)
	font = ImageFont.truetype(static("fonts/calibri.ttf"), fontsize)
	text = request.GET['text'] if(request.GET.get("text",False)) \
		else "{}x{}".format(width,height)
	textWidth,textHeight = draw.textsize(text,font=font)
	if(textWidth<width and textHeight<height):
		textTop = (height - textHeight)/2
		textLeft = (width - textWidth)/2
		draw.text((textLeft,textTop),
					text,
					fill=fontColor(color),
					font=font)
	response = HttpResponse(content_type="image/PNG")
	img.save(response,"PNG")
	return response

def sendContactMail(request):
	contact = ContactForm(request.POST)
	if(contact.is_valid()):
		print(contact.cleaned_data)
		send_mail("From PlaceholdIt",
			"""
			Name:{0}
			Email:{1}
			Message: {2}
			""".format(
				request.POST.get("fullname",False),
				request.POST.get("email",False),
				request.POST.get("message",False)
			), #message
			request.POST.get("email",False),   #sender
			['mmogamer2.am@gmail.com'],
			fail_silently=False
			)
		messages.success(request, 'Message Sent Successfully.')
		return HttpResponseRedirect("/")
	else:
		errors = []
		for error in contact.errors.items():
			errors.append(error[1][0])
			print(errors)
		messages.error(request,errors[0],
			extra_tags="warning")
		return HttpResponseRedirect("/");