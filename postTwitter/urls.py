from django.urls import path
from . import views

urlpatterns =[
    path("prueba",views.prueba),
    path("users/",views.users),
    path("user/<int:id>",views.user),
]