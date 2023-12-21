from rest_framework import viewsets, permissions
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tags__name"]

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
