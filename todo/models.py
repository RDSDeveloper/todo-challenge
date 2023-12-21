from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    PRIORITY_CHOICES = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(
        get_user_model(), related_name="todos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
