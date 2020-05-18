from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.teacher_app, name='index'),
    path('list/', views.teachers, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('edit/<int:pk>/', views.edit_teacher, name='edit'),
    path('remove/<int:pk>/', views.remove_teacher, name='remove'),
    path('generate/', views.generate_teacher, name='generate'),
]
