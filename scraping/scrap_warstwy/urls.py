from django.urls import path
from scrap_warstwy import views

urlpatterns = [
    path('warstwy', views.warstwy)
]