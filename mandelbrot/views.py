from django.shortcuts import render, redirect
from .models import Expert, OnboardingStep, Office, Project


def home(request):
    return render(request, 'mandelbrot/home.html', {"experts": Expert.objects.all()})

def expert(request, name):
    who = Expert.objects.get(pk=name)
    return render(request, 'mandelbrot/expert.html', {"expert": who})

def project(request, id):
    who = Project.objects.get(pk=id)
    return render(request, 'mandelbrot/project.html', {"project": who})

def office(request, id):
    office = Office.objects.get(pk=id)
    return render(request, 'mandelbrot/office.html', {"office": office})

def onboard(request, name):
    who = Expert.objects.get(pk=name)
    return render(request, 'mandelbrot/onboard.html', {"expert": who})

def process(request, name, step):
    step = OnboardingStep.objects.get(pk=step)
    who = step.who

    if step.done:
        return redirect(onboard, who.id)

    if request.method == "GET":
        callable = step.step.get_callable()
        errors = callable(step)
        if errors:
            return render(request, 'mandelbrot/process.html', {
                "expert": who,
                "step": step,
                "errors": errors,
            })
        return redirect(onboard, who.id)

    step = OnboardingStep.objects.get(pk=step)
    if step.done:
        return redirect(onboard, who.id)

    return render(request, 'mandelbrot/process.html', {
        "expert": who,
        "step": step,
    })
