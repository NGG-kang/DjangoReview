from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post', views.PostViewSet)


app_name = 'instagram'

urlpatterns = [
    path('post_create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    # re_path(r'^(?P<pk>[0-9]+)/comment_edit/(?P<comment_pk>[0-9]+)/$', views.comment_edit, name='comment_edit'),
    # path('<int:pk>/comment_edit/', views.comment_edit, name='comment_edit'),
    path('<int:pk>/post_update/', views.post_update, name='post_update'),
    path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/post_like/', views.post_like, name='post_like'),
    path('<int:pk>/post_unlike/', views.post_unlike, name='post_unlike'),
    path('', include(router.urls)),
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view())
]

