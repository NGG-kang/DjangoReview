# DjangoReview

[TOC]

### 개요

이 페이지는 github django 페이지의 코드들을 파헤쳐서 학습 한 내용과

강의 내용을 정리할 내용들의 메인 페이지 입니다

주관적인 의견이나 생각이 있으며, 정확하지 않을 수 있습니다.


2021/02/27을 기점으로 시작한 페이지 입니다

추가되지 않은 내용들이 많을 수 있습니다

Django 3.1 을 토대로 작성하는 페이지 입니다



강의 정리 폴더 : Django/Django_practice/~

강의 정리 페이지는 코드 파헤치기와 연계하여 연습한 코드도 포함 되어 있습니다



코드 정리 폴더 : Django/~

django github 의 코드들을 나름대로 정리 한 페이지 입니다



파일 정리 폴더 : Django/files/~

django 프로젝트, 앱 생성시 만들어지는 파일들을 참조 페이지를 토대로 공부하는 페이지 입니다

참초 : [djangoGithub](https://github.com/django/django) , [djangoDoc](https://docs.djangoproject.com/ko/3.1/)

강의 : [Educast Ask Company](https://educast.com/course/web-dev/ZU53)

---

####  나름대로의 우선순위(django 코드 파헤치기)

차례대로 정리 할 예정입니다.



1. MVC에서의 models.py, views.py, urls.py 먼저 간단하게 정리, 최소한의 코드로 돌아가게 하려면 어떻게 넣어야 하나 정리, 그러면서 하나하나 추가
2. models 만들 시 django models 파일들 보기, 제약조건 어떻게 넣는지, 등등
3. views의 from view, function view, class view 등 찾아보면서 깃헙 코드들 살펴보기
4. views에서 return하는 방법이 무엇인지 (http 파일 참조), render 
5. urls의 urlpatterns가 어디서 나오는지, 정규 표현식 url reverse가 무엇인지
6. User 인증, user는 어디에서 가져오나, user
7. decorator 장식자 문법들 어디에 적용되고 어떤것들이 있는지 파헤쳐보자
8. template 문법들, static 파일들로 css 적용하는 방법
9. settings파일, 무엇이 있고, 기본적인 분야에 어떻게 적용 할 수 있는지(static, media 등)
10. test 파일을 작성 하려면 어떻게 해야 할 지
11. django github에  middleware, template, templatetag폴더들이 어떤 일을 하는지 알아보기
12. 장고 보안에 관련하여 알아보기
13. 그 외에 django github에 보지 못했던 코드들이 있나 확인하기

---

#### 일일 회고록 

##### 2021-02-27 

**회고**

models의 fields에 쓰이는 options를 정리 해봤다

솔직히 외우거나 꼭 필요한 거는 없었고 validator로 따로 함수로 만들어서 제약조건을 넣는 정도만 알아도 충분하다 싶었다 내일은 조금더 많이 공부해야지

**오늘 한 일**

1. first commit
2. django github의 django 폴더들 임시 생성
3. 메인 README.md 파일에 우선순위 정리
4. Django/fiels/models.md 모델 옵션 추가

**내일 할 일**

1. 자동 기본 키 필드 
2. ~~다양한 필드들~~
3. ~~관계~~
4. ~~Meta 옵션~~



##### 2021-02-28

**회고**

[django의 설계 철학](https://docs.djangoproject.com/ko/3.1/misc/design-philosophies/#views)

Fiedl API reference

django Docs에 내용들을 읽어가면서 정리를 하려고 하니까 과연 이렇게 하는게 맞는것인지 회의감이 들었다. 얼마 안하는데도 솔직히 시작부터 너무 이론적으로 파고들려고 하지 않았나 싶다...

솔직히 정말로 돌아가는지도 확인 할 수가 없어서 직접 해봐가면서 하는게 좋을듯 하다

새로운 django 앱을 하나 만들어서 하나하나 공부하는거로 해야 할까?

django 강의 들으면서 공부와, 내가 앱 만들어가면서 공부를 한번 해 봐야 할 거 같다

그러면서 django 코드들 파서 뭐가 있는지도 확인도 하고 그렇게 진행을 해 봐야 할거같다



**오늘 한 일**

1. ~~다양한 필드들~~
2. ~~관계~~
3. ~~Meta 옵션~~
4. Model

**내일 할 일**

1. Model쪽 강의 들으면서 정리하기
2. 새로운 앱 만들어서 인스타그램? 클론코딩 해보기



##### 2021-03-01

새로운 앱 만들어서 인스타크램 UI만 보고 클론코딩을 시도 해보려고 했다

그러나 잊어버린게 많아서 자꾸만 기존에 만든 코드들을 들락날락 하더라...

반복이 중요하긴 하지만 이렇게 까먹어서야 가능 할까는 생각이 든다

변명이긴 한데 자신감이 떨어져서 놀고먹었다...



**오늘 한 일**

새로운 앱 만들어서 클론코딩 시도해봄



내일 할 일



##### 2021-03-02

오늘 한 일

**Askcompany 강의**찔끔 들었다 솔직히 공부 하기 많이 싫었는데 조금이라도 했다...

다른 사람들 열심히 사는데 왜 나는 열심히 안 살고 있는지 약간의 죄책감이 들었다

오늘보다는 더 나은 내일을 살아야겠다



내일 할 일

1. 강의 조금은 더 듣기
2. 공부의 동기를 조금 찾아보자





**2021-03-03**

오늘 한 일

Askcompany강의 한 단원 끝냈다, 이론적인 부분이라 하루에 끝낼수 있었던것 같다

코딩부분으로 들어가면 어떻게 정리를 할지 생각해봐야할듯



내일 할 일

Askcompany강의 계속 듣기

파이썬의 언팩 문법이란?



##### 2021-03-04

오늘 한 일

함수기반 뷰 잠깐 하고 정말 어렵다고 생각한 정규표현식을 공부 했다

생각보다 쉬웠다고 생각했으나 생각보다 어려웠던 정규 표현식

장고에 맞춰서 커스텀 정규 표현식도 잠깐 해봤다

금방 까먹을 내용이긴 한데 원래 너무 어렵게 생각해서 이걸 어떻게 해야하나 생각했던 내용이지만 

생각보다 쉽게 잘 풀려서 기분이 좋았다

마지막으로 파이썬의 패킹, 언패킹 문법을 살짝 공부 해 봤다

*로 이루어지는 패킹과 언패킹 쉬우면서도 어려운 내용이었다고 생각한다

지금은 별로 안 써서 기억에서 금방 잊혀질 것 같지만 자주 쓸 날이 오면 유용하게 사용 할 것 같다



내일 할 일

클래스 기반 뷰(양이 꽤나 많음)

url reverse

