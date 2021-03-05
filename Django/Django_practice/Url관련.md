# URL 관련 정리

[TOC]



## URL Dispatcher

특정 URL 패턴 -> view의 List

`settings.py`의 ROOT_URLCONF로 기본적으로 프로젝트로 정해져있음

최조의 urlpatterns로부터 include를 통해 Tree구조로 확장



HTTP 요청이 들오올 때마다, 등록된 urlpatterns 상의 매핑 리스트를 처음부터 순차적으로 훝으며 URL 매칭을 시도

​	매칭이 되는 URL Rule이 다수 존재하더라도, 처음 Rule만을 사용

​	매칭 안되면 404 Page Not Found



urlpatterns가 아닌 다른 이름으로 해도 include를 하여 하나의 리스트로 합치면 상관없음

## 간단하게 쓰는 법

```python
urlpatterns = [
    path('post_list/', views.post_list, name="post_list")
]
```

처음은 url, 두번쨰는 view 세번째는 name을 지정한다

url 리버스 기능을 사용시 name이 필요하다



### path(), re_path()

기본 지원되는 path converters를 통해 정규표현식 기입이 간소화

자주 사용하는 패턴을 converter로 등록하면 재활용면에서 편리 

#### path converters

IntConverter		r"[0-9]+"

StringConverter  r"[ ^/ ]+"

UUIDConverter   r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

SlugConverter (StroingConverter상속) r"[-a-zA-Z0-9_]+"

PathConverter (StroingConverter상속) r".+"

### 정규표현식

거의 모든 프로그래밍 언어에서 지원

문자열의 패턴, 규칙 Rule을 정의하는 방법

문자열 검색이나 치환작업을 간편하게 처리

장고 URL Dispatcher에서는 정규표현식을 통한 URL 매칭

정규 표현식은 띄어쓰기 하나에도 민감하다



**문법** : 1글자에 대한 패턴 + 연속된 출연횟수 지정 / 대괄호 내에 1글자에 대한 후보 글자들 나열

시작 : r"" 로 시작, 따옴표 안에 표현식 넣음

[0-9] 혹은 [\d] : 0부터 9까지 한번

[\D] : 숫자를 제외한 문자와 매치

[a-z] 소문자 a부터 z까지 한번

[A-Z] 대문자 A부터 Z까지 한번

[A-z] 대문자,소문자 A-z까지

[\s] 모든 공백과 매치

[\S] 공백을 제외한 문자와 매치
[\w] 모든 문자와 언더바

[\W] 일반 문자와 언더바를 제외한 문자(특문)과 매치

[\n] 줄넘김 문자

[\b] 단어와 단어 사이의 경계

[\B] 단어 사이의 경계가 아닌 것

[\t] tab문자



"+" 1번 이상

"*" 0번 이상

? 0번 또는 1번 : 

[.]  점은 \n 을 제외한 모든 문자열 한개 를 뜻함 : abc.ef -> "abc"와 "ef" 사이에 문자열 1개

\ 특수문자 예외처리

^ 문자열 시작 : ^www -> "www"로 시작하는 문자열

[^문자열] : 중괄호 안의 ^는 부정으로 쓰인다

$ 문자열 끝 : .com$ -> ".com"으로 끝나는 문자열

| OR연산 

( ) 묶음처리 " (naver|google)$" -> naver또는 google로 끝나는 문자열/
괄호로 묶인 부분은 하나의 덩어리로 취급해서 검색시 괄호 안에 해당되는 내영들을 그대로 가져다 이용할 수 있다.

{n} n만큼 반복

{n,} n개 이상만큼 반복

{n,m} n개이상 m개 이하





#### django 에서의 URL 정규표현식 매핑

`urls.py`라고 가정

```python
re_path(r'instagram/(?P<year>\d+)/')
```

r(raw)로 시작하여 이스케이프( \ ) 해석하지 않고 남겨두기 떄문에 정규표현식에 유용하다
r을 사용하지 않는다면 \d를 \ \d 로 2번씩 써야 한다

(?P<year\>) : year영역에 정규표현식 적용 (그룹하여 그룹명을 넘겨준다고 생각하면된다)

\d : \d+ 패턴에 부합되면

\<year> : year라는 변수명으로 view로 넘겨주겠다





#### django의 custom converter

```python
class YearConverter:
    regex = r'\d+'

    def to_python(self,value):
        return int(value)

    def to_url(self, value):
        return str(value)

from django.urls import path, re_path, register_converter

register_converter(YearConverter, 'year')
urlpatterns=[
    path('archives/<year:year>/', views),
    # re_path(r'archives/(?P<year>\d+)/',views),
]
```

클래스로 컨버터를 생성하여

to_python은 url이 매칭되었을 시, view 함수가 호출되기 전에 to_python을 먼저 겨쳐서 인자를 정리해 주는 역할

to_url은 url_reverse시 다시 문자열로 리버싱하는 역할

django의 register_converter(converter, 'name')으로 name을 정하여

urlpatterns에 \<year:year>로 값을 집어넣는다



한글 매칭은 slug converter를 사용하면된다



### 장고앱 생성시 추천작업

1. 앱 생성
2. 앱이름/urls.py 생성, urlpatterns=[] 생성
3. 프로젝트/urls.py에 include 적용
4. 프로젝트/settings.py의 INSTALLED_APPS에 앱이름 적용



```python
# 프로젝트/urls.py
from django.urls import include, path

urlpatterns = [
    path('앱이름/', include('앱이름.urls')),
]
```



## 

