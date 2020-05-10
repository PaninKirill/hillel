from django.db import models


class Group(models.Model):
    FACULTY = [
        ('Music', 'Music'),
        ('Art and Design', 'Art and Design'),
        ('Medicine', 'Medicine'),
        ('Law', 'Law'),
        ('Forestry', 'Forestry'),
        ('Arts and Humanity', 'Arts and Humanity'),
        ('Dentistry', 'Dentistry'),

    ]
    FACULTY_N_SPECIALIZATION = [
        ('Music', (
            ('Theatre Faculty', 'Theatre Faculty'),
            ('Film and TV', 'Film and TV'),
            ('Music and Dance Faculty', 'Music and Dance Faculty'),
        )
         ),
        ('Art and Design', (
            ('Digital Arts', 'Digital Arts'),
            ('Electronic Integrated Arts', 'Electronic Integrated Arts'),
            ('Art & Design', 'Art & Design'),
            ('Ceramic Art', 'Ceramic Art'),
        )
         ),
        ('Medicine', (
            ('Critical Care Medicine', 'Critical Care Medicine'),
            ('Pain Medicine', 'Pain Medicine'),
            ('Pediatric Anesthesiology', 'Pediatric Anesthesiology'),
            ('Obstetric Anesthesiology', 'Obstetric Anesthesiology'),
        )
         ),
        ('Law', (
            ('Law and Sexuality', 'Law and Sexuality'),
            ('International and Comparative Law', 'International and Comparative Law'),
            ('Human Rights', 'Human Rights'),
            ('Media, Entertainment', 'Media, Entertainment'),
            ('Law and Philosophy', 'Law and Philosophy'),
        )
         ),
        ('Forestry', (
            ('Forestry', 'Forestry'),
            ('Natural Resources', 'Natural Resources'),
            ('Wildlife Sciences', 'Wildlife Sciences'),
        )
         ),
        ('Arts and Humanity', (
            ('Commerce,Law and Management', 'Commerce,Law and Management'),
            ('Engineering and the Built Environment', 'Engineering and the Built Environment'),
            ('Health Sciences', 'Health Sciences'),
            ('Science', 'Science'),
            ('Humanities', 'Humanities'),
        )
         ),
        ('Dentistry', (
            ('Orthopedic dentistry', 'Orthopedic dentistry'),
            ('Propedeutics of therapeutic dentistry', 'Propedeutics of therapeutic dentistry'),
            ('Propaedeutics of pediatric therapeutic dentistry', 'Propaedeutics of pediatric therapeutic dentistry'),
            ('Therapeutic dentistry', 'Therapeutic dentistry'),
            ('Pediatric therapeutic dentistry', 'Pediatric therapeutic dentistry'),
            ('Prevention of dental diseases', 'Prevention of dental diseases'),
        )
         ),
    ]

    faculty = models.CharField(
        max_length=64,
        choices=FACULTY
    )
    degree_specialization = models.CharField(
        max_length=64,
        choices=FACULTY_N_SPECIALIZATION,
    )
    course = models.IntegerField()

    def info(self) -> str:
        return f'{self.id} {self.faculty} {self.degree_specialization} {self.course}'

    def __str__(self):
        return f'{self.id}, {self.faculty}'

    def __repr__(self):
        return f'{self.id}, {self.faculty}, {self.degree_specialization}'
