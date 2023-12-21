import logging
from django.db import models
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)


class Tag(models.Model):
    """
    A model representing a tag.
    """

    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Returns a string representation of the tag.

        Returns:
            str: The name of the tag.
        """
        return self.name

    def save(self, *args, **kwargs) -> None:
        """
        Saves the tag.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        logger.info(f"Saving tag {self.name}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        """
        Deletes the tag.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        logger.info(f"Deleting tag {self.name}")
        super().delete(*args, **kwargs)


class Todo(models.Model):
    """
    A model representing a todo item.
    """

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

    def __str__(self) -> str:
        """
        Returns a string representation of the todo item.

        Returns:
            str: The title of the todo item.
        """
        return self.title

    def save(self, *args, **kwargs) -> None:
        """
        Saves the todo item.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        logger.info(f"Saving todo {self.title}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        """
        Deletes the todo item.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        logger.info(f"Deleting todo {self.title}")
        super().delete(*args, **kwargs)
