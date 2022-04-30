from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, RedirectView, TemplateView, FormView
from .models import *
from .forms import PostForm


class PostListView(ListView):
    template_name = 'list.html'
    model = Post
    context_object_name = 'posts'


class SinglePostView(DetailView):
    template_name = 'single_post.html'
    model = Post
    context_object_name = 'post'

class AddPostView(CreateView):
    template_name = 'new.html'
    model = Post
    form_class = PostForm