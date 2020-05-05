from django.http import HttpResponse
from teachers.models import Teacher
from faker import Faker
import random
from utils import parse_usr_value, clear_table_parser, list_rank
from django.db import connection


def teacher_app(request):
    print(request)
    return HttpResponse('Teacher app')


def teachers(request):
    count = Teacher.objects.count()
    teachers_queryset = Teacher.objects.all()

    response = f'Teachers: {count}<br/>'

    for teacher in teachers_queryset:
        response += teacher.info() + '<br/>'

    return HttpResponse(response)


def generate_teacher(request):
    fake = Faker()
    rand_age = random.randint(25, 75)
    teacher = Teacher.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=rand_age,
                                     rank=random.choice(list_rank),
                                     )
    response = f'Teacher: {teacher.info()}<br/>'

    return HttpResponse(response)


def sheets(request):
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    response = f'Current sheets: {seen_models}<br/>'

    return HttpResponse(response)


def clear_sheet(request):
    """
    :param request:
    /clear_sheet/tc/?clear=1&sheet_name=Teacher
    :return:
    Wipes out all rows in sheet Teacher
    """
    req_clear_sheet = clear_table_parser(request.GET['clear'], 'digit')
    sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    response = f'Selected SHEET has been cleared:<br/>'
    if sheet_name == 'Teacher':
        if req_clear_sheet == 1:
            Teacher.objects.all().delete()
            response += f'{sheet_name}'
    return HttpResponse(response)


def delete_row(request):
    """
    :param request:
    /del_row/tc/?id=49
    :return:
    Wipes out selected row from current table
    """
    req_clear_row = clear_table_parser(request.GET['id'], 'id')
    try:
        Teacher.objects.filter(id=req_clear_row).delete()
        response = f'Selected ROW has been cleared: {req_clear_row}<br/>'
    except Exception:
        response = f'Something went wrong. Enter valid value'

    return HttpResponse(response)


def query_filter(request):
    """
    :param request:
    filter/tc/?letter=re
    :return:
    list of teachers with params equal to request: id, first_name, last_name, age, rank
    """
    # sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    letter = clear_table_parser(request.GET['letter'], 'alpha')
    response = f'Selected data:<br/>'
    filter_queryset = Teacher.objects.filter(first_name__startswith=str(letter))

    for teacher in filter_queryset:
        response += teacher.info() + '<br/>'

    return HttpResponse(response)


def generate_teachers(request):
    """
    :param request:
    generate_teachers/tc/?count=10
    :return:
    list of 10 teachers: id, first_name, last_name, age, rank.
    """
    fake = Faker()
    rand_teachers_queryset = Teacher.objects.all()
    response = f'Teachers:<br/>'
    usr_value = parse_usr_value(request.GET['count'])
    if type(usr_value) is str:
        return HttpResponse(usr_value)

    for _ in range(usr_value):
        Teacher.objects.create(first_name=fake.first_name(),
                               last_name=fake.last_name(),
                               age=random.randint(25, 75),
                               rank=random.choice(list_rank),
                               )

    for teacher in rand_teachers_queryset:
        response += teacher.info() + '<br/>'

    return HttpResponse(response)
