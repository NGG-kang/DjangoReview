from django.contrib.auth.views import LoginView
from django.urls import path
from .views import post_list, post_update, post_create, post_detail, post_delete, post_like, post_unlike

app_name = 'instagram'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_create/', post_create, name='post_create'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/post_update/', post_update, name='post_update'),
    path('<int:pk>/post_delete/', post_delete, name='post_delete'),
    path('<int:pk>/post_delete/', post_delete, name='post_delete'),
    path('<int:pk>/post_like/', post_like, name='post_like'),
    path('<int:pk>/post_unlike/', post_unlike, name='post_unlike'),
]

