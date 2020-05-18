# Generated by Django 2.2 on 2020-05-16 01:54

from django.db import migrations


def forwards(apps, schema):
    Teacher = apps.get_model('teachers', 'Teacher')
    for teacher in Teacher.objects.all().only('first_name', 'last_name', 'phone').iterator(100):
        teacher.phone = ''.join(i for i in teacher.phone if i.isdigit())
        teacher.first_name = teacher.first_name.capitalize()
        teacher.last_name = teacher.last_name.capitalize()
        teacher.save(update_fields=['first_name', 'last_name', 'phone'])


def backwards(apps, schema):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('teachers', '0004_teacher_phone'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]