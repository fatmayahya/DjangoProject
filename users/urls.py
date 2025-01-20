from .views.auth_views import login_view, logout_view
from .views.profile_views import profile_view
from django.urls import path 

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
]
