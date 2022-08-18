from django.contrib import admin
# Models
from apps.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
