from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', views.PostViewSet)





app_name = 'instagram'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/post_update/', views.post_update, name='post_update'),
    path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/post_like/', views.post_like, name='post_like'),
    path('<int:pk>/post_unlike/', views.post_unlike, name='post_unlike'),
    path('api/', include(router.urls)),
    path('list/', views.post_api_view),
]

