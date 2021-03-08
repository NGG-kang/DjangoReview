# 장고 인증

## 로그인

`settings.py`장고의 기본 Login url

LOGIN_URL = '/accounts/login/'

기본 LoginView에서의 로그인 템플릿
registration/login.html

LoginView에 `template_name='accounts/login.html'`를 넣어서 템플릿을 바꿀수 있다





```python
# django.contrib.auth / urls.py
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

```

login, logout, password_change, reset이 django딴에서 이미 구현되어있다

활용하는게 편하고 좋은 방법



## 프로필 페이지 구현



user : 

	- 로그인 : user
	- 비로그인 : AnonumousUser

{{ user }}는 settings.py의 templates의 options에서 auth가 구현되어있다

고로 로그인 유저를 언제든 가져올수 있음



간단한 프로필뷰 구현

```python
# FBV
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# CBV
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
profile = ProfileView.as_view()
```

프로필 페이지 구현시 유저가 생성될 때 같이 만들거나

아니면 프로필을 볼 때 없으면(에러시) 프로필을 None으로 만들어서 새롭게 만들도록 한다

