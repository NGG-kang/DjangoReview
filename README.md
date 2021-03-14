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





##### 2021-03-03

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



##### 2021-03-05

오늘 한 일

원래 원리부터 보는게 아니고
이러이러한게 있다, 이렇게 쓰면 이렇게 된다는걸 알고 원리를 파고들어야 하는데
자꾸 원리부터 파고들려고 하니까 시간이 너무 오래걸리는거같다...
이러면 안되는데 이렇게 시작해 버렸으니 그대로 이어가는게 맞을까...
또 고민된다
장고 모델 뷰 url 폼 만들고, rest framework로 api 개발 방법 검색이나 이런걸 해야 했었나...

아무튼 오늘은 django의 view에 대해서 조금 공부를 했다



내일 할 일

django의 static

django의 forms



##### 2021-03-06

오늘 한 일

django의 static, forms 아주 조금 했다

어제 늦게까지 안자고 버텼더니 후폭풍이 매우 커서 정신을 못차리겠다

그래서 forms 앞부분만 맛보기로 조금 공부했다

내일은 form을 끝내도록 노력해야지



내일 할 일

django form 더 공부하기

가능하면 다음 챕터인 django 인증 공부하기



##### 2021-03-07

오늘 한 일

django forms에 대해 다 본건 아니지먼 거의 끝까지 봤다

중간의 csrf_token이랑 messages가 껴있어서 왔다갔다 한 느낌이다

오늘도 열심히 놀았다



내일 할일

django form 마저 끝내기

django 인증 공부 끝내기



##### 2021-03-08

오늘 한 일

django form, django 인증 공부를 마무리 했다

그 뒤는 non-SPA 방식 instagram 개발, restframework, react, 배포만 남아있는데

일단 내가 먼저 혼자서 Non-SPA 방식으로 만들어보려고 했는데...

지금까지 공부해온게 뒤섞여서 어렵기도 하고 까먹어서 빈 공간에서 만들려고하니 너무 막막하다...

그래도 내가 해보면서 기억하는게 맞겠지?



 내일 할 일

바닥부터 django로 Non-SPA 웹페이지 만들기

그 뒤에도 공부를 다시 해볼까...? 아니면 웹페이지 만들까... 고민중



##### 2021-03-09

오늘 한 일

기존 모델까지 만들어놨던 MixedDjango 파일에 ModelForm을 활용한 

CRUD와 Login, Singup, Logout을 만들었다. 

중간중간 막히는 구간도 있었으나 검색하거나 또는 나의 실수로 이루어진 내용임을 찾아서 해결 했다

static을 추가하여 css를 추가중이긴 한데...

솔직히 매우 조잡한 화면이긴 하다

더 복잡하게 만들지, 또는 bootstrap css까지 마무리 하고 rest framework API 개발을 할 지 고민을 해야겠다

내일 할 일

bootstrap css로 화면 좀 꾸며주기

만족 할 만한 페이지 같으면 API 개발 공부 시작하자



##### 2021-03-10

오늘 한 일

기존 CRUD 방식에 validation이라고 해야하나 작성한 회원만 수정, 삭제할수 있게 바꿨다

FBV 방식으로 하면 request를 받는건 어렵지 않았는데 CBV로 받으려고 하니 어떻게 request를 받는지 잘 몰라서 한참을 해멨다

다시 코드를 돌아보니 다시 개선 할 코드가 보이는데 내일 또 시도해 봐야겠다

현재 ModelForm, CBV기반으로 만들었는데 FBV기반으로도 만들어도 괜찮을것 같다

또한 view의 filter를 적용하면서 django-debug-toolbar의 sql을 확인할 수 있는게 정말 많은 도움이 되었다

잘못된 쿼리를 바로 쉽게 확인할 수 있어서 바로 수정이 가능하니 참으로 편리한 디버그 툴임에 틀림없다

그리고 CBV 방식에서 어떻게 쿼리셋을 리턴해야할지 잘 몰랐는데

django github의 소스코드를 보며 따라가니 어느정도 길이 보이는것같다

css가 전부 적용되지 않았고, 이상하게 적용된 부분이 있다

css 적용하는 일은 너무나도 어려운것 같다. 그래도 어느정도 css에 맞춰주는건 계속 해야겠다



내일 할 일 

DeleteView 개선

FBV 방식으로 만들어보기?

css로 페이지 화면 개선



##### 2021-03-11

오늘 한 일

어제 했던 css를 대충이나마 마무리를 했다

그리고 instagram앱에 get 방식으로 queryset과 paginator를 적용 할 수 있게 했다

queryset 방식으로 통일 하려다가 리턴값을 주는데 제약사항(queryset을 빈 오브젝트로 반환하는 방법을 모름)이 생겨서 get방식으로 통일했다

그리고 본격적으로 instagram을 보면서 기능을 그대로 따라 하려는 생각을 하고 instgram app의 model을 수정했으나 makemigrations를 하려니 자꾸 custom User를 못받아오더라... 정말 화난다

기존 migration을 다 지우고, db도 지우고 했으나 계속 에러가 난다

너무 짜증나서 이정도만 하고 내일 고민 해야 겠다



내일 할 일

instagram app의 Model부분 고칠 방법 찾아내기

인스타 그램 앱 기능적인 부분을 구현하기



##### 2021-03-12

오늘 한 일

어제 못했던 Model부분 User 미인식 부분을 해결 했다

왜그런가 했더니 AutoOneToOneField라고 User 생성시 자동으로 Profile 생성하도록 django-boost라는 라이브러리를 설치했더니 User를 인식을 못하더라... 

github에서 그나마 업데이트를 한 라이브러리라 설치 후 시도를 한 거였는데  

이것때문에 원인 분석 DB, Migrations 다 삭제하고 하느라 2시간이 걸렸다

그리고 또 다른 라이브러리이고 업데이트가 멈춘 django-annoying의 AutoOneToOne 필드를 이용해봤더니 

아니나 다를까 이것은 동작하지 않는 필드다... 기본 OneToOneFiled랑 똑같이 작동한다...

Profile.save()나 create 둘 다 동작 하지 않고... 오전 내내 붙잡고 했더니 현타가 왔다...

오늘은 멘탈적인 부분으로 매우 심란한 상태로 더 이상 못 할거 같다

낮잠을 잤더니 더 우울해져서 오후에도 잡고 하지를 못했다

더 자서 내일 해봐야 겠다



내일 할 일

User 생성시Profile 같이 생성하도록 만들기

위의 것이 도저히 불가능 하다면 그냥 무시하고 instagram 기능들 만들기(글 좋아요, 댓글 CRUD, 팔로우, 팔로잉)



##### 2021-03-13

오늘 한 일

User 생성시 Profile이 자동 생성되도록 만들었다

하는 방법은 django-auto-one-to-one 라이브러리를 썼다

코드를 보니까 django의 basemodel과 signal을 사용해서 만드는거 같은데

django docs에서 singnal을 이해 못해서 솔직히 잘 모르겠더라...

하면 할수록 더욱 어려워지니 정말 힘들다...



메인 페이지를 로그인 페이지, 로그인시 프로파일로 까지 적용했다

하다보니까 css를 안 만지니 너무 못생긴 사이트가 되어서 css에 손을 대다가 포기했다

뭐 하나 건들면 전체가 움직여버리는게 정말 어려운 작업이 css가 아닌가 싶다...

프로필 자동생성, 프로필 수정까지만 만들었으니 내일은 좋아요, 댓글, 팔로우, 팔로잉 후딱 만들어야겠다

css는 좀 뒷전으로 미루자!



내일 할 일

댓글 CRUD
팔로우, 팔로잉(추천친구 까지?)
글 좋아요



##### 2020-03-14

오늘 한 일

팔로우, 팔로잉
글 좋아요, 취소
댓글 CR까지 만들었다

하다보니 자꾸 기존에 동영상 강의로 배웠던 코드를 참조해서 하게 되어버렸는데 내일 다시 코드 보면서 어떻게 돌아가는지 다시 확인 하고, 기억 해야겠다

그리고 post_list에 좋아요 한 유저 글 목록까지 보여주게 하려고 했는데 왠지 모르게 sql문에서는 본인의 것만 가져온다... 내일 다시 확인 해봐야 할듯



내일 할 일

post_list 좋아요 한 유저 것도 같이 가져오도록 하기

댓글 수정, 삭제를 구현 해야할까...?

django-rest-framework 슬슬 공부 시작 해야할듯