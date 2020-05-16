from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('students/', include('students.urls'), name='students'),
    path('teachers/', include('teachers.urls'), name='teachers'),
    path('groups/', include('groups.urls'), name='groups'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
