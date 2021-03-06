from django.contrib import admin

from .models import Technology, Status


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
