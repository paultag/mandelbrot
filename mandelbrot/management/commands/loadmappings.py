from django.core.management.base import BaseCommand, CommandError
from mandelbrot.models import Expert, OtherName, Role

import datetime as dt

import csv
import os


def role_importer(_, stream):
    for mapping in stream:
        Role.objects.get_or_create(**mapping)

def name_importer(_, stream):
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


FLAVORS = (
    (OtherName, "names.csv", name_importer),
    (Role,      "roles.csv", role_importer),
)


class Command(BaseCommand):
    help = 'Load Mappings'

    def add_arguments(self, parser):
        parser.add_argument(type=str, dest='path', help='mapping dir')

    def handle(self, *args, path, **options):
        for model, csv_path, function in FLAVORS:
            with open(os.path.join(path, csv_path), 'r') as fd:
                function(model, csv.DictReader(fd))
