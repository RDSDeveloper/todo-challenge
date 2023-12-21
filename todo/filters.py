from django_filters import rest_framework as filters
from .models import Todo


class TodoFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    description = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Todo
        fields = ["created_at", "description", "tags__name"]
