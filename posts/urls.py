from django.urls import path
from .apps import PostsConfig
from .views import (PostCreateAPIView, PostListAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDestroyAPIView,
                    CommentCreateAPIView, CommentListAPIView, CommentRetrieveAPIView, CommentUpdateAPIView,
                    CommentDestroyAPIView)

app_name = PostsConfig.name

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post_list'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_retrieve'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('posts/destroy/<int:pk>/', PostDestroyAPIView.as_view(), name='post_destroy'),

    path('comments/', CommentListAPIView.as_view(), name='comment_list'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comments/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment_retrieve'),
    path('comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('comments/destroy/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment_destroy'),
]
