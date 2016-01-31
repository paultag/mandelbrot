from django.db.models import Q
from django.db import models
import datetime as dt
import importlib


class Expert(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    photo_url = models.URLField(blank=True)
    title = models.CharField(max_length=128)
    interests = models.ManyToManyField('Interest', related_name="experts", blank=True)
    buddy = models.ForeignKey('Expert', related_name="buddies", blank=True, null=True)
    projects = models.ManyToManyField('Project', through='ProjectMember')
    bio = models.TextField(blank=True)
    public = models.BooleanField()

    def __str__(self):
        return "<Expert '{}'>".format(self.name)

    def get_preferred_public_contact_details(self):
        return self.contact_details.filter(preferred=True, public=True)

    def get_active_agencies(self):
        return Agency.objects.filter(
            projects__memberships__who=self,
            projects__memberships__end_date=None,
            projects__active=True,
        ).distinct()

    def get_active_memberships(self):
        return self.memberships.filter(
            end_date=None,
            project__active=True,
        ).order_by('start_date')

    def get_inactive_memberships(self):
        return self.memberships.filter(
            Q(end_date__isnull=False) | Q(project__active=False),
        ).order_by('end_date')


CONTACT_TYPES = [
    ("email", "E-Mail"),
    ("phone", "Phone"),
    ("fax", "Fax"),
    ("twitter", "Twitter"),
    ("github", "GitHub"),
    ("yo", "Yo"),
    ("slack", "Slack"),
    ("website", "Cyber Website"),
]


class ContactDetail(models.Model):
    who = models.ForeignKey('Expert', related_name="contact_details")
    type = models.CharField(max_length=128, choices=CONTACT_TYPES)
    label = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    note = models.CharField(max_length=128, blank=True)
    preferred = models.BooleanField()
    public = models.BooleanField()

    def __str__(self):
        return "<ContactDetail who='{}' type='{}' value='{}'>".format(
            self.who.name, self.type, self.value
        )


class Office(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    address = models.TextField()
    tips = models.TextField(blank=True)

    def __str__(self):
        return "<Office: {}>".format(self.name)


class Role(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return "<Role '{}'>".format(self.name)


class Interest(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "<Interest '{}'>".format(self.name)


class Badge(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=128)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return "<Badge '{}' ({})>".format(self.id, self.title)


class BadgeAward(models.Model):
    who = models.ForeignKey('Expert', related_name="badges")
    badge = models.ForeignKey('Badge', related_name="recipiants")
    awarded_by = models.ForeignKey('Expert', related_name="badges_given")
    awarded_on = models.DateField()

    def __str__(self):
        return "<BadgeAward '{}' given to {} by {}>".format(
            self.badge.id,
            self.who.id,
            self.awarded_by.id,
        )


class Agency(models.Model):
    class Meta:
        verbose_name = "agency"
        verbose_name_plural = "agencies"

    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return "<Agency '{}'>".format(self.name)

    def get_active_projects(self):
        return self.projects.filter(active=True)

    def get_inactive_projects(self):
        return self.projects.filter(active=False)

    def get_active_memberships(self):
        return ProjectMember.objects.filter(
            project__agencies=self,
            project__active=True,
            end_date=None
        )

    def get_active_experts(self):
        return Expert.objects.filter(
            memberships__project__agencies=self,
            memberships__project__active=True,
            memberships__end_date=None
        ).distinct()


class Project(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    mission = models.TextField()
    description = models.TextField()
    active = models.BooleanField()
    experts = models.ManyToManyField('Expert', through='ProjectMember')
    offices = models.ManyToManyField('Office', related_name="projects", blank=True)
    agencies = models.ManyToManyField('Agency', related_name="projects")

    def __str__(self):
        return "<Project '{}'>".format(self.name)

    def get_active_memberships(self):
        return self.memberships.filter(end_date=None).order_by('start_date')

    def get_inactive_memberships(self):
        return self.memberships.filter(
            end_date__isnull=False
        ).order_by('end_date')


class ProjectMember(models.Model):
    who = models.ForeignKey('Expert', related_name="memberships")
    project = models.ForeignKey('Project', related_name="memberships")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    roles = models.ManyToManyField('Role')
    part_time = models.BooleanField()

    def get_duration(self):
        if self.end_date:
            return self.end_date - self.start_date
        return dt.date.today() - self.start_date

    def __str__(self):
        return "<ProjectMember '{}' in '{}'>".format(
            self.who.name,
            self.project.name,
        )
