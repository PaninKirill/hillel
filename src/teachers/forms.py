from django import forms

from teachers.models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'age',
            'rank',
            'email',
            'phone',
        )

    def clean_age(self):  # clean_ + field
        course = self.cleaned_data['age']
        if not 18 <= course <= 99:
            raise forms.ValidationError('You are either too young or too old')
        return course

    def clean_phone(self):  # clean_ + field
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits')
        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError('First name must contain only letters')
        return first_name

    def clean_last_name(self):  # Petr 1 - not allowed
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError('Last name must contain only letters')
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        check_existence = Teacher.objects.all().only('email').filter(email__iexact=email).exclude(email__iexact=email)
        if len(check_existence) != 0:
            raise forms.ValidationError(f'{email} already exists')
        return email
