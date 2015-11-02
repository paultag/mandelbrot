from django.conf.urls import include, url
from django.contrib import admin
import mandelbrot.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(mandelbrot.urls)),
]
