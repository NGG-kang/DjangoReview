# 관계형 필드

## ForeignKey

1:N 관계 models.ForeignKey

1:N 에서 N측에 ForeignKey 지정

1개의 포스트에 N개의 댓글



1:1 관계 models.OneToOneField

예) User와 Profile 관계 1:1



**M:N 관계 models.ManyToMany**

예) 1개의 포스팅에 다수의 태그 / 1개의 태그에는 다스의 포스팅



**ForeignKey(to, on_delete)**

to : 대상 모델 / 클래스를 직접 지정하거나, 클래스명을 문자열로 지정, 자기참조는 self

on_delete : Record 삭제시 Rule

CASCADE, PROTECT, SET_NULL, SET, DO_NOTHING

CASCADE만 왜래키로 참조하는 모델의 record도 삭제



**FK에서의 reverse_name**

reverse 접근시의 속성명: 디폴트 -> 모델명소문자_set

Post와 Comment가 있다면

post.comment_set.all()  === Comments.objects.filter(post=post)

filter를 걸지 않아도 _set으로 comment에 연결된 post를 가져올수있다



여러개의 앱에 같은 이름의 모델이 있으면 충돌이 발생한다

1. related_name = '+'를 사용하여 reverse_name을 포기하거나
2. 어느 한쪽 또는 모두의 FK의 reverse_name(related_name)을 변경



**limit_choices_to **

`limit_choices_to={'is_public': True}`

선택한 항목에서만 작성이 가능하게끔 제한을 걸어두는것



### 기타 User딴

`from django.contrib.auth.models import User`를 사용하여 models딴에 User를 가져올수 있으나

User는 바뀔 수 있으므로 이런 고정된 User를 사용은 비추천한다

그래서 `settings.py`에 AUTH_USER_MODEL = 'auth.User' 디폴트 값을 놓고

```python
from django.conf import settings
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

이렇게 settings의 값을 넣는것을 추천한다



## OneToOneField

Ex) User:Profile

ForeignKey(unique=True)와 유사하지만 reverse 차이

User:Profile을 FK로 지정한다면 profile.user_set.first() -> user

User:Profile을 O2O로 지정하면 -> profile.user -> user



OneToOneField(to, on_delete)

프로필 같은 경우는 보통 유저 생성시 같이 생성되도록 한다고 한다...



## ManyToManyField

M:N관계에서 어느쪽이라도 필드 지정가능

ManyToMany(to, blank=False)

M:N을 이어주는 중간 테이블이 필요하다

1. 방법

   ```python
   class Post():
       #...
   class Article():
       #...
   class Tag():
       post_set = models.ManyToManyField(Post)
       article_set = models.ManyToManyField(Article)
   ```

2. 방법

   ```python
   class Post():
       tag_set = models.ManyToManyField('Tag')
   class Article():
       tag_set = models.ManyToManyField('Tag')
   class Tag():
       name = models.CharField(max_length=50, unique=True)
   ```

   

   

## 기타

RDBMS지만, DB따라 NoSQL기능도 지원한다

ex)하나의 post안에 다수의 댓글 저장 가능

**djkoch/jsonfield**

대개의 DB엔진에서 사용가능

TextField/CharField를 래핑

dict등의 타입에 대한 저장을 직렬화하여 문자열로 저장

내부 필드에 대해 쿼리 불가

**django.contrib.postgres.fields.JSONField**

내부적으로 PostgreSQL의 jsonb타입

내부 필드에 대해 쿼리 지원