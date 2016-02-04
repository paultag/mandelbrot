from django.core.management.base import BaseCommand, CommandError
import django.utils.text
from mandelbrot.models import Project, ProjectMember, Agency, Expert, Role

import os
import datetime as dt
import importlib.machinery

loader = importlib.machinery.SourceFileLoader(
    'priorities',
    '../usds/scripts/priorities_lint.py'
)
priorities = loader.load_module()
priorities_md = '../usds/administration/priorities.md'


class Command(BaseCommand):
    help = 'Load projects from priorities.md'
    CACHE = {}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(priorities_md, 'r') as fd:
            (sections, _) = priorities.parse_document(fd.read())

        for project in scrape(sections):
            print(project)


def role(name):
    # name = name.title()
    a, _ = Role.objects.get_or_create(name=name)
    return a


def agency(id):
    id = id.upper()
    a, _ = Agency.objects.get_or_create(id=id)
    if a.name == '':
        a.name = {
            'VA': 'Veterans Affairs',
            'DHS': "Homeland Security",
            'DOD': "Defense",
            "DOJ": "Justice",
            "DOS": "State",
            "ED": "Education",
            'HHS': "Health and Human Services",
            "IRS": "Internal Revenue Service",
            "HQ": "Office of the President",
            "EOP": "Office of the President",
            "SBA": "Small Business Administration",
            "SSA": "Social Security Administration",
            "DOC": "Commerce",
            "OPM": "Office of Personnel Management",
            "DOT": "Transportation",
            "USTR": "United States Trade Representative",
            "DOI": "Interior",
        }.get(id, id)
    if a.photo_url == '':
        a.photo_url = 'http://placehold.it/600/f8f8f8?=hi'
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

            if 'VA' not in [x.id for x in agencies]:
                continue

            db_project = Project(
                id=django.utils.text.slugify(title),
                name=title,
                active=active,
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

                # print("Name", employee.name)
                # print("Empl", employee.employer)
                roles = [role(x) for x in employee.role.split("/")]
                part_time = employee.quantity == 1.0

                expert = None
                try:
                    expert = Expert.objects.get(name=employee.name)
                except Expert.DoesNotExist:
                    print("No such person: {}".format(employee.name))

                if expert:
                    membership = expert.memberships.filter(
                        project=db_project,
                        end_date__isnull=True,
                    )
                    if len(membership) == 0:
                        m = ProjectMember(
                            project=db_project,
                            who=expert,
                            start_date=dt.date.today(),
                            part_time=part_time,
                        )
                        m.save()
                        for r in roles:
                            m.roles.add(r)
                        m.save()

                        print(m)

            yield db_project
