from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_veiw, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
]