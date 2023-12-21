from rest_framework import viewsets, permissions
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class TodoFilter(filters.FilterSet):
    tags__name = filters.ChoiceFilter(choices=[])

    class Meta:
        model = Todo
        fields = ["tags__name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.request.query_params.get("user")
        if user:
            self.filters["tags__name"].extra.update(
                {
                    "choices": [
                        (tag.name, tag.name) for tag in Tag.objects.filter(user=user)
                    ]
                }
            )


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
