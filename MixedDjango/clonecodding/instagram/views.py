from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib import messages
from . models import Post
from . forms import PostForm
# Create your views here.





class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅 저장 완료')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅 수정 완료')
        return super().form_valid(form)


def post_delete(request, pk):
    model = Post
    messages.warning(request, '정말 삭제 하시겠습니까?')
    if request.method == 'POST':
        post = get_object_or_404(model, pk=pk)
        post.delete()
        messages.success(request, '포스팅 삭제 완료')
        return redirect('instagram:post_list')
    return render(request, 'instagram/post_delete.html', {

    })




post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
post_list = ListView.as_view(model = Post)
post_detail = DetailView.as_view(model=Post)