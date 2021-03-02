# Instagram 경과 페이지

## 2021-03-01

프로젝트 생성

`django-admin startproject cloncodding`



프로젝트 생성 후 instagram과 accounts 앱 2개를 만들어주었다

`python manage.py startapp instagram`

`python manage.py startapp accounts`

그리고 배운 바로썬 만들고 migrate를 한번 하는게 좋다고 해서

`python manage.py migrate`를 했다



`settings.py`의 `INSTALLED_APPS`에 instagram, accounts 추가

갑자기 static과 media 폴더도 `settings.py`에 지정하는걸 강의에 들어서 뜬금없이 추가 하긴 했다

`MEDIA_ROOT = os.path.join(BASE_DIR, 'media_fields/')`

`MEDIA_URL = '/media/'`

`STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')`

`STATIC_URL = '/static/'`

[django Setting](https://docs.djangoproject.com/en/3.1/ref/settings/#static-files)장고 settings 페이지를 확인해서 넣은거긴 한데 아직 작동하는지는 모른다

단 ROOT 에서는 실제 물리적 장소, URL은 주소로 입력 했을 시 파일 주소인건 알았다



그리고 instagram, accounts에 각각 `urls.py`추가하고, `urlpatterns=[]`를 추가 해 주었다

추가를 안하고 project의 `urls.py`에 include 하니까 urlpatterns가 없다고 나오더라



다음으로 accounts의 model에서 커스텀 유저 만들기를 도전했다

[settings auth](https://docs.djangoproject.com/en/3.1/ref/settings/#auth-user-model) 를 참조하여 AUTH_USER_MODEL의 default가 auth.User인걸 알았다

`settings.py`에 AUTH_USER_MODEL = 'accounts.User'를 넣고

accounts의 models.py에 아래와 같이 만들었다

```python
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, blank=True)
```

그렇게 하고 커스텀 User를 만들려고 하니 기존 migrate 때문에 에러가 나더라...

스택 오버 플로우에서 해결법을 찾았다

https://stackoverflow.com/questions/42794212/migrating-from-django-user-model-to-a-custom-user-model

settings.py의 AUTH_USER_MODEL 를 주석하고

기존 settings.py의 설치된 앱 주석하고, 기존 마이그레이션을 되돌리고

다시 커스텀 User를 되돌리니까 User가 설치가 되더라



커스텀 User를 하고 `python manage.py createsuperuser`를 했는데

커스텀 User 한것만 나오는게 아니라 기존에 있던거를 그대로 가져가되 커스텀 한것만 바뀌는걸 알았다. 

email을 blank를 안주니 슈퍼유저를 만들때도 이메일을 적으라고 하더라...

옵션들을 꼭 줘야 하는건 알았다



그리고 instagram App에 `models.py`에서 Post, Comment, Tag 모델을 만들었다

그러나 ForeignKey, ManyToManyField과 like_user는 어떻게 해야할지 너무 어렵더라

그래서 기존에 배우면서 만들었던 instgram의 model을 조금 참조 하여 만들었다

```python
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d")
    tag = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post_set")



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
```

솔직히 더 가다듬을 부분이 있긴 한데 나중에 하도록 하겠다