import random

from django.apps import apps
from django.http import HttpResponse

from groups.models import Group

from utils import clear_table_parser, parse_usr_value


def group_app(request):
    return HttpResponse('Group app')


def groups(request):
    count = Group.objects.count()
    groups_queryset = Group.objects.all()

    response = f'Groups: {count}<br/>'

    for group in groups_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)


def generate_group(request):
    set_faculty = random.choice(list(Group.FACULTY_N_SPECIALIZATION.keys()))
    set_degree_specialization = random.choice(Group.FACULTY_N_SPECIALIZATION.get(set_faculty))
    group = Group.objects.create(
        faculty=set_faculty,
        degree_specialization=set_degree_specialization,
        course=random.randint(1, 5),
    )
    response = f'Group: {group.info()}<br/>'

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
    /filter/tc/?age=50&first_name=Elizabeth
    /filter/gr/?order_by=course
    /filter/gr/?course=2&order_by=-faculty
    :return:
    list of teachers with params equal to request:
    id, faculty, degree_specialization, course...
    """
    params = [
        'course',
        'course__gt',
        'course__lt',
        'course__lte',
        'course__gte',
        'faculty',
        'faculty__exact',
        'faculty__startswith',
        'faculty__endswith',
        'degree_specialization',
        'degree_specialization__startswith',
        'degree_specialization__endswith',
        'id',
        'order_by',
    ]

    response = f'Selected data:<br/>'
    groups_queryset = Group.objects.all()

    # simple filter

    for param in params:
        value = request.GET.get(param)
        if param not in 'order_by':
            if value:
                groups_queryset = groups_queryset.filter(**{param: value})

    # adds filter order_by

    for param in params:
        value = request.GET.get(param)
        if param in 'order_by':
            if value:
                groups_queryset = groups_queryset.order_by(value)

    for group in groups_queryset:
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
        set_faculty = random.choice(list(Group.FACULTY_N_SPECIALIZATION.keys()))
        set_degree_specialization = random.choice(Group.FACULTY_N_SPECIALIZATION.get(set_faculty))
        Group.objects.create(
            faculty=set_faculty,
            degree_specialization=set_degree_specialization,
            course=random.randint(1, 5),
        )

    for group in rand_groups_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)
