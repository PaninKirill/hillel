from django.db import models


class Group(models.Model):
    faculty = models.CharField(max_length=64)
    degree_specialization = models.CharField(max_length=64)
    course = models.IntegerField()

    def info(self) -> str:
        return f'{self.id} {self.faculty} {self.degree_specialization} {self.course}'
