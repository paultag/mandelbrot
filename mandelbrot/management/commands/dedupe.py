from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from mandelbrot.models import ContactDetail, Expert


class Command(BaseCommand):
    help = 'Load experts from GitHub'
    CACHE = {}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for (old, new) in dedupe():
            print("Deleting old detail {}, new detail: {}".format(old, new))


def dedupe_phones(expert):
    seen = {}
    numbers = [str(x) for x in range(0,9)]

    for phone in expert.contact_details.filter(type='phone'):
        value = "".join(filter(lambda x: x in numbers, phone.value))
        if len(value) > 10:
            if len(value) % 10 == 0:
                values = [value[x:x+10] for x in range(0, len(value), 10)]
            else:
                print("Warning: {} is bad. Bad {}, bad!".format(
                    phone.value,
                    phone.who.name,
                ))
                continue
        else:
            values = [value]

        for value in values:
            if value in seen:
                yield (phone, seen[value])
                phone.delete()
            seen[value] = phone


def dedupe():
    for expert in Expert.objects.all():
        yield from dedupe_phones(expert)
