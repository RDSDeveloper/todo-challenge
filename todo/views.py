from rest_framework import viewsets, permissions
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as filters


class TodoFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    description = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Todo
        fields = ["created_at", "description", "tags__name"]


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TodoFilter

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
