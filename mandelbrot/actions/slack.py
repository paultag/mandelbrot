from mandelbrot.utils import invite_to_slack
from mandelbrot.models import SlackChannel


def invite(step):
    who = step.who
    channels = SlackChannel.objects.filter(roles__in=who.roles.all()).all()
    errors = []

    for team in set(channel.team for channel in channels):
        response = invite_to_slack(team, who.foiable_email)
        if not response.get('ok', False):
            errors.append(response.get('error', "INTERNAL ERROR"))

    if errors == []:
        step.done = True
        step.save()

    return errors
