from django.core.management.base import BaseCommand, CommandError

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
                print(person)


def update_expert(org, github_user, expert):
    return None


def create_expert(org, github_user):
    public = org.is_public_member(github_user)

    try:
        expert = Expert.objects.get(
            contact_details__type="github",
            contact_details__value=github_user.login,
        )
        return update_expert(org, github_user, expert)
    except Expert.DoesNotExist:
        pass

    expert = Expert.objects.create(
        id=github_user.login,
        name=github_user.name if github_user.name else github_user.login,
        title="Digital Services Expert",
        photo_url=github_user.avatar_url,
    )

    expert.contact_details.add(ContactDetail.objects.create(
        who=expert,
        value=github_user.login,
        label="GitHub",
        type="github",
        preferred=True,
    ))

    if github_user.email:
        expert.contact_details.add(ContactDetail.objects.create(
            who=expert,
            value=github_user.email,
            label="Email",
            note="From GitHub",
            type="email",
            preferred=False,
        ))

    if github_user.blog:
        expert.contact_details.add(ContactDetail.objects.create(
            who=expert,
            value=github_user.blog,
            label="homepage",
            note="From GitHub",
            type="website",
            preferred=False,
        ))

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
        expert = create_expert(org, member)
        if expert is not None:
            yield expert
