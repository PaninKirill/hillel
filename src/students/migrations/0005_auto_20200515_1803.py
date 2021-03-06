# Generated by Django 2.2 on 2020-05-15 18:03

from django.db import migrations


def forwards(apps, schema):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().only('first_name', 'last_name', 'phone').iterator():
        student.phone = ''.join(i for i in student.phone if i.isdigit())
        student.first_name = student.first_name.capitalize()
        student.last_name = student.last_name.capitalize()
        student.save(update_fields=['first_name', 'last_name', 'phone'])


def backwards(apps, schema):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0004_student_phone'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
