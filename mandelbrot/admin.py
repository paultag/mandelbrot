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
    OtherName,
)

admin.site.register(Role)
admin.site.register(Interest)

admin.site.register(Agency)
admin.site.register(Office)
admin.site.register(ContactDetail)

admin.site.register(ProjectMember)

admin.site.register(Badge)
admin.site.register(BadgeAward)

admin.site.register(OtherName)


class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMember


class OtherNameInline(admin.TabularInline):
    model = OtherName


class BadgeAwardInline(admin.TabularInline):
    model = BadgeAward
    fk_name = "who"


class ContactDetailInline(admin.TabularInline):
    model = ContactDetail


class ExpertAdmin(admin.ModelAdmin):
    model = Expert
    inlines = [ProjectMembershipInline, ContactDetailInline,
               BadgeAwardInline, OtherNameInline]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ProjectMembershipInline]


admin.site.register(Expert, ExpertAdmin)
admin.site.register(Project, ProjectAdmin)
