from django.conf import settings
from django.urls import include, path

from students import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.students_app, name='index'),
    path('list/', views.students, name='list'),
    path('create/', views.create_student, name='create'),
    path('edit/<int:pk>/', views.edit_student, name='edit'),
    path('remove/<int:pk>/', views.remove_student, name='remove'),
    path('generate/', views.generate_student, name='generate'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
