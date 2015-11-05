from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'mandelbrot.views.home'),

    url(r'^expert/(?P<name>.*)/$', 'mandelbrot.views.expert', name='expert'),
    url(r'^office/(?P<id>.*)/$', 'mandelbrot.views.office', name='office'),

    # url(r'^onboard/(?P<name>.*)/(?P<step>.*)/$', 'mandelbrot.views.process'),
    # url(r'^onboard/(?P<name>.*)/$', 'mandelbrot.views.onboard'),
]
