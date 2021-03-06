# Static

[TOC]



## Static 파일

개발 리소스로서의 정적인 파일 (js,css,image 등)

앱/ 프로젝트 단위로 저장/서빙



### static 파일 경로

장고는 One Project, Multi App 구조

한 App을 위한 static 파일을 app/static/app 경로에 둔다

프로젝트 전반적으로 사용되는 static파일은 settings.STATICFIELS_DIRS에 지정된 경로에 둔다

다수 디렉토리에 저장된 static 파일은 collectstatic 명령을 통해 settings.STATIC_ROOT에 지정한 경로로 모아서 복사해서 서비스에 사용



STATIC_URL = None / STATIC_URL = '/static/'
	각 static 파일에 대한 URL Prefix
		탬플릿 태그 {% static "경로" %} 에 의해서 참조되는 설정
	항상 / 로 끝나도록 설정

STATICFIELDS_DIRS = [] / STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'pjname', 'static')]
	File System Loader에 의해 참조되는 설정

STATIC_ROOT = None / STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	python manage.py collectstatic 명령이 참조되는 설정
	여러 디렉토리에 나눠진 static 파일들을 이 경로의 디렉토리로 복사하여, 서빙
	배포에서만 의미가 있는 설정



## Static Files Finders

Template Loader와 유사
	설정된 Finders를 통해, static 템플릿이 있을 디렉토리 목록을 구성
		장고 서버 초기 시작 시에만 1회 작성
	디렉토리 목록에서 지정 상대경로를 가지는 static 파일 찾기

대표적인 2가지 Static Files Finders
	**App Directories Finder**
		"장고앱/static/"  경로를 디렉토리 목록에 추가
	**File System FInder**
		settings.STATICFILES_DIRS 설정값을 디렉토리 목록에 추가



## 탬플릿에서 static URL 처리 예시

1. settings.STATIC_URL, Prefix를 하드코딩

   STATIC_URL 설정은 언제라도/프로젝트마다 변경될 수 있음.
   변경이 되었을 때 하나하나 수정해줘야함

   무엇보다 배포시 static_url 설정값이 변경됨

2. Template Tag를 통한 처리

   프로젝트 설정에 따라 유연하게 static url prefix가 할당된다

   ```html
   {% load static %}
   <img src="{% static "blog/title.png" %}" />
   ```

   

## 개발환경에서의 static파일서빙

개발서버를 쓰고, settings.DEBUG = True 일 때에만 지원
	프로젝트/urls.py에 명시되어 있지 않아도 자동으로 추가
	순수 개발목적

개발서버를 쓰지 않거나 settings.DEBUG = False 일 때에는
	별도로 static 서빙 설정을 해 줘야한다

URL을 통해 파일시스템에 직접 접근하는 것이 아니라, 지정 이름의 STATIC 파일을 장고의 StaticFiles Finder에서 대신 찾아 그 내용을 읽어서 응답하는것



## static 서빙을 하는 여러가지 방법

1. 클라우드 정적 스토리지나 CDN 서비스 활용
2. apache/nginx 웹서버 등을 통한 서빙
3. 장고를 통한 서빙
   whitenoise 라이브러리를 활용해서 가능 -> Heroku 배포에 필요



## collectstatic 명령

실 서비스 배포 전에는 필히 본 명령을 통해 여러 디렉토리에 나눠져있는 static 파일들을 한 곳으로 복사

디렉토리 : settings.STATIC_ROOT

왜냐하면 여러 디렉토리에 나눠 저장된 static 파일들의 위치는 현재 장고 프로젝트만 알고있고, 외부 웹서버는 전혀 모르기 때문

외부 웹서버에서 Finder의 도움 없이도 static파일을 서빙하기 윟마

한 디렉토리에 모두 모여있기에 Finder의 도움이 필요없음



정적인 컨텐츠는 외부 웹서버를 통해 처리하면 효율적인 처리

정적 컨텐츠만의 최적화 사용방법



## 배포시에 static 처리 프로세스

1. 서비스용settings 에 배포 static 설정
2. 관련 클라우드 스토리지 설정, 혹은 아파치/nginx static 설정
3. 개발이 완료된 static파일을, 한 디렉토리로 복사
   `python manage.py collectstatic --settings=서비스용settings`
   Storage 설정에 따라 한 번에 클라우드 스토리지로의 복사를 수행되기도 함.
   settings.STATIC_ROOT 경로로 복사
4. settings.STATIC_ROOT 경로에 복사된 파일들을 배포서버로 복사
   대상 : 클라우드 스토리지, 혹은 아파치/nginx에서 참조할 경로
5. static 웹서버를 가리키도록 settings.STATIC_URL 수정



## static 관련 라이브러리

django-storages