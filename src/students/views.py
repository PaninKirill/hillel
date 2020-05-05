from django.http import HttpResponse
from students.models import Student
from faker import Faker
import random
from utils import parse_usr_value, clear_table_parser
from django.db import connection


def students_app(request):
    print(request)
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
    rand_age = random.randint(18, 25)
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=rand_age,
                                     )
    response = f'Student: {student.info()}<br/>'

    return HttpResponse(response)


def sheets(request):
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    response = f'Current sheets: {seen_models}<br/>'

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
    /filter/st/?letter=A
    :return:
    list of students with params equal to request: id, first_name, last_name, age
    """
    # sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    letter = clear_table_parser(request.GET['letter'], 'alpha')
    response = f'Selected data:<br/>'
    filter_queryset = Student.objects.filter(first_name__startswith=str(letter))

    for student in filter_queryset:
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
        Student.objects.create(first_name=fake.first_name(),
                               last_name=fake.last_name(),
                               age=random.randint(18, 25),
                               )

    for student in rand_students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)
