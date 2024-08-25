
from django.urls import path
from account_app.views import SignUpView, LoginView, UserListView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
]
