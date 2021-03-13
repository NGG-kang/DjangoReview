from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import UserForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model, login
from .models import Profile
from instagram.models import Post






class LoginView(LoginView):
    model = get_user_model()
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('instagram:post_list')


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('instagram:post_list')
    else:
        form = UserForm
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


class LogoutView(LogoutView):
    next_page = reverse_lazy('instagram:post_list')


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user_id=request.user.pk)
    # post_list = Post.objects.get(pk=request.user.pk)
    post_list = Post.objects.filter(author=request.user)

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'post_list': post_list,
    })

@login_required
def profile_edit(request):
    if request.POST:
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('profile/')
    profile = Profile.objects.get(pk=request.user.pk)
    profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit_form.html', {
        'form': profile_form,
    })



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



class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'




login_view = LoginView.as_view()
logout_veiw = LogoutView.as_view()
