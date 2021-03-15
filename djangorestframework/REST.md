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



