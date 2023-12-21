from django.urls import include, path
from rest_framework import routers
from .views import TodoViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r"todos", TodoViewSet, basename="todo")
router.register(r"tags", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
