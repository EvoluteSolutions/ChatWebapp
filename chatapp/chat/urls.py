
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Home page URL pattern
    path('login_view/',views.login_view,name="login_view"),
]
