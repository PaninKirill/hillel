from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['faculty', 'degree_specialization', 'course', 'head', 'supervisor']
    list_select_related = ['head', 'supervisor']


admin.site.register(Group, GroupAdmin)
