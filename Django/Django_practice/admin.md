# Django Admin

[장고 어드민 문서](https://docs.djangoproject.com/ko/3.1/ref/contrib/admin/)



django.contrib.admin을 통해 admin 기능 제공

urls.py에서 임의의 주소로 변경해도 알아서 찾아간다 : **URL Reverse**



**django-admin-honeypot** 앱을 통해 가짜 어드민 페이지 노출 가능하다



#### 어드민 모델 등록

모델 클래스 등록을 통해, 조회/추가.수정/삭제 웹 UI를 제공한다

단 사용자가 추가 해야함



##### 등록법 1

가장 쉬운 버전

admin.site.register(model)



##### 등록법 2

클래스 활용

```python
class modelAdmin(admin.ModelAdmin):
    pass
admin.site.register(model, modelAdmin) #지정한 ModelAdmin으로 동작
```



##### 등록법 3

장식자 문법을 사용한다

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
```





#### admin 속성

##### `__str__`

Java의 toString처럼

python에는 다음과 같이 사용

```python
def __str__(self):
    return f"Post obejct ({self.id})"
```

model 출력시 `__str__`값이 나온다

##### list_display

모델 리스트에 출력할 컬럼 지정

1. `list_display = ['id', 'message']`
2. `list_display = '__all__'`

##### list_display_links

모델 리스트에 출력한 컬럼에서 링크 넣을 컬럼 지정

##### short_description

함수로 admin 딴에 넣고 싶은 내용을 넣었을 때

short_description을 통해 설명 내용을 바꿀수 있다

```python
    def message_length(self, post):
        return len(post.message)
    message_length.short_description = "메시지 글자수"
```

##### search_fields

admin내 검색UI를 통해, DB를 통한 where쿠리 대상 필드 리스트

`search_fields=['message']`

##### list_filter

지정 필드 값으로 필터링 옵션 제공

`list_filter = ['message'] `

