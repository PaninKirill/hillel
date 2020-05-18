import random

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'generates random students'  # noqa  help is python builtins but django command requires it.

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, nargs='?', default=100,
                            help='Takes an argument to generate requested amount of Groups',
                            )  # ./src/manage.py generate_students (100) <-- optional

        parser.add_argument('--wipe', action='store_true', help='Wipe out sheet',
                            )  # ./src/manage.py generate_students --wipe

    def handle(self, *args, **options):
        if options['amount']:
            students = []
            fake = Faker()
            for _ in range(options['amount']):
                students.append(Student(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randint(18, 25),
                    grade=random.choice(Student.YEAR_IN_SCHOOL_CHOICES)[1],
                    email=fake.email(),
                    phone=fake.phone_number(),
                ))
            Student.objects.bulk_create(students)

        if options['wipe']:
            Student.objects.all().delete()
