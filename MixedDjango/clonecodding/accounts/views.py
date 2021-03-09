from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
# Create your views here.


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


login_view = LoginView.as_view()
logout_veiw = LogoutView.as_view()
