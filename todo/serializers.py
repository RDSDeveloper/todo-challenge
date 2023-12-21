from rest_framework import serializers
from .models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Tag
        fields = ["id", "name", "user"]


class TagField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Tag.objects.get(name=data)


class TodoSerializer(serializers.ModelSerializer):
    tags = TagField(many=True, queryset=Tag.objects.all())
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "updated_at",
            "due_date",
            "priority",
            "tags",
            "user",
        ]
