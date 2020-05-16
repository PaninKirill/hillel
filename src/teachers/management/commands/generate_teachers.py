import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = 'generates random teachers'  # noqa  help is python builtins but django command requires it.

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, nargs='?', default=100,
                            help='Takes an argument to generate requested amount of Students',
                            )  # ./src/manage.py generate_teachers (100) <-- optional

        parser.add_argument('--wipe', action='store_true', help='Wipe out sheet',
                            )  # ./src/manage.py generate_teachers --wipe

    def handle(self, *args, **options):
        if options['amount']:
            fake = Faker()
            teachers = []
            for _ in range(options['amount']):
                teachers.append(Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(25, 75),
                    rank=random.choice(Teacher.TEACHERS_RANK)[1],
                    email=fake.email(),
                    phone=fake.phone_number(),
                ))
            Teacher.objects.bulk_create(teachers)
        if options['wipe']:
            Teacher.objects.all().delete()
