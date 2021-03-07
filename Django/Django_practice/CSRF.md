# CSRF

Cross Site Reuqest Forgery

사용자가 의도하지 않게 게시판에 글을 작성하거나, 쇼핑을 하게 하는 등의 공격

특정 웹사이트가 유저의 웹브라우저를 신용하는 상태를 노린것



**공격을 막기 위해 Token을 통한 체크**

Post 요청을 받을 때 Token값이 없거나 유효하지 않는다면, 403Forbidden 응답



**처리순서**

1. 입력 Form을 보여줄 때, CSRF Token값도 값이 할당
   CSRF Token은 User마다 다르며, 계속 변경됩니다.
2. 그 입력 Form을 통해 Token값이 전달되면, Token유효성 검증



Template tag로  {% csrf_token %} 을 쓰면 된다

장고 프로젝트 기본 세팅으로 CsrfViewMiddleware가 적용되어있다



**주의사항**

CSRF Token != 유저인증 Token

CSRF Token !+ JWT(Json Web Token)

CSRF Token은 현재 요청이 유효한지의 대한 토큰이다



**가급적이면 끄지 않는다**

기본 제공되는 보안기능이며, 이를 유지하는데 비용이 거의 들지 않는다

특정 View에 한에, CSRF Token 체크에서 배제하려면

해당 뷰에 @csrf_exempt 장식자를 적용



**앱 API에서는 꺼준다**

django-rest-framework의 APIView에서는 csrf_exempt가 적용되어있음

앱에서는 별개의 인증이 있다.





