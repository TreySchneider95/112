# from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import PostListView, SinglePostView, AddPostView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<pk>', SinglePostView.as_view(), name='post_detail'),
    path('new/', AddPostView.as_view(), name='new_post'),
]