from django.core.management.base import BaseCommand, CommandError
from mandelbrot.models import Expert

import os


BLACKLIST = {"README"}


class Command(BaseCommand):
    help = 'Load Mappings'

    def add_arguments(self, parser):
        parser.add_argument(type=str, dest='path', help='mapping dir')

    def handle(self, *args, path, **options):
        for dirpath, dirnames, filenames in os.walk(top=path):
            for name in filenames:
                if not name.endswith(".md"):
                    continue

                expert = name[:-3]
                if expert in BLACKLIST:
                    continue

                expert = Expert.objects.get(id=name[:-3])
                with open(os.path.join(dirpath, name), 'r') as fd:
                    expert.bio = fd.read()
                    print("Updated {}".format(expert.id))
                expert.save()


# vim: foldmethod=marker
