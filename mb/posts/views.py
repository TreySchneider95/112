from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, RedirectView, TemplateView, FormView
from .models import *


class PostListView(ListView):
    template_name = 'list.html'
    model = Post
    context_object_name = 'posts'