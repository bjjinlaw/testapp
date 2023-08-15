from rest_framework import routers
from testapp.views import TaskViewSet, CategoryViewSet, home
from django.urls import path, include


router = routers.SimpleRouter()
router.register("tasks", TaskViewSet, basename="task")

router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", home, name="home"),
    path("api/", include(router.urls)),
]
