# URL reverse

URL Reverse를 통해 유연하게 URL 생성

`urls.py` 변경만으로 각 뷰에 대한 URL이 변경되는 유연한 URL 시스템



## URL Reverse 혜택

개발자가 일일이 URL을 계산하지 않아도 된다

URL이 변경되더라고 URL Reverse가 변경된 URL을 추적한다

예를들어 admin/ 링크의 이름을 바꿔도 admin/ 뒤의 링크들은 자동으로 역 추적하여 바꿔줌

이것이 URL Reverse



### URL Reverse를 수행하는 4가지 함수 (1)

url 탬플릿 태그 
	내부적으로 reverse 함수를 사용
`	{% url "blog:post_detail" pk=10 %}`, `	{% url "blog:post_list" %}`

reverse 함수
	매칭 URL이 없으면 NoReverseMatch 예외 발생
	`reverse('blog:post_detail', args=[100])`
	`reverse('blog:post_detail', kwargs={'pk': 100})`

resolve_url 함수(reverse를 더 쓰기 쉽게 한것)
	매핑 URL이 없으면 "인자 문자열"을 그대로 리턴
	내무적으로 reverse 함수를 사용
	`resolve_url('blog:post_detail', 100)`
	`resolve_url('blog:post_detail', pk: 100})`
	`resolve_url('/blog/100/')`

redirect 함수
	매칭 URL이 없으면 "인자 문자열"을 그대로 URL로 사용
	내부적으로 resolve_url 함수를 사용
	`redirect('blog:post_detail', 100)`
	`redirect('blog:post_detail', pk: 100})`
	`redirect('/blog/100/')`

대충 'Appname:template_name' 이라고 생각하면 된다



from django.urls import reverse

from django.shortcuts import resolve_url



### 모델 객체에 대한 detail 주소 계산

위의 예시들과 같이 사용할 수 있으나

아래와 같이 사용할 수도 있다

resolve_url(post)

redirect(post)

{{ post.get_absolute_url }}



Post 모델에 **get_absolute_url**을 지정한다

resolve_url함수는 가장 먼저 get_absolute_url() 함수의 존재여부를 체크하고

존재 할 경우 reverse를 수행하지 않고 그 리턴값을 즉시 리턴

```python
class Post(model.Model):
	...
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])
```



## 그 외

### CreateView / UpdateView

success_url을 제공하지 않을경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크하고, 이동이 가능할 경우 이동

생성/수정하고나서 Detail화면으로 이동하는 것은 자연스러운 시나리오

### 특정 모델에 대한 Detail뷰를 작성할 경우

Detail뷰에 대한 URLConf설정을 하자마자, 필히 get_absoulte_url설정을 하자, 코드가 간결해짐