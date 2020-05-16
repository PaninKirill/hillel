from django.contrib import admin

from teachers.models import Teacher


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'first_name', 'last_name', 'age', 'rank', 'email',)
    fields = ('first_name', 'last_name', 'age', 'rank', 'email',)
    readonly_fields = ('email',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(age__gte=30)

        return queryset


admin.site.register(Teacher, StudentAdmin)
