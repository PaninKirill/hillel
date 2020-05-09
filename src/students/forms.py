from django import forms

from students.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'grade'
        )
