import random

from django.core.management.base import BaseCommand

from groups.models import Group


class Command(BaseCommand):
    help = 'generates random groups'  # noqa  help is python builtins but django command requires it.

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, nargs='?', default=100,
                            help='Takes an argument to generate requested amount of Groups',
                            )  # ./src/manage.py generate_groups (100) <-- optional

        parser.add_argument('--wipe', action='store_true', help='Wipe out sheet',
                            )  # ./src/manage.py generate_groups --wipe

    def handle(self, *args, **options):
        if options['amount']:
            for _ in range(options['amount']):
                set_faculty = random.choice(list(Group.FACULTY_N_SPECIALIZATION.keys()))
                set_degree_specialization = random.choice(Group.FACULTY_N_SPECIALIZATION.get(set_faculty))
                Group.objects.create(
                    faculty=set_faculty,
                    degree_specialization=set_degree_specialization,
                    course=random.randint(1, 5),
                )
        if options['wipe']:
            Group.objects.all().delete()
