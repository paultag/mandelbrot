from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Expert, Office, Project, Agency


def home(request):
    return render(request, 'mandelbrot/home.html', {"experts": Expert.objects.all()})

# Class-based view utility classes {{{

class MandelbrotView(View):
    model = None
    name = None

    def params(self, *args, **kwargs):
        raise NotImplementedError()

    def authorized(self, *args, **kwargs):
        return True

    def get(self, request, *args, **kwargs):
        if self.name is None:
            raise NotImplementedError("You forgot `name` on your view")

        # flavors = request.META['HTTP_ACCEPT'].split(",")
        # encoding = "text/html"
        # if len(flavors) > 0:
        #     encoding = flavors[0]

        data = self.lookup(request, *args, **kwargs)
        if not self.authorized(data, request, *args, **kwargs):
            raise self.model.DoesNotExist()

        # if encoding == "application/json":
        #     return self.json(request, data)

        return render(request, self.template, {self.name: data})


class BoringObjectView(MandelbrotView):
    def lookup(self, request, id):
        return self.model.objects.get(pk=id)


class BoringObjectsView(MandelbrotView):
    model = None
    def lookup(self, request):
        return self.model.objects.all()

# }}}

# Model Views {{{

# Expert views {{{

class ExpertsView(BoringObjectsView):
    name = "experts"
    template = "mandelbrot/experts.html"
    model = Expert

    def lookup(self, request):
        return Expert.get_active()


class ExpertView(BoringObjectView):
    name = "expert"
    template = "mandelbrot/expert.html"
    model = Expert

# }}}

# Project views {{{

class ProjectsView(BoringObjectsView):
    name = "projects"
    template = "mandelbrot/projects.html"
    model = Project

    def lookup(self, request):
        return Project.objects.filter(active=True)

class ProjectView(BoringObjectView):
    name = 'project'
    model = Project
    template = "mandelbrot/project.html"

# }}}

# Office views {{{

class OfficesView(BoringObjectsView):
    name = "offices"
    template = "mandelbrot/offices.html"
    model = Office

class OfficeView(BoringObjectView):
    name = "office"
    template = "mandelbrot/office.html"
    model = Office

# }}}

# Agency views {{{

class AgenciesView(BoringObjectsView):
    name = "agencies"
    template = "mandelbrot/agencies.html"
    model = Agency

class AgencyView(BoringObjectView):
    name = "agency"
    template = "mandelbrot/agency.html"
    model = Agency

# }}}

# }}}


# vim: foldmethod=marker
