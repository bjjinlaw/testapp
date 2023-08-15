from rest_framework import routers
from testapp.views import TaskViewSet, CategoryViewSet, Home
from django.urls import path, include


router = routers.SimpleRouter()
router.register("tasks", TaskViewSet, basename="task")

router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("api/", include(router.urls)),
]
