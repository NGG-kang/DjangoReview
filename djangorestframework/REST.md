# REST (Representational State Transfer)

[TOC]

아키텍처 스타일. 프로토콜에 독립적 -> 일반적인 REST 구현에서 HTTP를 사용



## RESTful API의 몇 가지 디자인 원칙

1. 리소스를 중심으로 디자인
2. 클라이언트에서 엑세스할 수 있는 모든 종류의 개체/서비스가 리소스에 포함
3. 리소스마다 해당 리소스를 고유하게 식별하는 식별자
4. 요청/응답 포맷으로 흔히 JSON을 사용
5. 균일한 인터페이스를 적용
   리소스에 표준 HTTP 동사(GET, POST, PUT, PATCH, DELETE)를 적용



## 리소스를 중심으로 API구성(예시)

/order/ 로의 POST 요청 				O

/create_order/  로의 POST 요청   X



/customers/ 고객 컬랙션

/customers/5/ pk가 5인 고객

/customers/5/orders/ 고객 5에 대한 모든 주문

/orders/99/customer/ 주문 99의 고객



**심플하게 URI을 구성하기**

/customers/1/orders/99/products/ 유연성이 떨어짐

/customers/1/orders/ 를 통해 고객 1의 모든 주문을 찾은 후에

/orders/99/products/ 로 변경해서 동일한 처리



## HTTP 메서드를 기준으로 기본 작업 정의

GET : 리소스의 표현, 응답 본문에 리소스의 세부 정보

POST : 새 리소스 생성 요청, 본문에 새 리소스 세부 정보를 제공 -> 멱등성 미보장

PUT : 기존 리소스를 대체, 요청 본문에 갱신할 리소스 정보를 제공 -> 반드시 **멱등성 보장**되어야

PATCH : 기존 리소스를 부분 대체. 요청 본문에 갱신할 리소스 정보를 제공 -> 멱등성 미보장

DELETE : 지정 리소스를 제거



| 리소스            | POST                      | GET                          | PUT                           | DELETE                    |
| ----------------- | ------------------------- | ---------------------------- | ----------------------------- | ------------------------- |
| /posts/           | 새 포스팅 만들기          | 모든 포스팅 목록             | 포스팅 대량 업데이트          | 모든 포스팅 삭제          |
| /posts/1/         | 오류                      | 포스팅 1에 대한 내용         | 포스팅 1의 정보 갱신          | 포스팅 1 삭제             |
| /posts/1/comments | 포스팅 1의 새 댓글 만들기 | 포스팅 1에 대한 든 댓글 목록 | 포스팅 1의 댓글 대량 업데이트 | 포스팅 1의 모든 댓글 삭제 |





## 요청/응답 형식 지정

요청 : Content-Type 헤더

ex) application/json, application/vnd.ms-excel, image/jpeg, application/pdf 등

요청시에 처리를 원하는 형식 지정하면, 서버에서는 이 형식으로 응답

서버에서 해당 형식을 지원하지 않으면 HTTP 상태 코드 415 (지원하지 않는 미디어 유형) 반환





## HTTP METHOD별 상태코드

GET
일반적으로 200 응답, 리소스 못 찾을 경우 404(Not Found)응답

POST

201(create)응답. 새 리소스의 URL은 응답의 Location 헤더에
새 리소스를 만들지 않은 경우, 200 응답하고 응답 본문에 포함할 수도. 반환할 결과가 없으면 204(내용없음) 반환할수도
잘못된 데이터로 요청하면 400(잘못된 요청) 응답하고 응답 본문에 오류정보 또는 자세한 정보를 제공하는 URI 링크 포함

PUT

기존 리소스를 업데이트할 경우 200 또는 204 반환. 상항에 따라 업데이트할 수 없는 경우 409(충돌) 반환

DELTE

성공하면, 응답 본문에 추가정보가 포함도지 않았음을 의미로 204 응답. 리소스가 없는 경우 404 응답

비동기 작업

작업 완료 시간이 오래 걸릴 경우, 다른 Task Queue를 통해 비동기 처리가 가능하다

이때 요청은 수락되었지만 아직 완료되기전을 나타내는 202(수락됨) 응답

클라이언트가 이 작업을 Polling(주기적으로 검사)을 통해 모니터링할 수 있도록, 비동기 요청의 상태를 반환하는 URI을 Location헤더로 반환



## django-rest-framework

Serializer/ModelSerializer를 통한 데이터 유효성 검증 및 데이터 직렬화

각종 Parser를 통한 데이터 처리

APIView/Generic/ViewSet/ModelViewSets를 통한 요청 처리

각종 Renderer를 통한 다양한 응답 포맷 지원

인증(Authentication)/권한(Permission)체계 - 써드파티를 통해 JWT 지원

Throttling(최대 호출 횟수 제한)





pip install djangorestframework



프로젝트 urls.py에 path('api-auth/', include('rest_framework.urls')) 추가

이 주소는 login, logout을 지원하는 주소이므로 추가하든 상관없음



serializer.py를 만들어서 form과 같이 만들면 된다

views는 ViewSet을 활용한다

url은 router를 통해  post, get을 만들어준다

```python
# serializer.py
from rest_framework.serializers import ModelSerializer
from .mdoels import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        
# views.py
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
# urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
```





## 다양한 HTTP 클라이언트 프로그램

javascript를 통한 호출

Android/iOS앱 코드를 통한 호출

웹 요청 개발 프로그램을 통한 호출
GUI 프로그램 : Postman
CLI 프로그램 : cURL, HTTPie
라이브러리 : requests



HTTPie

pip install httpie

`http https://www.naver.com` 처럼 http로 시작

현재 프로젝트 에서는 `http http://127.0.0.1:8000/instagram/api/post/`



**HTTPie 명령 예시**

http GET 주소 GET인자명==값 GET인자명==값

http --json POST 주소 GET인자명==값 GET인자명==값 POST인자명=값 POST인자명=값
application/json 

http --form POST 주소 GET인자명==값 GET인자명==값 POST인자명=값 POST인자명=값
multipart/form-data

http PUT 주소 GET인자명==값 GET인자명==값 PUT인자명=값 PUT인자명=값

http DELETE 주소 GET인자명==값 GET인자명==값



지금 내가 만들어둔 모델같은 경우는 author가 필수라서 

`http POST http://127.0.0.1:8000/instagram/api/post/ author=1 message=1244`
이렇게 써서 POST 요청을 했다





## 직렬화 (Serialization)

모든 프로그래밍 언어의 통신에서 데이터는 필히 문자열로 표현되어야만 한다
송신자 : 객체를 문자열로 변환하여 데이터 전송 -> 직렬화
수신자 : 수신한 문자열을 다시 객체로 변환하여, 활용 -> 비직렬화

각 언어에서 모두 지원하는 직렬화 포맷(JSON, XML등)도 있고,

특정 언어에서만 지원하는 직렬화 포맷(파이썬은 Pickle)이 있다



django타입 Model, QuerySet등 에 대해서는 직렬화 룰이 없다

1. 직접 변환

   ```
   data = [ {'id': post.id, 'title': post.title}
   		for post in Post.objects.all()]
   json.dumps(data, cls=DjangoJSONEncoder, ensure_ascii=False)
   ```

2. 커스텀 룰

   DjangoJsonEncoder를 사용

   DRF에서도 커스텀 JSON Encoder를 사용한다

3. rest_framework.renderer.JSONRender를 통한 직렬화

   1. 장고의 DjnagoJSONEncoder를 상속 받지 않고, json.JSONEncoder 상속을 통해 구현
      Model타입은 미지원 -> ModelSerializer를 통한 변환

   2. JSONRenderer
      json.dubmps에 대한 래핑 클래스 -> 보다 편한 직렬화 지원(Model 변환 룰은 없음)

   3. ModelSerializer를 통한 JSON 직렬화

      Serializer/ModelSerializer은 Form/ModelForm과 유사

      역할 면에서 Serializer는 POST 요청만 처리하는  Form



**ReturnDict 타입**

serializer.data의 데이터 타입

OrderDict을 상속 받았으며, serializer를 키워드 인자로 받는다

```python
post = Post.objects.first()
serializer = PostModelSerializer(post)
serializer.data
# (한개 반환)

post = Post.objects.all()
serializer = PostModelSerializer(post, many=True)
serializer.data
# (다수 반환 쓸 시 many=True 사용 해야함)

```

json.dumps(serializer.data) 또는

JSONRenderer().render(serialzer.data)로 JSON 직렬화



**장고 기본 View에서의 HttpResponse JSON 응답**

모든 View는 HttpResponse 타입의 응답을 해야만 한다

1. 직접 json.dumps를 통해 직렬화된 문자열을 획득하여 HttpResponse를 통해 응답
2. 1번을 정리하여 JsonResponse 지원 -> 내부적으로 json.dumps를 사용하여 DJangoJSONEncoder가 디폴트 지정



**JsonResponse**

JsonResponse는 여러 인자를 가지는데

JsonResponse(data, encoder, safe, json_dumps_params, **kwargs)

**data**는 말 그대로 직렬화 할 데이터

**encoder**는 Serializer를 넣으면 되고

**safe**는 dict 객체만 직렬화 할수 있는지 여부를 제어, 기본값 참

**json_dumps_params**는 예시로 `json_dumps_params={'ensure_ascii': False}`데이터 변환값 이라고 생각하면 될까? 이걸 지정하면 아스키코드로 변환을 안한다

**\*\*kwargs**같은 경우는 뭐 당연히 값들 필요하면 넣는 용도로 쓰는 거겠지?





## DRF를 통한 httpResponse JSON 응답

```
qs = Post.objects.all()
serializer = PostModelSerializer(qs, many=True)

from  rest_framework.response import Response
response = Response(serializer.data)  # Conetent-Type: text/html 디폴트 지정
```

Response에서는 JSON 직렬화가 Lazy하게 동작한다

실제 응답 생성시에 .rendered_content 속성에 접근하며, 이때 변환이 이뤄진다



**Response와 APIView**

DRF의 모든 뷰는 APIView를 상속받는다

APIView를 통해 Response에 다양한 속성이 지정된다



**간결하게 사용**

리스트만 볼 시 아래와 같이 사용할 수 있다.

```python
from rest_framework import generics

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
post_list = PostListAPIView.as_view()
```





**포스팅 조회 응답에 username 응답 하기**

1. serializer의 ReadOnylField 사용

author = FK 필드가 있을 때, Serializer 에서는 FK 키값으로 응답

serializer.ReadOnylField를 통해 FK의 필드값을 읽어올 수 있다

```python
class PostSerializer(serializer.ModelSerialzer):
    username = serializers.ReadOnylField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['pk', 'username', 'title', 'content']
```

2. 중첩된 Serializer를 통해서도 구현 가능

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']
   
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = '__all__'
```





## DRF의 기본 CBV인 APIView

하나의 CBV이므로 하나의 URL만 처리 가능

각 method(get,post,put,delete)에 맞게 멤버함수를 구현하면, 해당 method 요청이 들어올 때 호출

1. 직렬화/비직렬화 처리(JSON 등)
2. 인증 체크
3. 사용량 제한 체크 : 호출 허용량 범위인지 체크
4. 권한 클래스 지정
5. 요청된 API버전 문자열을 탐지하여 request,version에 저장



APIView 클래스 혹은 @api_view 장식자

View에 여러 기본 속성을 부여

1. renderer_classes : 직렬화 class 다수
2. parser_classes : 비직렬화 class 다수
3. authentication_classes : 인증 class 다수
4. throttle_classes : 사용량 제한 class 다수
5. permission_classes : 권한 class 다수
6. content_negotiation_class : 요청에 따라 적절한 직렬화/비직렬화 class를 선택하는 class
   ex) JSON응답을 교구하는지 / HTML응답을 요구하는지 판단
7. metadata_class : 메타 정보를 처리하는 class
8. versioning_class : 요청에서 API버전 정보를 탐지하는 class



1. APIView : 클래스 기반 뷰
   def get: / def post:
2. @api_view : 함수 기반 뷰를 위한 장식자
   @api_view(['GET', 'POST'])



## DRF에서 지원하는 mixins

CreateModelMixin

ListModelMixin

RetrieveModelMixin

UpdateModelMixin

DestoryModelMixin

등등이 mixin들이 있다



```python
class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generic.GenericAPIView):
    queryset = Post.objects.all()
	serializer_class = PostModelSerializer
    
    def get(self, request, *args, **kwargs):
        retrun self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        retrun self.create(request, *args, **kwargs)
```

이렇게 mixins를 사용해서 만들려고 하면 번거롭다

그래서 정리 한게

APIView -> mixins -> Generics -> Viewset 

이렇게 정리되어진다

generics.ListCreateAPIView와 같은 generics를 사용하면 자동으로 get, post와 같은 것들이 구현되어 있으므로

아주 get, post는 생략하고 queryset과 serializer_class만 적용하면 된다





## ViewSet

 단일 리소스에서 관련있는 View들을 단일 클래스에서 제공

list/create/    detail/update/partial_update/delete : 2개의 URL이 필요



2가지 ModelViewSet

viewsets.ReadOnlyModelViewSet
	list 지원 -> 1개의 URL
	detail지원 -> 1개의 URL

viewsets.ModelViewSet
	list/create지원 -> 1개의 URL
	detail/update/partial_update/delete 지원 -> 1개의  URL



```python
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
post_list = PostViewSet.as_view({
    'get': 'list'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve'
})
# 이렇게 개별 View를 만들 수도 있고 (url 따로 줘야함)

router = DefaultRouter()
router.register('post', views.PostViewSet)
urlpatterns=[
    path('', include(router.urls)) # 이렇게 한번에 넣을 수도 있다
]								   # 이 기능은 format을 지원한다(주소에 .json, .api 쓸수있음)
```





### ViewSet에 새로운 EndPoint 추가하기

```python
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=False, method=['GET'])
    def public(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
```

만약 이렇게 구현한다면 post/public 이라는 주소가 생긴다





##  Renderer를 통한 다양한 응답포맷

같은 Endpoint에서 용창받은 타입에 맞춰, 다양한 응답포맷을 지원

Content-Type, URL의 방법을 통해 Renderer지정 가능

**JSONRenderer(디폴트) : json.dump/s를 통한 JSON 직렬화**
media_type : application/json, format: json
OOO.json / ?format=json / Accept:application/json(httpie에서 가능)

**BrowsalbeAPIRenderer(디폴트) : self-document HTML 렌더링**
media_type : text/html, format: api
OOO.api / ?format=api / Accept:text/html(httpie에서 가능)

**TemplateHTMLRenderer: 지정 템플릿을 통한 렌더링**
media_type : text/html, format: api
Response에서 template_name 인자 지정 필요
API서버라고 해서 모든 응답을 JSON으로 받지 않아도. 경우에 따라서 HTML응답을 받을수도

템플릿을 통해 Render를 수행하기에 별도의 Serializer가 불필요

**그외**

StaticHTMLRenderer

AdminRenderer 등등...

**서드파티 Renderer**

drf-renderer-xlsx

yaml, xml, jsonp, cvs 등등이 있다



### Renderer클래스 리스트 지정하기

전역지정
settings -> REST_FRAMEWORK -> DEFAULT_RENDERER_CLASSES 리스트에 문자열로 지정

APIView마다 지정
queryset_serializer_class와 더불어 , renderer_classes 리스트

@api_view마다 지정
renderer_classes 장식자
함수부분에 `def aa(request, foramt=None)`처럼 format을 줘야한다
그리고 urlpatterns에는 직접 포맷별로 만들거나 아래와 같이 쓰면 자동으로 format별로 만들어준다

```python
from rest_framework.urlpatterns improt format_suffix_patters

urlpatterns=format_suffix_patterns([
    path('hello/', views.hello)
])
```





이러한 설정은 깃헙 rest-framework/settings에 있다





## Serializer를 통한 유효성 검사 및 저장

Serializer는 Django Form과 컨셉, 사용법이 유사하나 생성자의 차이가 있다

form : data, files, instance

serailizer : instance, data

순서도 다름

**data=인자가 주어지면**

is_valid()가 호출되어야

1. initail_data필드에 접근 가능
2. .validated_data를 통해 유효성 검증에 통과한 값들이 .save()시에 사용된다
3. .errors 유효성 검증 수행 후에 오류내역
4. .data 유효성 검증 후에 갱신된 인스턴스에 대한 필드값 사전

serializer.save(**kwargs)호출할때

1. DB에 저장한 관련 instance를 리턴
2. .validated_data와 kwargs사전을 합친 데이터를
   1. update함수/ create함수를 통해 관련필드에 값을 할당하고, DB로의 저장을 시도
   2. update() : self.instance 인자를 지정했을 때
   3. .create() : self.instance 인자를 지정하지 않았을 때



**from rest_framework.validators.import ...**

값에 대한 유효성 검사를 수행하는 호출 가능한 객체

DRF에서는 유일성 체크를 도와주는 Validators 제공

1. UniqueValidator : 지정 1개 필드가 지정 QuerySet 범위에서의 유일성 여부체크

   모델 필드에 unique=True를 지정하면 자동 지정

2. UniqueTogetherValidator : UniqueValidtor 의 다수 필드 버전

3. BaseUniqueForValidator

4. UniqueForDateValidator : 지정 날짜 범위에서 유일성 여부 체크

5. UniqueForMonthValidator : 지정 월 범위에서 유일성 여부 체크

6. UniqueForYearValidator : 지정 년 범위에서 유일성 여부 체크



**유효성 검사에 실패하면 ValidationError 예외 발생**

필히 rest_framework.exceptions.ValidationError 사용

장고 기본에서는 django.forms.exceptions.ValidationError



**Serializer에의 유효성 검사**

필드 정의시에 validattors 지정하거나 클래스 Meta.validators지정

Field Level 검사 : 유효성 검사 및 값 반환

`def validate_title(self, value):`

Object Level 검사 : 유효성 검사 및 값 반환

`def validate(self, data)`



**DB로의 반영과 Mixins의 perform_ 계열 함수**

APIView의 create/update/destory 멤버 함수에서 실질적인 DB처리 로직은

**perform_**create(serailizer)/**percorm_**update(serializer)/**perform_**destory(instance)를 통해 이루어진다

```python
def perform_create(self, serializer):
    author = self.reqeust.user
    serializer.save(author=author)
```



## Authentication, Permission 인증, 권한

Authentication : 유저식별

permission : 각 요쳉에 대한 허용/거부

Throttling : 일정 기간동안 허용할 최대 호출 횟수



**인증 처리 순서**

1. 매 요청시마다 APIView의 dispatch 호출
2. APIView의 initial호출
3. APIView의 perform_authentication 호출
4. request의 user 속성 호출
5. request의 _authenticate()호출



**인증 종류**

SessionAuthentication : 세션을 통한 인증, APIView에서 디폴트

BasicAuthentication : Basic인증 헤더를 통한 인증 (Authorization: Basic \~~~~~~~~~ )

TokenAuthentication : Token헤더를 통한 인증( Basic 인증과 비슷함 )

RemoteUserAuthentication : user가 다른 서비스에서 관리될때, Remote 인증, Remote-User 헤더를 통한 인증 수행



**django기본앱을 통한 login logout지원**



개체에 대한 접근을 허용하기 위해서, 인증/식별만으로는 충분하지 않다
추가로 각 개체에 대한 허가가 필요하다



**DRF의 Permission 시스템**
현재 요청에 대한 허용/거부를 결정, APIView단위로 지정 가능

IsAllow : 인증 여부에 상관없이 뷰 허용(디폴트)

IsAuthenticated : 인증된 요쳉에 한해서, 뷰 호출 허용

IsAdminUser : Staff인증 요청에 한해서, 뷰 호출 허용

isAuthenticatedOrReadOnly : 비인증 요청에게는 읽기 권한 허용

DjangoModelPermissions : 인증된 요청에 한해 뷰 호출을 허용하고, 추가 장고모델단위 Permission체크

DjangoModelPermissionsOrAnonReadOnly :
djangomodelpermissions와 유사하나, 비인증 요청에게는 읽기만 허용

DjangoObjectPermissions : 비인증 요청은 거부하고, 인증된 요청은 Object에 대한 권한 체크 수행



인증 사용 예시

```python
# views.py
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
# 또는 디폴트 지정
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSED': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}
```



**커스텀 Permission**

모든 Permission 클래스는 다음 2가지 함수를 선택적으로 구현

has_permission(request,view) : APIView 접근시 체크, 
거의 모든 Permission 클래스에서 구현하며, 로직에 따라 True/False 반환

has_object_permission(request, view, obj) : APIView의 get_object 함수를 통해 object 획득시에 체크
브라우저를 통한 API 접근에서 CRETAE/UPDATE Form 노출시에 체크
DjangoObjectPermissions에서 구현하며, 로직에 따라 True/Fasle 반환





## 필터링, 오더링

form 처럼 `def get_queryset(self):`을 쓴다

단 GET을 가져오는 방법은 `self.request.query_params.get('q', '')` 이렇게 query_params를 써야 한다



Django Admin의 search 기능과 유사한 기능제공
별도의 검색엔진을 사용하는 것이 아니라 DBMS의 조건절 활용

```
filter_backends = [SearchFilter, OrderingFilter]
search_field=['message'] # ?search=       	미지정 시에 serializer에 지정된 필드들 전부
ordering_fields=['id']	 # ?ordering=
ordering=['id']			 # 디폴트 정렬을 지정
```

주소 예시

`http://127.0.0.1:8000/instagram/post/?search=3`



문자열 패턴 지정( search_filed 안에 넣는 패턴들임)

"^" : starts with search

"=": Exact matches

"@": Full-text search (단어 구문에 대한 검색, 지원 하는 DB가 따로 있으므로 확인 요망)

"$": Regex search

get_search_fields 함수로도 구현 가능



## Pagination

**PageNumberPagination**

page/ page_size 인자를 통한 페이징 처리

page_size 미지정 상황을 위해 디폴트 지정이 필요



**LimitOffsetPagination**

offset/limit 인자를 통한 페이징 처리





전역설정

```python
# settings.py
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}
```



 

## Throttling(최대 호출 횟수 제한하기)

Rate: 지정기간내에 허용할 최대 호출 횟수

Scope : 각 Rate에 대한 별칭

Throttle : 특정 조건 하에 최대 호출 횟수를 결정하는 로직이 구현된 클래스



AnonRateThrottle
인증 요청에는 제한 없음, 비인증 요청에는 IP 단위로 횟수 제한

UserRateThrottle
인증 요청에는 유저 단위로 횟수제한, 비인증은 IP단위

ScopeRateThrottle
인증 요청에는 유저 단위로 횟수제한, 비인증은 IP단위
각 APIView 내 throttle_scope 설정을 읽어, APIView 별로 서로 다른 Scope를 적용

```python
# settings.py
# 디폴트 설정
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [],
    'DEFAULT_THROTTLE_RATES': {
        'anon': None,
        'user': None
    }
}

# 예시
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.thorttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '10/day',
    }
}

# ViewSet 예
from rest_framework.throttling import UserRateThrttle

class PostViewSet(ViewSet):
    throttle_classes = UserRateThrottle
```



**최대 호출 횟수 제한이 걸리면**

429 Too Many Requests 응답

예외 메세지에 API 활용이 가능한 시점을 알려줌
이는 Throttle의 wait 맴버함수를 통해 계산





**Cache**

매 요청시마다 cache에서 timestamp list를 get/set -> 캐시 성능이 중요



기본 settings의 디폴트 캐시 : 로컬 메모리 캐시 (로컬 메모리는 서버 재 시작시 초기화 된다)

데이터베이스 캐시, 파일 시스템 캐시, 로컬 메모리 캐시, 더미 캐시가 있다

그외로 redis를 활용한 캐시가 있음(django-redis-cache 사용)





Throttle별 캐시 설정

**Rates포맷**

포맷 : 숫자/간격

숫자 : 지정 간격 내의 최대 요청 제한 횟수

간격 : 지정 문자열의 첫 글자만 사용 "d", "day, "ddd"모두 Day
's' ,'m', 'h', 'd' 등



**Rates 제한 메커니즘**

SingleRateThrottle에서는 요청한 시간의timestamp를 list로 유지

매 요청시마다

1. cache에서 timestap list를 가져옴
2. 체크 범위 밖의 timestamp값들은 버림
3. timestamp list의 크기가 허용범위보다 클 경우, 요청을 거부
4. timestamp list의 크기가 허용범위보다 작을경우, 현재 timestamp를 list에 추가하고, cache에 다시 저장



**클라이언트 IP**

X-Forwarded-For 헤더와 REMOTE_ADDR 헤더를 참조해서 확정

우선순위 : X-Forwarded-For > REMOTE_ADDR 





## Token 인증 적용

초기에 username/paswword로 Token을 발급 받고

이 Token을 매 API요청에 담아서 보내어 인증을 처리

 settings.py 의 INSTALLED_APPS에 토큰 추가 필요

```
'rest_framework.authtoken',
```

세션, 베이직만되어있고 토큰이 없다, 토큰 설정 추가 필요

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication ',
    ],
}
```

SessionAuthentication : 세션을 통한 인증, APIView에서 디폴트

BasicAuthentication : Basic인증 헤더를 통한 인증 (Authorization: Basic \~~~~~~~~~ )

TokenAuthentication : 

**Token 모델**

User모델과 1:1

각 user별 토큰은 수동으로 생성

토큰은 유저별로 유일하며, 토큰만으로 인증을 수행



**ObtainAUthToken 뷰를 통한 획득 및 생성**

URL pattern 매핑이 필요하다

```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token)
]
```



**Signal을 통한 자동 생성**

시그널은 모델에서 세이브시 호출되는 일종의 콜백



**Management 명령을 통한 생성**

토큰 생성, 생성된 Token은 변경하지 않음

`python manage.py drf_create_token <username>`

강제로 토큰 재생성

`python manage.py drf_create_token -r <username>`





토큰 생성 예시

`http POST http://127.0.0.1:8000/accounts/api-token-auth/ username=kang password=kang`



파이썬 토큰 사용 예시

```python
import requests

TOKEN = '1d7e23073b4d263818b1807ce702211a73503f57'
headers = {
    'Authorization': f'Token {TOKEN}',
}
res = requests.get("http://localhost:8000/instagram/post/1", headers=headers)
print(res.json())
```





## JWT인증 

JSON Web Token 인증



Token인증과 JWT 인증



**DRF의 Token**

단순한 랜덤 문자열

각 유저와 1:1매칭

유효기간이 없다



**JWT**

데이터베이스를 조회하지 않아도, 로직만으로 인증이 가능

포맷 : "헤더.내용.서명"
서버에서 토큰 발급시에 비밀키로 서명을 하고, 발급시간을 저장
서명은 암호화가 아님, 누구라도 볼 수 있기에 보안성 데이터는 넣지 말고 최소한의 필요한 정보만 넣기

claim : 담는 정보의 한 조각. "key/value"형식

위변조 불가 (장고에서는 settings.SECRET_KEY를 활용하거나 별도로 JWT_SECRET_KEY 설정)

갱신(Refresh)매커니즘을 지원
유효 기간 내에 갱신하거나 username/password를 통해 인증

이미 발급된 Token을 폐기(Revoke)하는 것은 불가



Header를 base64 인코딩(헤더)

Payload를 base64 인코딩(내용)

Signature = Header/payload를 조합하고, 비밀키로 서명한 후, base64 인코딩(서명)



**Token은 안전한 장소에 보관하기**

스마트폰앱은 설치된 앱 별로 안전한 저장공간이 있으나

웹브라우저는 없음
웹 클라이언트는 세션 인증이 나은 선택일 수 있음. 단 장고/웹클라이언트가 같은 호스트 명을 가져야

통신은 필히 https로 지정



**djangorestframework-jwt**

설치

`pip install djangorestframework-jwt`

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}
    
# urls.py
urlpatterns=[    
    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),
]
```



HTTPie를 통한 JWT 발급

```
# terminal
http POST http://127.0.0.1:8000/api-jwt-auth/ username=kang password=kang

# test_tokey.py
import requests

JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImthbmciLCJleHAiOjE2MTU4OTU4OTgsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MTU4OTU1OTh9.tXGT-0pvML5ADkUAQj8E1meU_N11SDcwbddzlJW535E'

headers = {
    'Authorization': f'JWT {JWT_TOKEN}',
}
res = requests.get("http://localhost:8000/instagram/post/1", headers=headers)
print(res.json())
```



**JWT Token 유효기간이 지났다면**

JWT Tokne 유효기간 내에 갱신을 해야만 한다

유효기간 디폴트 5분

settings.JWT_AUTH의 JWT_EXPIRATION_DELTA 참조



**JWT Token 갱신받기**

Token 유효기간 내에만 가능

settings.JWT_AUTH의 JWT_ALLOW_REFRESH설정은 디폴트 False
True 설정에서만 갱신 지원. False인 경우에는 orig_iat 필드를 찾을 수 없다는 응답

```python
JWT_AUTH={
    'JWT_ALLOW_REFRESH': True,
}
```



JWT 주요 settings

JWT_SECRET_KEY

JWT_ALGORITHM

JWT_EXPIRATION_DELTA

JWT_ALLOW_REFRESH

JWT_REFRESH_EXPIRATION_DELTA

