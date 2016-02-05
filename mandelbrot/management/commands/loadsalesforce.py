from django.core.management.base import BaseCommand, CommandError
import django.utils.text

from mandelbrot.models import Expert

import datetime as dt
import csv


def get_expert(name):
    try:
        return Expert.by_name(name=name)
    except Expert.DoesNotExist:
        whom = Expert.objects.create(
            id=django.utils.text.slugify(name),
            name=name,
            active=False,
            start_date=dt.date.today(),
            title="DSE",
        )
        return whom



class Command(BaseCommand):
    help = 'Load projects from a salesforce export'

    def add_arguments(self, parser):
        parser.add_argument(
            type=str,
            dest='csv_path',
            help='salesforce csv'
        )

    def import_expert(self, who):
        name = " ".join([
            who['Applicant Lookup: First Name'],
            who['Applicant Lookup: Last Name'],
        ])
        person = get_expert(name)
        active = {
            "Current Staff": True,
            "Inactive Staff": False,
            "Alum": False,
        }[who['Allocation Status']]
        person.active = active

        start_date = None
        for key in [
            'Applicant Lookup: Projected Start Date',
            'Applicant Lookup: Revised Start Date',
            'Actual Start Date',
        ]:
            data = who[key]
            if data != "":
                start_date = data
                break
        else:
            start_date = "01/01/2016"

        if start_date:
            person.start_date = dt.datetime.strptime(start_date, "%m/%d/%Y")

        for key, type, preferred in (
            ('Phone', 'phone', None),
            ('Mobile', 'phone', None),
            ('Email', 'email', None),
            ('Official Email', 'email', True),
        ):
            value = who['Applicant Lookup: {}'.format(key)]
            if value.strip() == "":
                continue
            detail, created = person.add_contact_detail(value=value, type=type)
            if created:
                detail.label = key
                if preferred:
                    detail.preferred = preferred
            detail.save()
        person.save()
        return person


    def handle(self, *args, csv_path, **options):
        with open(csv_path, 'r') as fd:
            for entry in csv.DictReader(fd):
                expert = self.import_expert(entry)
                print(expert)
