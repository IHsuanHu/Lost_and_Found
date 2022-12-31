from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", views.home, name='home_page'),
    path("lost_post_list/", PostListView.as_view(), name='lost_post_list'),
    path("lost_post_list/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("lost_post_list/<int:pk>/update/", PostUpdateView.as_view(), name='post_update'),
    path("lost_post_list/new/", PostCreateView.as_view(), name='post_create'),
    path("lost_post_list/<int:pk>/delete/", PostDeleteView.as_view(), name='post_delete'),
]
