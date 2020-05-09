import random

from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from faker import Faker

from teachers.models import Teacher

from utils import clear_table_parser, parse_usr_value


def teacher_app(request):
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
    teacher = Teacher.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(25, 75),
        rank=random.choice(Teacher.TEACHERS_RANK)[0],
    )
    response = f'Teacher: {teacher.info()}<br/>'

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
    /filter/tc/?age=50&first_name=Elizabeth
    /filter/tc/?order_by=age
    /filter/tc/?age=20&order_by=-first_name
    :return:
    list of teachers with params equal to request:
    id, first_name, last_name, age, rank, etc..
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
        'rank',
        'rank__startswith',
        'rank__endswith',
        'id',
        'order_by',
     ]

    response = f'Selected data:<br/>'
    teachers_queryset = Teacher.objects.all()

    # simple filter

    for param in params:
        value = request.GET.get(param)
        if param not in 'order_by':
            if value:
                teachers_queryset = teachers_queryset.filter(**{param: value})

    # adds filter order_by

    for param in params:
        value = request.GET.get(param)
        if param in 'order_by':
            if value:
                teachers_queryset = teachers_queryset.order_by(value)

    for teacher in teachers_queryset:
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
        Teacher.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(25, 75),
            rank=random.choice(Teacher.TEACHERS_RANK)[0],
        )

    for teacher in rand_teachers_queryset:
        response += teacher.info() + '<br/>'

    return HttpResponse(response)


def t_index(request):
    return render(request, 't_index.html')


def create_teacher(request):
    from teachers.forms import TeacherCreateForm

    if request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacher/')
    else:
        form = TeacherCreateForm()

    context = {'create_form': form}

    return render(request, 'create_student.html', context=context)
