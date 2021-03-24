from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import UserForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, login
from .models import Profile, User
from instagram.models import Post






class LoginView(LoginView):
    model = get_user_model()
    template_name = 'accounts/login.html'


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserForm
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


class LogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user_id=request.user.pk)
    # post_list = Post.objects.get(pk=request.user.pk)
    post_list = Post.objects.all() \
                .filter(
                Q(author__in=request.user.following_set.all()) |
                Q(author=request.user)
    )

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'post_list': post_list,
    })

@login_required
def profile_edit(request):
    if request.POST:
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('accounts:profile')
    profile = Profile.objects.get(pk=request.user.pk)
    profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit_form.html', {
        'form': profile_form,
    })

@login_required
def follow_recommend(request):
    profile = get_object_or_404(Profile, user_id=request.user.pk)
    suggested_user_list = get_user_model().objects.all()\
            .exclude(pk=request.user.pk)\
            .exclude(pk__in=request.user.following_set.all())

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'suggested_user_list': suggested_user_list
    })

@login_required
def follower_list(request):
    profile = get_object_or_404(Profile, user_id=request.user.pk)
    follower_list = get_user_model().objects.all()\
            .exclude(pk=request.user.pk)\
            .filter(pk__in=request.user.following_set.all())

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'follower_list': follower_list
    })

def user_follow(request, username):
    follow_user = get_object_or_404(User, username=username, is_active=True)
    request.user.following_set.add(follow_user)
    follow_user.following_set.add(request.user)
    messages.success(request, f"{follow_user}님을 팔로우 했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

@login_required
def user_unfollow(request, username):
    unfollow_user = get_object_or_404(User, username=username, is_active=True)
    request.user.following_set.remove(unfollow_user)
    unfollow_user.following_set.remove(request.user)
    messages.success(request, f"{unfollow_user}님을 언팔로우 했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

class ProfileView(ListView):


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





login_view = LoginView.as_view()
logout_veiw = LogoutView.as_view()
