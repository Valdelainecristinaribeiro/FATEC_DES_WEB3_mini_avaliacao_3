from django.urls import path
from . import views as vs

urlpatterns = [
    path('', vs.feriados)
]