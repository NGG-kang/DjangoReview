from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.urls import reverse
from django.contrib.auth import get_user_model

# 함수기반
# def post_list(request):
#     post_list = Post.objects.filter(author=request.user)
#
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': post_list
#     })
#
# def post_create(request):
#     form = PostForm(request.POST, request.FILES)
#     pass
#
# def post_modify(request, pk):
#     pass
#
# def post_delete(request, pk):
#     pass


class PostListView(ListView):


    # def get_queryset(self):
    # get_queryset의 다음에 페이지네이터가 구현되어 있어서 paginate_by를 쓸 수 있다
    #         if not self.request.user.is_anonymous:
    #             self.queryset = Post.objects.filter(author=self.request.user)
    #             if not self.queryset:
    #                 self.queryset = None
    #             return self.queryset
    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            qs = Post.objects.filter(author=request.user)
            if qs:
                paginator, page, queryset, is_paginated = super().paginate_queryset(qs, 9)
                context = {
                    'paginator': paginator,
                    'page': page,
                    'is_paginated': is_paginated,
                    'post_list': queryset,
                }
                return render(request, 'instagram/post_list.html', context)
        return render(request, 'instagram/post_list.html', {
            'post_list': None
        })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        print(form.cleaned_data)
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅 저장 완료')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(Post, pk=kwargs['pk'])
        if self.object.author != request.user:
            messages.warning(self.request, '작성한 회원만 수정할 수 있습니다')
            return redirect(self.object)
        form = PostForm
        return super(PostUpdateView, self).get(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.author == self.request.user:
            messages.success(self.request, '포스팅 수정 완료')
            form.save()
        else:
            messages.warning(self.request, '작성한 회원만 수정할 수 있습니다')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = 'instagram/post_list.html'

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(Post, pk=kwargs['pk'])
        if self.object.author != request.user:
            messages.warning(self.request, '작성한 회원만 삭제할수 있습니다')
            return redirect(self.object)
        return super(PostDeleteView, self).get(Post)

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(Post, pk=kwargs['pk'])
        if self.object.author != request.user:
            messages.warning(self.request, '작성한 회원만 삭제할수 있습니다')
            return redirect(self.object)
        self.object.delete()
        messages.success(request, '포스팅 삭제 완료')
        return redirect('instagram:post_list')




# 함수기반
# @login_required
# def post_delete(request, pk):
#     model = Post
#     post = get_object_or_404(model, pk=pk)
#     if post.author == request.user:
#         messages.warning(request, '정말 삭제 하시겠습니까?')
#         if request.method == 'POST':
#             post.delete()
#             messages.success(request, '포스팅 삭제 완료')
#             return redirect('instagram:post_list')
#     else:
#         messages.warning(request, '작성한 회원만 삭제할 수 있습니다')
#         return redirect(post)
#     return render(request, 'instagram/post_delete.html', {
#     })

#
post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
post_list = PostListView.as_view()
post_delete = PostDeleteView.as_view()
post_detail = DetailView.as_view(model=Post)

