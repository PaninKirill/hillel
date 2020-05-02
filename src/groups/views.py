from django.http import HttpResponse
from groups.models import Group
import random
from utils import parse_usr_value, clear_table_parser, random_faculty_n_specialization
from django.db import connection


def group_app(request):
    print(request)
    return HttpResponse('Group app')


def groups(request):
    count = Group.objects.count()
    groups_queryset = Group.objects.all()

    response = f'Groups: {count}<br/>'

    for group in groups_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)


def generate_group(request):
    rand_course = random.randint(1, 5)
    group = Group.objects.create(faculty=random_faculty_n_specialization('faculty'),
                                 degree_specialization=random_faculty_n_specialization('specialization'),
                                 course=rand_course,
                                 )
    response = f'Group: {group.info()}<br/>'

    return HttpResponse(response)


def sheets(request):
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    response = f'Current sheets: {seen_models}<br/>'

    return HttpResponse(response)


def clear_sheet(request):
    """
    :param request:
    /clear_sheet/gr/?clear=1&sheet_name=Group
    :return:
    Wipes out all rows in sheet Group
    """
    req_clear_sheet = clear_table_parser(request.GET['clear'], 'digit')
    sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    response = f'Selected SHEET has been cleared:<br/>'
    if sheet_name == 'Group':
        if req_clear_sheet == 1:
            Group.objects.all().delete()
            response += f'{sheet_name}'

    return HttpResponse(response)


def delete_row(request):
    """
    :param request:
    /del_row/gr/?id=49
    :return:
    Wipes out selected row from current table
    """
    req_clear_row = clear_table_parser(request.GET['id'], 'id')
    try:
        Group.objects.filter(id=req_clear_row).delete()
        response = f'Selected ROW has been cleared: {req_clear_row}<br/>'
    except Exception:
        response = f'Something went wrong. Enter valid value'

    return HttpResponse(response)


def query_filter(request):
    """
    :param request:
    filter/gr/?letter=re
    :return:
    list of teachers with params equal to request: id, faculty, degree_specialization, course
    """
    # sheet_name = clear_table_parser(request.GET['sheet_name'], 'alpha')
    letter = clear_table_parser(request.GET['letter'], 'alpha')
    response = f'Selected data:<br/>'
    filter_queryset = Group.objects.filter(faculty__startswith=str(letter))

    for group in filter_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)


def generate_groups(request):
    """
    :param request:
    PATH: /generate_groups/gr/?count=10
    :return:
    list of 10 groups: id, faculty, degree_specialization, course.
    """
    rand_groups_queryset = Group.objects.all()
    response = f'Groups:<br/>'
    usr_value = parse_usr_value(request.GET['count'])
    if type(usr_value) is str:
        return HttpResponse(usr_value)

    for _ in range(usr_value):
        Group.objects.create(faculty=random_faculty_n_specialization('faculty'),
                             degree_specialization=random_faculty_n_specialization('specialization'),
                             course=random.randint(1, 5),
                             )

    for group in rand_groups_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)
