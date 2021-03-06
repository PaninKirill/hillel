# Generated by Django 2.2 on 2020-05-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(
                choices=[
                    ('PR', 'Professor'),
                    ('AEP', 'Associate Professor'),
                    ('ASP', 'Assistant Professor'),
                    ('MI', 'Master Instructor'),
                    ('SI', 'Senior Instructor'),
                    ('IR', 'Instructor'),
                    ('RA', 'Research Associate'),
                    ('LR', 'Lecturer')
                ],
                default='LR',
                max_length=3
            ),
        ),
    ]
