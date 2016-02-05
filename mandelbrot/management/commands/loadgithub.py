from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from mandelbrot.models import Expert, ContactDetail
from github3 import login

import os


KEY = os.environ['GITHUB_ACCESS_TOKEN']
USER = os.environ['GITHUB_USER_NAME']



class Command(BaseCommand):
    help = 'Load experts from GitHub'
    CACHE = {}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for org, team in (
            ('department-of-veterans-affairs', 'Digital Service at VA'),
            ('usds', 'USDS'),
        ):
            for person in scrape(org, team):
                # print(person)
                pass


def find(github_user):
    expert_name = name(github_user)

    try:
        return Expert.by_name(expert_name)
    except Expert.DoesNotExist:
        pass

    expert = Expert.objects.filter(
        contact_details__type="github",
        contact_details__value=github_user.login
    ).distinct()

    if len(expert) == 0:
        raise Expert.DoesNotExist(expert_name)
    if len(expert) != 1:
        raise Expert.MultipleObjectsReturned(expert_name)
    expert, = expert
    return expert


def name(github_user):
    return github_user.name if github_user.name else github_user.login


def scrape_expert(org, github_user):
    public = org.is_public_member(github_user)
    expert_name = name(github_user)

    try:
        expert = find(github_user)
    except Expert.DoesNotExist:
        print(",{},GitHub Name,,,False".format(expert_name))
        return None
    except Expert.MultipleObjectsReturned:
        print("Ambigious name: {}".format(expert_name))
        return None

    for type, value, preferred in (
        ("github", github_user.login, True),
        ("website", github_user.blog, True),
        ("email", github_user.email, False),

    ):
        if value is None:
            continue

        detail, created = expert.add_contact_detail(
            value=value,
            label=None,
            type=type,
            preferred=preferred,
        )
        if created:
            detail.label = "From GitHub"
            detail.save()

    if expert.photo_url == "":
        expert.photo_url = github_user.avatar_url

    expert.save()
    return expert


def scrape(org_name, team_name):
    github = login(USER, password=KEY)
    org = github.organization(org_name)
    for team in org.iter_teams():
        if team.name == team_name:
            break
    else:
        raise KeyError("No such team found: {} {}".format(
            org_name, team_name,
        ))

    for member in team.iter_members():
        member.refresh()
        d = scrape_expert(org, member)
        if d is not None:
            yield d
