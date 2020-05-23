from django import forms

from groups.models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'faculty',
            'degree_specialization',
            'course',
            'head',
            'supervisor',
        )

    def clean_course(self):  # clean_ + field
        course = self.cleaned_data['course']
        if not 1 <= course <= 5:
            raise forms.ValidationError('Choose between 1-5')
        return course

    def clean_faculty(self):  # clean_ + field
        faculty = self.cleaned_data['faculty']
        return faculty

    def clean_degree_specialization(self):
        degree_specialization = self.cleaned_data['degree_specialization']
        related_data = {i[0]: i[1] for i in Group.FACULTY_N_SPECIALIZATION}
        faculty = self.clean_faculty()
        check_related = related_data.get(faculty)
        for spec in check_related:
            if spec[0] == degree_specialization:
                return degree_specialization
        raise forms.ValidationError(f'{degree_specialization} does not belong to {faculty}')
