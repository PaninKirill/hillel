from django.db import models


class Group(models.Model):
    FACULTY_N_SPECIALIZATION = {
        'Music': [
            'Theatre Faculty ',
            'Film and TV',
            'Music and Dance Faculty',
        ],
        'Art and Design': [
            'Digital Arts',
            'Electronic Integrated Arts',
            'Art & Design',
            'Ceramic Art',
        ],
        'Medicine': [
            'Critical Care Medicine',
            'Pain Medicine',
            'Pediatric Anesthesiology',
            'Obstetric Anesthesiology',
        ],
        'Law': [
            'Law and Sexuality',
            'International and Comparative Law',
            'Human Rights',
            'Media, Entertainment and Technology Law and Policy',
            'Law and Philosophy',
        ],
        'Forestry': [
            'Forestry',
            'Natural Resources',
            'Wildlife Sciences',
        ],
        'Arts and Humanity': [
            'Commerce,Law and Management',
            'Engineering and the Built Environment',
            'Health Sciences',
            'Science',
            'Humanities',
        ],
        'Dentistry': [
            'Orthopedic dentistry',
            'Propedeutics of therapeutic dentistry',
            'Propaedeutics of pediatric therapeutic dentistry',
            'Therapeutic dentistry',
            'Pediatric therapeutic dentistry.',
            'Prevention of dental diseases',
        ],

    }

    faculty = models.CharField(max_length=64)
    degree_specialization = models.CharField(max_length=64)
    course = models.IntegerField()

    def info(self) -> str:
        return f'{self.id} {self.faculty} {self.degree_specialization} {self.course}'

    def __str__(self):
        return f'{self.id}, {self.faculty}'

    def __repr__(self):
        return f'{self.id}, {self.faculty}, {self.degree_specialization}'
