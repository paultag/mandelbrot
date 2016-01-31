from django.core.management.base import BaseCommand, CommandError
import django.utils.text
from mandelbrot.models import Project, ProjectMember, Agency

import os
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
            sections = priorities.parse_document(fd.read())

        for project in scrape(sections):
            print(project)


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

            project = Project(
                id=django.utils.text.slugify(title),
                name=title,
                active=active,
            )
            project.save()

            for agency in agencies:
                agency.save()
                project.agencies.add(agency)

            yield project
