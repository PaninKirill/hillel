import datetime

from celery import shared_task

from django.core.mail import send_mail
from django.utils import timezone


#
# @shared_task
# def slow_func(num=10):
#     from time import sleep
#     sleep(num)


# @shared_task
# def periodic():
#     print('HELLO\n' * 3)
#
#
# @shared_task
# def print_student(student_id):
#     from students.models import Student
#     student = Student.objects.get(id=student_id)
#     print(student.id, student.first_name, student.last_name)


@shared_task
def url_logger(method, path, execution_time):
    from students.models import Logger
    Logger.objects.create(
        method=method,
        path=path,
        execution_time=execution_time,
    )


@shared_task
def logger_cleaner():  # scheduled in celerybeat (current settings - once a day at midnight)
    from students.models import Logger
    time_delta = timezone.now() - datetime.timedelta(days=7)

    log_queryset = Logger.objects.all().only('created').filter(created__lte=time_delta)

    log_queryset.delete()


@shared_task
def email_sender(issue, username, subject, message, email):
    send_mail(
        subject=f'Department: {issue}, Subject: {subject}',
        message=f'From:{username}, {email}, {message}',
        from_email='devs.ops.tests@gmail.com',
        recipient_list=['devs.ops.tests@gmail.com', 'panin.kirill@gmail.com', 'dmytro.kaminskyi92@gmail.com', ],
        fail_silently=False,
    )
