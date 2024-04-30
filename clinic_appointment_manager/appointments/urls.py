from django import path
from appointments import views

urlpatterns = [
    path('', views.hola)
]