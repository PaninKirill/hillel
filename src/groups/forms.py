from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'faculty',
            'degree_specialization',
            'course',
        )
