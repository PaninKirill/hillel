from django.contrib import admin
from django.urls import path

from groups import views as g_views

from students import views as s_views

from teachers import views as t_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', s_views.st_index),
    path('student/create_student/', s_views.create_student),
    path('teacher/', t_views.t_index),
    path('teacher/create_teacher/', t_views.create_teacher),
    path('group/', g_views.g_index),
    path('group/create_group/', g_views.create_group),

    path('main/st/', s_views.students_app),
    path('main/tc/', t_views.teacher_app),
    path('main/gr/', g_views.group_app),
    path('students/st/', s_views.students),
    path('teachers/tc/', t_views.teachers),
    path('groups/gr/', g_views.groups),
    path('generate_student/st/', s_views.generate_student),
    path('generate_teacher/tc/', t_views.generate_teacher),
    path('generate_group/gr/', g_views.generate_group),
    path('generate_students/st/', s_views.generate_students),
    path('generate_teachers/tc/', t_views.generate_teachers),
    path('generate_groups/gr/', g_views.generate_groups),
    path('clear_sheet/st/', s_views.clear_sheet),
    path('clear_sheet/tc/', t_views.clear_sheet),
    path('clear_sheet/gr/', g_views.clear_sheet),
    path('sheets/st/', s_views.sheets),
    path('sheets/tc/', t_views.sheets),
    path('sheets/gr/', g_views.sheets),
    path('filter/st/', s_views.query_filter),
    path('filter/tc/', t_views.query_filter),
    path('filter/gr/', g_views.query_filter),
    path('del_row/st/', s_views.delete_row),
    path('del_row/tc/', t_views.delete_row),
    path('del_row/gr/', g_views.delete_row),
]
