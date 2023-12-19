from django.contrib import admin
from .models import Todo, Tag


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "completed",
        "created_at",
        "updated_at",
        "user",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
