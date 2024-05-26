from django.urls import path
from .views import AddAndChangeUser,UserCopyView

urlpatterns = [
    path("user/", AddAndChangeUser.as_view()),
    path("user/<pk>/", AddAndChangeUser.as_view()),
    path("userCopy/", UserCopyView.as_view()),
    path("userCopy/<pk>/", UserCopyView.as_view()),
]
