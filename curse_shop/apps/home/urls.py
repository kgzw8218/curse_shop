from django.urls import path
from . import views
from .views import HomeAPIView

urlpatterns = [
    path("", HomeAPIView.as_view(), name="home"),
]