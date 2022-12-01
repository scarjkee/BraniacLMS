from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ["title", "preambule", "body"]
    list_per_page = 5
    list_filter = ['created', 'updated']


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'deleted', 'created']
    search_fields = ["name", "cost"]
    list_per_page = 4
    list_filter = ['created', 'updated', 'cost']
    actions = ['mark_deleted']

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")