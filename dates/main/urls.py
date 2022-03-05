from django.urls import path, include
from .views.views import RegistrationView
from .views.user_list import UserListView


urlpatterns = [
    path('user_list', UserListView.as_view()),
    path('registration', RegistrationView.as_view()),

]