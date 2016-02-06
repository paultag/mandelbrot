from django.conf.urls import url
import mandelbrot.api.views

urlpatterns = [
    url(r'^expert/(?P<id>.*)/$', mandelbrot.api.views.ExpertView.as_view()),
    url(r'^experts/$', mandelbrot.api.views.ExpertsView.as_view()),

    url(r'^project/(?P<id>.*)/$', mandelbrot.api.views.ProjectView.as_view()),
    url(r'^projects/$', mandelbrot.api.views.ProjectsView.as_view()),
]
