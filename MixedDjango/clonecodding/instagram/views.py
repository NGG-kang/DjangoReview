from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.contrib import messages
from . models import Post
from . forms import PostForm
# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅 저장')
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm



post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)