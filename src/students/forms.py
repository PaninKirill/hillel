from django import forms

from students.models import Student
from students.tasks import email_sender


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'grade',
            'email',
            'phone',
        )

    # def clean_phone(self):  # clean_ + field
        """
        auto-cleaner phone after form submit
        """
    #     phone = self.cleaned_data['phone']
    #     cleaned_phone = ''.join(i for i in phone if i.isdigit())
    #     return cleaned_phone

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
        check_existence = Student.objects.all().only('email').filter(email__iexact=email).exclude(email__iexact=email)
        if len(check_existence) != 0:
            raise forms.ValidationError(f'{email} already exists')
        return email


class ContactUsForm(forms.Form):
    CHOICES = [('-', '-'),
               ('Service related', 'Service related'),
               ('New comers', 'New comers'),
               ]  # to separate departments
    issue = forms.ChoiceField(choices=CHOICES, required=True)  # will appear in email TITLE alongside form.title
    username = forms.CharField(max_length=36, required=True, label='Name')
    email = forms.EmailField(max_length=36, required=True)
    subject = forms.CharField(max_length=36, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    field_order = ['username', 'email', 'subject', 'issue', 'message', ]

    def save(self):
        issue = self.cleaned_data["issue"]
        username = self.cleaned_data["username"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        email = self.cleaned_data["email"]
        # rabbitMQ
        return email_sender.apply_async(args=[issue, username, subject, message, email], countdown=3)
        # async - for fun
        # rabbitMQ

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalpha():
            raise forms.ValidationError('Field name must contain only letters')
        return username

    def clean_issue(self):
        issue = self.cleaned_data['issue']
        if issue in '-':
            raise forms.ValidationError('Choose related topic')
        return issue
