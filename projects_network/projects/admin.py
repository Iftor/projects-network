from django.contrib import admin

from .models import Project, ProjectParticipant, ProjectRole, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(ProjectParticipant)
class ProjectParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "project", "participant"]


@admin.register(ProjectRole)
class ProjectRoleParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
