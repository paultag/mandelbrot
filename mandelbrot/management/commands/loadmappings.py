from django.core.management.base import BaseCommand, CommandError
from mandelbrot.models import Expert, OtherName, Role, Office, Project, Agency

import datetime as dt

import csv
import os

# Role {{{

def role_importer(stream):
    for mapping in stream:
        Role.objects.get_or_create(**mapping)

# }}}

# Workplace {{{

def workplace_importer(stream):
    for mapping in stream:
        project = Project.objects.get(id=mapping['project'])
        office = Office.objects.get(id=mapping['office'])
        project.offices.add(office)
        project.save()

# }}}

# Office {{{

def office_importer(stream):
    text_fields = ['address', 'tips']
    for mapping in stream:
        for field in text_fields:
            mapping[field] = mapping[field].replace("\\n", "\n")

        try:
            office = Office.objects.get(id=mapping['id'])
        except Office.DoesNotExist:
            office = Office(id=mapping['id'])
        for k, v in mapping.items():
            setattr(office, k, v)

        office.save()

# }}}

# Sort name {{{

def sort_names(stream):
    for mapping in stream:
        expert = Expert.objects.get(id=mapping['id'])
        expert.sort_name = mapping['sort_name']

# }}}

# Name {{{

def name_importer(stream):
    def fix_mapping(mapping):
        ret = {}
        for k, v in mapping.items():
            if k.endswith("_date"):
                if v.strip() == "":
                    v = None
            if k == "presentable":
                v = True if v.lower() == "true" else False
            ret[k] = v
        return ret

    for mapping in (fix_mapping(x) for x in stream):
        uid = mapping.pop("who")
        expert = Expert.objects.get(id=uid)
        created = False

        try:
            name = expert.other_names.get(name=mapping['name'])
        except OtherName.DoesNotExist:
            name = OtherName(who=expert, **mapping)
            name.save()
            expert.other_names.add(name)
            created = True

        if not created:
            for k, v in mapping.items():
                setattr(name, k, v)
            name.save()

# }}}

# Agencies {{{

def agency_importer(stream):
    for mapping in stream:
        try:
            office = Agency.objects.get(id=mapping['id'])
        except Office.DoesNotExist:
            office = Agency(id=mapping['id'])
        for k, v in mapping.items():
            setattr(office, k, v)

        office.save()

# }}}

FLAVORS = (
    ("names.csv",      name_importer),
    ("roles.csv",      role_importer),
    ("offices.csv",    office_importer),
    ("workplaces.csv", workplace_importer),
    ("agencies.csv",   agency_importer),
    ("sort_names.csv", sort_names),
)


class Command(BaseCommand):
    help = 'Load Mappings'

    def add_arguments(self, parser):
        parser.add_argument(type=str, dest='path', help='mapping dir')

    def handle(self, *args, path, **options):
        for csv_path, function in FLAVORS:
            with open(os.path.join(path, csv_path), 'r') as fd:
                function(csv.DictReader(fd))


# vim: foldmethod=marker
