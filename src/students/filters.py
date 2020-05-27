import django_filters

from students.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
