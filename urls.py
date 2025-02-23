from django.urls import path
from . import views
from django.urls import include
patternsList = [
    path("", views.fortune)
    path("", include("randomfortune.urls"))
]
