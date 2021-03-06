from django.urls import path

from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.group_app, name='index'),
    path('list/', views.groups, name='list'),
    path('create/', views.create_group, name='create'),
    path('edit/<int:pk>/', views.edit_group, name='edit'),
    path('remove/<int:pk>/', views.remove_group, name='remove'),
    path('generate/', views.generate_group, name='generate'),
]
