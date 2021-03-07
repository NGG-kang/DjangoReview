# Messages Framework

from django.contrib import messages

* 현재 user를 위한 1회성 메세지를 담는 용도

ex)저장했습니다, 로그인했습니다

* HttpRequest 인스턴스를 통해 메시지를 남긴다
  즉 view에서만 사용 가능

* 메시지를 1회 노출되고 사라진다

* View를 통한 템플릿 시스템을 통해 노출을 하며, 템플릿 내에서 JavaScript를 통한 노출도 가능



## Message Levels를 통한 메시지 분류

* 파이썬 로깅 모듈의 level을 차용
* 레벨에 따라 로깅 여부 판단
  혹은 템플릿에서 다른 스타일로 노출
* 레벨 종류
  * DEBUG : 디폴트 설정으로 무시되는 레벨
    개발 관련된 메세지이며, 실 서비스는 무시
  * INFO : 해당 유저에 대한 정보성 메세지
  * SUCCESS : 액션이 성공적으로 수행되었음을 알림
  * WARNING : 실패가 아직 발생하진 않았지만, 임박
  * ERROR : 액션이 수행되지 않았거나, 다른 Failure가 발생



##  messages 소비

messages context_processors를 통해 messages 목록에 접근

.tags 속성을 통해 레벨을 제공

.message 속성을 통해 내용을 제공 (=  str(message))

소비를 하지 않으면 message가 계속 쌓인다

소비는 html 템플릿 태그로 소비

```html
{% if messages %}
	<ul class="messages">
        {% for message in messages %}
        	<li>
                	[{{ message.tags }} {{ message.message }}]
        	</li>
	</ul>
{% endif %}
```

```python
# views.py 예시
@login_required
def post_list(request):
    ...
    messages.info(request, 'message 테스트')
```



## 출력 tags 변경하기

```python
# settings.py
from django.contrib.messages import constans as messages_constants

MESSAGE_TAGS = {
    messages_constants.DEBUG: 'secondary',
    messages_constants.ERROR: 'danger',
}
```



## MESSAEG_LEVEL 변경하기

메세지 노출 최소 레벨

`settings.py`

`MESSAGE_LEVEL = messages_constants.DEBUG`추가



## django bootstrap4를 통한 messages

[django bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/templatetags.html?highlight=messages#bootstrap4.templatetags.bootstrap4.bootstrap_messages)

`{% bootstrap_messages %}`사용