import random

from django.apps import apps
from django.http import HttpResponse

from faker import Faker

from students.models import Student

from utils import clear_table_parser, parse_usr_value


def students_app(request):
    return HttpResponse('Students app')


def students(request):
    count = Student.objects.count()  # SELECT COUNT(*) FROM students_student;
    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    response = f'Students: {count}<br/>'

    for student in students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(18, 25),
        grade=random.choice(Student.YEAR_IN_SCHOOL_CHOICES)[1]
    )
    response = f'Student: {student.info()}<br/>'

    return HttpResponse(response)


def sheets(request):
    sheets_reg = [
        m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()
    ]
    response = f'Current sheets: {sheets_reg}<br/>'
    return HttpResponse(response)


def clear_sheet(request):
    """
    :param request:
    /clear_sheet/st/?clear=1&sheet_name=Student
    :return:
    Wipes out all rows in sheet Student
    """
    req_clear_sheet = clear_table_parser(request.GET['clear'], 'digit')
    sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    response = f'Selected SHEET has been cleared:<br/>'
    if sheet_name == 'Student':
        if req_clear_sheet == 1:
            Student.objects.all().delete()
            response += f'{sheet_name}'

    return HttpResponse(response)


def delete_row(request):
    """
    :param request:
    /del_row/st/?id=49
    :return:
    Wipes out selected row from current table
    """
    req_clear_row = clear_table_parser(request.GET['id'], 'id')
    try:
        Student.objects.filter(id=req_clear_row).delete()
        response = f'Selected ROW has been cleared: {req_clear_row}<br/>'
    except Exception:
        response = f'Something went wrong. Enter valid value'

    return HttpResponse(response)


def query_filter(request):
    """
    :param request:
    /filter/st/?age=22&first_name=Elizabeth
    /filter/st/?order_by=age
    /filter/st/?age=20&order_by=-first_name
    :return:
    list of students with params equal to request:
    id, first_name, last_name, age, grade, etc..
    """
    params = [
        'age',
        'age__gt',
        'age__lt',
        'age__lte',
        'age__gte',
        'first_name',
        'first_name__exact',
        'first_name__startswith',
        'first_name__endswith',
        'last_name',
        'last_name__startswith',
        'last_name__endswith',
        'grade',
        'grade__startswith',
        'grade__endswith',
        'id',
        'order_by',
    ]

    response = f'Selected data:<br/>'
    students_queryset = Student.objects.all()

    # simple filter

    for param in params:
        value = request.GET.get(param)
        if param not in 'order_by':
            if value:
                students_queryset = students_queryset.filter(**{param: value})

    # adds filter order_by

    for param in params:
        value = request.GET.get(param)
        if param in 'order_by':
            if value:
                students_queryset = students_queryset.order_by(value)

    for student in students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)


def generate_students(request):
    """
    :param request:
    PATH: /generate-students/st/?count=10
    :return:
    list of 10 students: id, first_name, last_name, age.
    """
    fake = Faker()
    rand_students_queryset = Student.objects.all()
    response = f'Students:<br/>'
    usr_value = parse_usr_value(request.GET['count'])
    if type(usr_value) is str:
        return HttpResponse(usr_value)

    for _ in range(usr_value):
        Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 25),
            grade=random.choice(Student.YEAR_IN_SCHOOL_CHOICES)[1]
        )

    for student in rand_students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)
