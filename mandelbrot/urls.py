from django.conf.urls import url
import mandelbrot.views

urlpatterns = [
    url(r'^$', mandelbrot.views.home, name='home'),

    url(r'^experts/$', mandelbrot.views.ExpertsView.as_view(), name='experts'),
    url(r'^expert/(?P<id>.*)/$', mandelbrot.views.ExpertView.as_view(), name='expert'),

    url(r'^projects/$', mandelbrot.views.ProjectsView.as_view(), name='projects'),
    url(r'^project/(?P<id>.*)/$', mandelbrot.views.ProjectView.as_view(), name='project'),

    url(r'^offices/$', mandelbrot.views.OfficesView.as_view(), name='offices'),
    url(r'^office/(?P<id>.*)/$', mandelbrot.views.OfficeView.as_view(), name='office'),

    url(r'^agencies/$', mandelbrot.views.AgenciesView.as_view(), name='agencies'),
    url(r'^agency/(?P<id>.*)/$', mandelbrot.views.AgencyView.as_view(), name='agency'),
]
