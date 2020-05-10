from django import forms

from teachers.models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'rank'
        )
