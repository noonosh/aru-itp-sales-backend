from django.urls import path
from . import views


urlpatterns = [
    path('cars/', views.CarsList.as_view()),
]
