import random

from django.db import models

from faker import Faker


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    grade = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()  # models.IntegerField
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=24, default='')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.grade}'

    def inc_age(self) -> None:
        self.age += 1
        self.save()

    def __str__(self):
        return f'{self.id}, {self.full_name}'

    def __repr__(self):
        return f'{self.id}, {self.full_name}, {self.grade}'

    @classmethod
    def add_student(cls):
        fake = Faker()
        student = cls.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 25),
            grade=random.choice(Student.YEAR_IN_SCHOOL_CHOICES)[1],
            email=fake.email(),
            phone=fake.phone_number(),
        )
        return student

    def save(self, *args, **kwargs):
        check_existence = Student.objects.all().only('email').filter(
            email__iexact=self.email
        ).exclude(
            email__iexact=self.email
        )
        if len(check_existence) != 0:
            raise Exception(f'{self.email} already exists')
        else:
            super().save(*args, **kwargs)


class Logger(models.Model):
    method = models.CharField(max_length=128)
    path = models.CharField(max_length=128)
    execution_time = models.DecimalField(max_digits=4, decimal_places=4)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method}, {self.path}, {self.execution_time}, {self.created}'

    @staticmethod
    def _check_log():
        with open('middleware.log', 'a') as file:
            logger_queryset = Logger.objects.all()
            for log_data in logger_queryset:
                file.write(
                    f' {log_data.id},'
                    f' {log_data.method},'
                    f' {log_data.path},'
                    f' {log_data.execution_time},'
                    f' {log_data.created},'
                    f' \n')
