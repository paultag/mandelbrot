from django.db.models import Q
from django.db import models
import importlib


class Expert(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    photo_url = models.URLField(blank=True)
    title = models.CharField(max_length=128)
    email = models.EmailField()
    roles = models.ManyToManyField('Role', related_name="experts")
    steps = models.ManyToManyField('Step', through='OnboardingStep')
    buddy = models.ForeignKey('Expert', related_name="buddies", blank=True, null=True)
    projects = models.ManyToManyField('Project', through='ProjectMember')
    bio = models.TextField(blank=True)
    public = models.BooleanField()

    def __str__(self):
        return "<Expert '{}'>".format(self.name)

    def get_active_memberships(self):
        return self.memberships.filter(end_date=None, project__active=True)

    def get_inactive_memberships(self):
        return self.memberships.filter(
            Q(end_date__isnull=False) | Q(project__active=False))

    def onboard(self):
        if self.onboardings.count() != 0:
            return

        for step in Step.objects.filter(roles__in=self.roles.all()).all():
            step.onboard(self)
        return


CONTACT_TYPES = [
    ("email", "E-Mail"),
    ("phone", "Phone"),
    ("fax", "Fax"),
    ("twitter", "Twitter"),
]


class ContactDetail(models.Model):
    who = models.ForeignKey('Expert', related_name="contact_details")
    type = models.CharField(max_length=128, choices=CONTACT_TYPES)
    label = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    note = models.CharField(max_length=128, blank=True)

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

    def __str__(self):
        return "<Office: {}>".format(self.name)


class Role(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return "<Role '{}'>".format(self.name)


class Badge(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=128)

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


class Project(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    mission = models.TextField()
    active = models.BooleanField()
    experts = models.ManyToManyField('Expert', through='ProjectMember')
    offices = models.ManyToManyField('Office', related_name="projects", blank=True)

    def __str__(self):
        return "<Project '{}'>".format(self.name)

    def get_active_memberships(self):
        return self.memberships.filter(end_date=None)

    def get_inactive_memberships(self):
        return self.memberships.filter(end_date__isnull=False)


class ProjectMember(models.Model):
    who = models.ForeignKey('Expert', related_name="memberships")
    project = models.ForeignKey('Project', related_name="memberships")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "<ProjectMember '{}' in '{}'>".format(
            self.who.name,
            self.project.name,
        )


class OnboardingStep(models.Model):
    who = models.ForeignKey('Expert', related_name="onboardings")
    step = models.ForeignKey('Step', related_name="onboardings")
    done = models.BooleanField()

    def __str__(self):
        return "<OnboardingStep: '{}' '{}' ({})>".format(
            self.step.description, self.who.name, self.done
        )


class Step(models.Model):
    description = models.CharField(max_length=256)
    action = models.CharField(max_length=256, blank=True)  # Python importable name
    roles = models.ManyToManyField('Role', related_name="steps")

    def __str__(self):
        return "<Step: '{}'>".format(self.description)

    def get_callable(self):
        module, callable = self.action.rsplit(".", 1)
        module = importlib.import_module(module)
        return getattr(module, callable)

    def onboard(self, expert):
        return OnboardingStep.objects.create(who=expert, step=self, done=False)


class GithubTeam(models.Model):
    org = models.CharField(max_length=128)
    team = models.CharField(max_length=128)
    roles = models.ManyToManyField('Role', related_name="githubs")

    def __str__(self):
        return "<GithubTeam: '{}/{}'>".format(self.org, self.team)


class SlackChannel(models.Model):
    team = models.CharField(max_length=128)
    channel = models.CharField(max_length=128)
    roles = models.ManyToManyField('Role', related_name="slacks")

    def __str__(self):
        return "<SlackChannel: '{}/{}'>".format(self.team, self.channel)
