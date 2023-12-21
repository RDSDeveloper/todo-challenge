from rest_framework import serializers
from .models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    """
    A serializer for the Tag model.
    """

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        """
        Meta class for TagSerializer.
        """

        model = Tag
        fields = ["id", "name", "user"]


class TagField(serializers.RelatedField):
    """
    A custom field for representing a Tag object.
    """

    def to_representation(self, value: Tag) -> str:
        """
        Converts a Tag object to its string representation.

        Args:
            value (Tag): The Tag object.

        Returns:
            str: The name of the Tag.
        """
        return value.name

    def to_internal_value(self, data: str) -> Tag:
        """
        Converts a string to a Tag object.

        Args:
            data (str): The name of the Tag.

        Returns:
            Tag: The Tag object.
        """
        return Tag.objects.get(name=data)


class TodoSerializer(serializers.ModelSerializer):
    """
    A serializer for the Todo model.
    """

    tags = TagField(many=True, queryset=Tag.objects.all())
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        """
        Meta class for TodoSerializer.
        """

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
