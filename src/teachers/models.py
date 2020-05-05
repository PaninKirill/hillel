import random

from django.db import models

from faker import Faker


class Teacher(models.Model):
    PROFESSOR = 'PR'
    ASSOCIATE_PROFESSOR = 'AEP'
    ASSISTANT_PROFESSOR = 'ASP'
    MASTER_INSTRUCTOR = 'MI'
    SENIOR_INSTRUCTOR = 'SI'
    INSTRUCTOR = 'IR'
    RESEARCH_ASSOCIATE = 'RA'
    LECTURER = 'LR'

    TEACHERS_RANK = [
        (PROFESSOR, 'Professor'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (ASSISTANT_PROFESSOR, 'Assistant Professor'),
        (MASTER_INSTRUCTOR, 'Master Instructor'),
        (SENIOR_INSTRUCTOR, 'Senior Instructor'),
        (INSTRUCTOR, 'Instructor'),
        (RESEARCH_ASSOCIATE, 'Research Associate'),
        (LECTURER, 'Lecturer'),
    ]
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    rank = models.CharField(max_length=3, choices=TEACHERS_RANK, default='LR')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.rank}'

    def __str__(self):
        return f'{self.id}, {self.full_name}'

    def __repr__(self):
        return f'{self.id}, {self.full_name}, {self.rank}'

    @classmethod
    def add_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 25),
            rank=random.choice(Teacher.TEACHERS_RANK)[0]
        )
        teacher.save()
        return teacher
