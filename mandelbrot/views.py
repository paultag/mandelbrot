from django.shortcuts import render, redirect
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
