from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [

    path('register/', views.register_view, name="register_view"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(), name="logout"),

]
