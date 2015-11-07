from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'mandelbrot.views.home'),


    # url(r'^experts/$', 'mandelbrot.views.experts', name='experts'),
    url(r'^expert/(?P<name>.*)/$', 'mandelbrot.views.expert', name='expert'),

    # url(r'^projects/$', 'mandelbrot.views.projects', name='projects'),
    url(r'^project/(?P<id>.*)/$', 'mandelbrot.views.project', name='project'),

    url(r'^office/(?P<id>.*)/$', 'mandelbrot.views.office', name='office'),
]
