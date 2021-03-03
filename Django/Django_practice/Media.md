# Django Media

Media파일

FileField/ImageField를 통해 저장한 모든 파일

DB필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장

**실제로는 문자열을 저장하는 필드**

프로젝트 단위로 저장/서빙한다



Django의 ImageField는 pillow 라이브러리가 필요하다



### Media 파일 처리 순서

1. HttpRequest.FILES를 통해 파일이 전달
2. 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행
3. FileField/ImageField 필드에 "경로(문자열)를 저장하고"
4. settings.MEDIA_ROOT 경로에 파일을 저장



`settings.py`에 경로 지정

`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

`MEDIA_URL = '/media/'`

MEDIA_ROOT 예시

기본 dir 위에 public 안의 media폴더 라는 뜻

`MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'public', 'media')`



#### FileField, ImageField 

**FileField**

File Storage API를 통해 파일을 저장

장고에서는 File system storgae만 지원, django-storags를 통해 확장 지원

해당 필드를 옵션 필드로 두고자 할 경우, blank=True 옵션 적용



File Upload Handler

파일크기가 2.5MB 이하일경우 메모리에 담겨 전달

MemoryFileUploadHandler

파일크기가 2.5MB 초과일 경우

디스크에 담겨 전달

TemporaryFileUploadHandler

관련 설정

settings.FILE_UPLOAD_MAX_MEMORY_SIZE

**ImageField**

Pillow를 통해 이미지 width/height 획득

위 필드를 상속받은 커스텀 필드를 만들 수 있다

ex) PDFField, ExcelField등



ImageField는 url, path 속성을 가진다

photo.url 은 주소 경로 리턴

photo.path 는  파일 경로 리턴

##### 사용 할만한 옵션

blank: 파일 경로 미지정 여부

upload_to: 파일 경로 지정

`upload_to='instagram/post/%Y/%m/%d'`

경로를 지정하되 (%Y %m %d %H %M %S) 로 연월일 시분초를 폴더로 지정 할 수 있다

성능을 위해 한 폴더에 너무 많은 파일이 저장되지 않도록 조정하기

동일 파일명으로 저장시 파일에 더미 문자열을 붙여 파일 덮어쓰기 방지해준다

이렇게 문자열 지정을 해도 되고

**함수**형태로 만들수 있다

함수형은 중간 디렉터리 경로 및 파일명 까지 결정이 가능하다

**uuid를 통한 파일명 정하기가 가능하다** 

#TODO : uuid를 통한 파일명 바꾸기 알아보기



#### MEDIA_URL 지정

MEDIA_URL을 지정해줘야 MEDIA 파일을 서버에서도 볼 수 있다

그래서 `urls.py`에 MEDIA_URL을 추가 해줘야함

```python
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



그러나 static 파일 서빙을 직접 하는걸 권장하지 않는다

settings에 debug=false로 한다면 자동으로 static 비활성화 된다고 한다

진짜로 false로 하니까 not Found 페이지로 이동한다



make_safe를 사용하면 python에서 태그 사용시 

창에서 태그 결과가 나온다

```python
from django.utils.safestring import mark_safe
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f"<img src='{post.photo.url}' />")
        return None
```

