from django.urls import path
from .views import AddAndChangeUser

urlpatterns = [
    path("user/", AddAndChangeUser.as_view()),
    path("user/<pk>/", AddAndChangeUser.as_view()),
]
