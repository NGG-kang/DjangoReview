import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib import messages
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
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
            qs = Post.objects.all() \
                .filter(
                Q(author__in=request.user.following_set.all()) |
                Q(author=request.user)
            )
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


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        comment_list = Comment.objects.filter(post=kwargs.get('object'))
        comment_form = CommentForm()
        context = {
            'comment_list': comment_list,
            'form': comment_form
        }
        return super().get_context_data(**context)

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = super().get_object()
            comment.save()
            return redirect('instagram:post_detail', pk=kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk', '')

        if pk:
            comment = Comment.objects.get(pk=pk)
            if comment.author != request.user:
                messages.warning(request, message="작성자가 아닙니다")
                return

            self.object = self.get_object()
            initial_dict = {
                "comment": comment.comment,
                "author": comment.author,
                "post": comment.post,
            }
            form = CommentForm(request.POST or None, initial=initial_dict)
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context["comment_edit_form"] = form
            context["comment_pk"] = comment.pk
            return self.render_to_response(context)
            # return render(request, "instagram/form.html", {
            #     "comment_edit_form": comment_edit_form,
            #     "comment_message": comment.comment
            # })

        else:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('instagram:post_detail', pk=pk)

    else:
        comment_list = Comment.objects.filter(post=pk)
        comment_form = CommentForm()

    return render(request, 'instagram/post_detail.html', {
        'post': post,
        'form': comment_form,
        'comment_list': comment_list,
    })


def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user==post.author:
        messages.warning(request, "작성한 회원은 좋아요를 누를수 없습니다")
        return redirect('instagram:post_detail', pk=pk)
    post.like_user.add(request.user)
    messages.success(request, f"{post.author} 좋아요")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)


def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user.remove(request.user)
    messages.success(request, f"{post.author} 좋아요 취소")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)


def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('instagram:post_detail', pk=pk)


def comment_edit(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    form = CommentForm(request.POST or None,
                       instance=comment)
    if request.method == 'POST':
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.comment = request.POST.get("comment")
            comment_form.save()

    return redirect('instagram:post_detail', pk=pk)


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


post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
post_list = PostListView.as_view()
post_delete = PostDeleteView.as_view()

#######################################

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadonly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields=['message']
    ordering=['id']
    @action(detail=False, methods=['GET'])
    def message(self, request):
        qs = self.get_queryset().filter(message__startswith='1')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def message_set(self, request, pk):
        instance = self.get_object()
        instance.message = '바뀜'
        instance.save(update_fields=['message'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
# @api_view(['GET'])
# def post_api_view2(request):
#     qs = Post.objects.all()
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name='instagram/mypost.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostSerializer(post).data
        })