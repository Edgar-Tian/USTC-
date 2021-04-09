"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mysite import views
from mysite.dwsy import bmzlxs
from mysite.dwsy import drawimage
urlpatterns = [
    url(r'^$',views.hello),
    url(r'^dwsy/$',bmzlxs.form),
    url(r'^dwsy/bmzlxs/$',bmzlxs.handle),
    url(r'^dwsy/bmzlxsres/$',bmzlxs.result),
    path('Hello/',views.hello),
   # url(r'^image/(?P<news_id>.+)/$',drawimage.draw_image),
    url(r'^drawimage/$',drawimage.input_form),
    url(r'^drawimagehandle/$',drawimage.draw_image),
    url(r'^drawimageres/$',drawimage.result),
]
