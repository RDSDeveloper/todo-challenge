from django.urls import include, path
from rest_framework import routers
from .views import TodoViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r"todos", TodoViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
