# HTTP 상태 코드

웹 서버는 적절한 상태코드로서 응답해야한다

각 HttpResponse 클래스마다 고유한 status_code가 할당된다 ([코드)]([django/response.py at master · django/django · GitHub](https://github.com/django/django/blob/master/django/http/response.py))

REST API를 만들 때 특히 유용



### 대표적인 상태 코드

#### 200번대 : 성공

​	200 : 서버가 요청을 잘 처리함 / HttpResponse, render, JsonResponse
​	201 : 작성됨. 서버가 요청을 접수하고, 새 리소스를 작성했다

#### 300번대 : 요청을 마치기 위해, 추가 조치가 필요하다.

​	301 : 영구 이동, 요청한 페이지가 새 위치로 영구적으로 이동했다.
​	302 : 임시 이동, 페이지가 현재 다른 위치에서 요청에 응답하고 있지만, 요청자는 향후 원래 위치를 계속 사용해야 한다. /  HttpResponseRedirect, redirect

#### 400번대 : 클라이언트 측 오류

​	400 : 잘못된 요청.
​	401 : 권한 없음 (인증 못함)
​	403(Forbidden) : 필요한 권한을 가지고 있지 않아서, 요청을 거부 (인증을 했으나 뷰나 url의 권한이 없음)
​	404 : 서버에서 요청한 리소스를 찾을 수 없다. / get_object_or_404, raise Http404(django.http에 있음)
​	405 : 허용되지 않는 방법. POST 방식만을 지원하는 뷰에 GET 요청을 할 경우

#### 500번대 : 서버측 오류

​	500 : 서버 내부 오류 발생

​	뷰에서 요청 처리 중에 뷰에서 미처 잡지못한 오류가 발생한 경우



## 다양한 HttpResponse 서브 클래스

지정 상태코드 응답이 필요할 때

직접 사용할 일은 별로 없는데 django에서 만들어둔 상태코드들

HttpResponseRedirect : 상태코드 302

HttpResponsePermanentRedirect : 상태코드 301 (영구이동)

HttpResponseNotModified : 상태코드 304

HttpResponseBadRequest : 상태코드 400

HttpResponseNotFound : 상태코드 404

HttpResponseForbieend : 상태코드 403

HttpResponseNotAllowed : 상태코드 405

HttpResponseGone : 상태코드 410

HttpResponseServerError : 상태코드 500