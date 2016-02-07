from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from mandelbrot.models import Expert, ContactDetail
import requests

import os


KEY = os.environ['SLACK_ACCESS_TOKEN']



class Command(BaseCommand):
    help = 'Load experts from GitHub'
    CACHE = {}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for person in scrape():
            pass


def scrape():
    team = requests.get(
        'https://slack.com/api/users.list?token={}'.format(KEY),
    ).json()['members']

    for person in team:
        if person.get('deleted', False):
            continue
        if person.get('is_bot', False):
            continue

        name = person.get('real_name', person.get('name'))
        if name == "":
            continue

        try:
            who = Expert.by_name(name)
        except Expert.DoesNotExist:
            print(",{},Slack Name,,,False".format(name))
            continue

        if who.photo_url == "":
            who.photo_url = person.get('image_1024')

        detail, created = who.add_contact_detail(
            value=person['name'],
            label=None,
            type='slack',
            preferred=True,
        )
        if created:
            detail.label = "From Slack"
            detail.save()


        if False:
            yield
