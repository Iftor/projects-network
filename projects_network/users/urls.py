from django.urls import path
from .views import Login, LogoutView, CheckAuthenticated

urlpatterns = [
  path('login', Login.as_view(), name='login'),
  path('logout', LogoutView.as_view(), name='logout'),
  path('authenticated', CheckAuthenticated.as_view(), name='check_authenticated'),
]
