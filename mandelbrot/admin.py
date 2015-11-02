from django.contrib import admin
from mandelbrot.models import Expert, Role, Step, GithubTeam, SlackChannel, OnboardingStep

admin.site.register(Role)
admin.site.register(Step)

admin.site.register(GithubTeam)
admin.site.register(SlackChannel)

admin.site.register(OnboardingStep)


class OnboardingStepInline(admin.TabularInline):
    model = OnboardingStep


class ExpertAdmin(admin.ModelAdmin):
    model = Expert
    inlines = [OnboardingStepInline]


admin.site.register(Expert, ExpertAdmin)
