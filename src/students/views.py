from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student


def hello_world(request):
    print(request)
    return HttpResponse('Hello world')


def students(request):
    count = Student.objects.count()  # SELECT COUNT(*) FROM students_student;
    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    response = f'students: {count}<br/>'

    for student in students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)
