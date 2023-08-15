from rest_framework import routers
from testapp.views import Home
from django.urls import path, include


router = routers.SimpleRouter()

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("api/", include(router.urls)),
]
