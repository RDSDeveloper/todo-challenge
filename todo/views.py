from rest_framework import viewsets, permissions
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
import logging
from .filters import TodoFilter
from django_filters import rest_framework as filters


logger = logging.getLogger(__name__)


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TodoFilter

    def get_queryset(self):
        logger.info(f"Fetching todos for user {self.request.user.username}")
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        logger.info(f"Creating todo for user {self.request.user.username}")
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        logger.info(
            f"Deleting todo with id {kwargs['pk']} for user {request.user.username}"
        )
        return super().destroy(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f"Creating tag for user {self.request.user.username}")
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        logger.info(
            f"Deleting tag with id {kwargs['pk']} for user {request.user.username}"
        )
        return super().destroy(request, *args, **kwargs)
