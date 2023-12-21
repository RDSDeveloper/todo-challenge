from rest_framework import viewsets, serializers, permissions
from django_filters import rest_framework as filters
from django.http import HttpRequest, HttpResponse
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
from .filters import TodoFilter
import logging

logger = logging.getLogger(__name__)


class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and manipulating todo instances.
    """

    serializer_class = TodoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TodoFilter

    def get_queryset(self) -> "QuerySet[Todo]":
        """
        Fetches todos for the currently authenticated user.

        Returns:
            QuerySet[Todo]: A queryset of todos for the current user.
        """
        logger.info(f"Fetching todos for user {self.request.user.username}")
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer: serializers.Serializer) -> None:
        """
        Creates a todo for the currently authenticated user.

        Args:
            serializer (serializers.Serializer): The serializer containing the data to be saved.
        """
        logger.info(f"Creating todo for user {self.request.user.username}")
        serializer.save(user=self.request.user)

    def destroy(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Deletes a todo for the currently authenticated user.

        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The response object.
        """
        logger.info(
            f"Deleting todo with id {kwargs['pk']} for user {request.user.username}"
        )
        return super().destroy(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and manipulating tag instances.
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: serializers.Serializer) -> None:
        """
        Creates a tag for the currently authenticated user.

        Args:
            serializer (serializers.Serializer): The serializer containing the data to be saved.
        """
        logger.info(f"Creating tag for user {self.request.user.username}")
        serializer.save(user=self.request.user)

    def destroy(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Deletes a tag for the currently authenticated user.

        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The response object.
        """
        logger.info(
            f"Deleting tag with id {kwargs['pk']} for user {request.user.username}"
        )
        return super().destroy(request, *args, **kwargs)
