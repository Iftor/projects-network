from django.contrib import admin

from .models import Community, CommunityParticipant


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(CommunityParticipant)
class CommunityParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "community", "participant"]


