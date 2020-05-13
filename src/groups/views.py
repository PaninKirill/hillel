import random

from django.apps import apps
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import GroupCreateForm
from groups.models import Group

from utils import clear_table_parser, parse_usr_value


def home(request):
    return render(request, 'index.html')


def group_app(request):  # main page
    return render(request, 'group_index.html')


def groups(request):
    count = Group.objects.count()
    groups_queryset = Group.objects.all()

    response = f'Groups: {count}<br/>'

    for group in groups_queryset:
        response += group.info() + '<br/>'

    context = {'groups': groups_queryset, 'count': count}

    return render(request, 'groups_list.html', context=context)


def generate_group(request):
    set_params = {i[0]: i[1] for i in Group.FACULTY_N_SPECIALIZATION}
    set_faculty = random.choice(list(set_params.keys()))
    set_degree = random.choice(list(set_params.get(set_faculty)))
    group = Group.objects.create(
        faculty=set_faculty,
        degree_specialization=set_degree[1],
        course=random.randint(1, 5),
    )

    return render(request, 'generate_group.html', context={'group': group})


def sheets(request):  # abandoned
    sheets_reg = [
        m._meta.db_table for c in apps.get_app_configs() for m in c.get_models()
    ]
    response = f'Current sheets: {sheets_reg}<br/>'
    return HttpResponse(response)


def clear_sheet(request):  # abandoned
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


def delete_row(request):  # abandoned
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


def query_filter(request):  # abandoned
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


def generate_groups(request):  # abandoned
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
        set_params = {i[0]: i[1] for i in Group.FACULTY_N_SPECIALIZATION}
        set_faculty = random.choice(list(set_params.keys()))
        set_degree = random.choice(list(set_params.get(set_faculty)))
        groups.append(Group(
            faculty=set_faculty,
            degree_specialization=set_degree[1],
            course=random.randint(1, 5),
        ))
    Group.objects.bulk_create(groups)

    for group in rand_groups_queryset:
        response += group.info() + '<br/>'

    return HttpResponse(response)


def create_group(request):
    if request.method == 'POST':

        form = GroupCreateForm(request.POST)

        if form.is_valid():
            related_data = {i[0]: i[1] for i in Group.FACULTY_N_SPECIALIZATION}
            faculty = form.data.get('faculty')
            check_related = related_data.get(faculty)
            for spec in check_related:
                if spec[0] == form.data.get('degree_specialization'):
                    form.save()
                    messages.success(request, 'You have successfully created group')
                    return HttpResponseRedirect(reverse('groups:list'))
            messages.warning(request, 'Faculty does not much')
    else:
        form = GroupCreateForm()

    context = {'form': form}

    return render(request, 'create_group.html', context=context)


def edit_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':

        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            related_data = {i[0]: i[1] for i in Group.FACULTY_N_SPECIALIZATION}
            faculty = form.data.get('faculty')
            check_related = related_data.get(faculty)
            for spec in check_related:
                if spec[0] == form.data.get('degree_specialization'):
                    form.save()
                    messages.success(request, 'You have successfully changed group')
                    return HttpResponseRedirect(reverse('groups:list'))

            messages.warning(request, 'Faculty does not much')
    else:
        form = GroupCreateForm(instance=group)

    context = {'form': form, 'group': group}

    return render(request, 'edit_group.html', context=context)


def remove_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    messages.success(request, 'You have successfully deleted group')

    return HttpResponseRedirect(reverse('groups:list'))
