from django.core.management.base import BaseCommand, CommandError
import django.utils.text
from mandelbrot.models import Project, ProjectMember, Agency, Expert, Role

import os
import sys
import datetime as dt
import importlib.machinery

sys.path.append('../usds/scripts/priorities-lint/')
from priorities_lint.parser import parse_document

priorities_md = '../usds/administration/priorities.md'


class Command(BaseCommand):
    help = 'Load projects from priorities.md'
    CACHE = {}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(priorities_md, 'r') as fd:
            (sections, _) = parse_document(fd.read())

        for project in scrape(sections):
            pass


def role(name):
    try:
        return Role.objects.get(name=name)
    except Role.DoesNotExist:
        print("Unknown Role: {},".format(name))
        return None


def agency(id):
    id = id.upper()
    a, _ = Agency.objects.get_or_create(id=id)
    if a.photo_url == '':
        a.photo_url = '/static/img/seals/{}.png'.format(id.lower())
    return a


def project_details(project):
    agencies, title = (x.strip() for x in project.title.split(":", 1))
    agencies = agencies.split("/")
    return [agency(x) for x in agencies], title

def scrape(sections):
    for section in sections:
        active = False
        if section.title == "Projects open for staffing":
            active = True

        for project in section.projects:
            agencies, title = project_details(project)

            db_project = Project(
                id=django.utils.text.slugify(title),
                name=title,
                active=active,
                mission=project.mission,
            )
            db_project.save()

            for agency in agencies:
                agency.save()
                db_project.agencies.add(agency)

            for employee in project.team:
                if employee.employer == "18F":
                    continue
                if "open" in employee.name.lower():
                    continue

                roles = [role(x) for x in employee.role.split("/")]
                roles = [x for x in roles if x is not None]
                part_time = employee.quantity != 1.0

                if roles == []:
                    continue

                expert = None
                try:
                    expert = Expert.by_name(employee.name)
                except Expert.DoesNotExist:
                    print(",{},priorities.md,,,False".format(employee.name))
                    continue

                membership = expert.memberships.filter(
                    project=db_project,
                    end_date__isnull=True,
                )
                if len(membership) == 0:
                    m = ProjectMember(
                        project=db_project,
                        who=expert,
                        start_date=expert.start_date,
                        part_time=part_time,
                    )
                    m.save()
                    for r in roles:
                        m.roles.add(r)
                    m.save()

            yield db_project
