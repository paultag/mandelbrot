from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

import mandelbrot.urls

urlpatterns = [

    url(regex=r'^login/$', view=login, kwargs={'template_name': 'mandelbrot/login.html'}, name='login'),
    url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(mandelbrot.urls)),
]
