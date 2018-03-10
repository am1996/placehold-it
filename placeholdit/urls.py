from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^contact',views.sendContactMail,name="contact"),
    url(r'^(?P<width>[0-9]{1,4})x(?P<height>[0-9]{1,4})',
    	views.generate_image)
] + static(settings.STATIC_URL, 
	document_root=settings.STATIC_ROOT)
