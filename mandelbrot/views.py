from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Expert, OnboardingStep, Office, Project


def home(request):
    return render(request, 'mandelbrot/home.html', {"experts": Expert.objects.all()})


# Expert views

def experts(request):
    experts = Expert.objects.filter(public=True)
    return render(request, 'mandelbrot/experts.html', {"experts": experts})

def expert(request, name):
    # Raise 404 on ! public unless logged in
    who = Expert.objects.get(pk=name)
    if request.user.is_anonymous and who.public is False:
        raise Expert.DoesNotExist("Expert matching query does not exist")

    return render(request, 'mandelbrot/expert.html', {"expert": who})

# Project views

def projects(request):
    projects = Project.objects.filter(active=True)
    return render(request, 'mandelbrot/projects.html', {"projects": projects})

def project(request, id):
    project = Project.objects.get(pk=id)
    return render(request, 'mandelbrot/project.html', {"project": project})

# Office views

def offices(request):
    offices = Office.objects.all()
    return render(request, 'mandelbrot/offices.html', {"offices": offices})

def office(request, id):
    office = Office.objects.get(pk=id)
    return render(request, 'mandelbrot/office.html', {"office": office})

# Onboarding views

@login_required
def onboarding(request, expert):
    if request.method == "POST":
        done = lambda: redirect(onboarding, expert)
        step = request.POST.get("step")
        if step is None:
            return done()

        try:
            step = OnboardingStep.objects.get(pk=step)
        except OnboardingStep.NotFound:
            return done()

        if step.step.action:
            resp = step.step.get_callable()(step)

        step.done = True
        step.save()

        return done()

    if request.method == "GET":
        who = Expert.objects.get(pk=expert)
        onboardings = OnboardingStep.objects.filter(who=who)
        return render(request, 'mandelbrot/onboarding.html', {
            "onboarding": onboardings,
            "expert": who,
        })
