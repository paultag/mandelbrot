from django.contrib import admin
from mandelbrot.models import Expert, Role, Step, GithubTeam, SlackChannel, OnboardingStep

admin.site.register(Expert)
admin.site.register(Role)
admin.site.register(Step)

admin.site.register(GithubTeam)
admin.site.register(SlackChannel)

admin.site.register(OnboardingStep)
