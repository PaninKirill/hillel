from django.contrib import admin

from groups.models import Group


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'faculty', 'degree_specialization', 'course',)
    fields = ('faculty', 'degree_specialization', 'course',)
    readonly_fields = ('faculty',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(course__lte=5)

        return queryset


admin.site.register(Group, StudentAdmin)
