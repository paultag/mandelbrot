from django.db import models
import importlib


class Expert(models.Model):
    name = models.CharField(max_length=128)
    va_email = models.EmailField()
    foiable_email = models.EmailField()
    roles = models.ManyToManyField('Role', related_name="experts")
    steps = models.ManyToManyField('Step', through='OnboardingStep')

    def __str__(self):
        return "<Expert '{}'>".format(self.name)

    def onboard(self):
        if self.onboardings.count() != 0:
            return

        for step in Step.objects.filter(roles__in=self.roles.all()).all():
            step.onboard(self)
        return


class Role(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return "<Role '{}'>".format(self.name)


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
