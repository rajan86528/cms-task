from django.urls import path
from .views import UserRegistrationView, UserLoginView, AdminListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('admins/', AdminListView.as_view(), name="admin-list")
]