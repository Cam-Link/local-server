from django.urls import path
from . import views



urlpatterns = [
    path("link/", views.link),
    path("stream/", views.stream),
    path("stop/", views.stop),

]