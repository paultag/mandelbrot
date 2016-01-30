from django.contrib import admin
from mandelbrot.models import (
    Agency,
    Expert,
    Role,
    Interest,
    Office,
    ContactDetail,
    Project,
    ProjectMember,
    Badge,
    BadgeAward,
)

admin.site.register(Role)
admin.site.register(Interest)

admin.site.register(Agency)
admin.site.register(Office)
admin.site.register(ContactDetail)

admin.site.register(Project)
admin.site.register(ProjectMember)


admin.site.register(Badge)
admin.site.register(BadgeAward)


class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMember


class BadgeAwardInline(admin.TabularInline):
    model = BadgeAward
    fk_name = "who"


class ContactDetailInline(admin.TabularInline):
    model = ContactDetail


class ExpertAdmin(admin.ModelAdmin):
    model = Expert
    inlines = [ProjectMembershipInline, ContactDetailInline, BadgeAwardInline,]


admin.site.register(Expert, ExpertAdmin)
