from django.urls import path
from . import views



urlpatterns = [
    path("start/", views.start),
    path("link/", views.link),
    path("stream/", views.stream),
    path("refresh/", views.refresh),
    path("play/", views.play),
    path("stop/", views.stop),
]