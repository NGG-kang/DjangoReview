# Django Model 



Primary key : AutoField, BigAutoField

문자열: CharField, TextField, SlugField

날짜/시간: DateField, TimeField, DateTimeField, DuirationField

참/거짓: BooleanField, NullBooleanField

숫자: IntegerField, SmallIntegerField, PositiveIntegerField, PositiveIntegerField, PositiveSmallInteregerFIeld,  BigIntergerField, DecimalField, FloatField

파일: BianryField, FileField, ImageField, FieldPathField



이메일: EmailField

URL: URLField

UUID: UUIDField

아이피: GenericIPAddressField

Relationship Types

- ForeignKey
- ManyToManyField
- OneToOneField

그외 커스텀 필드들

https://django-model-utils.readthedocs.io/en/latest/



**모델의 필드들은 DB 필드 타입을 반영한다**

Varchar 필드타입 -> charField, SlugField, URLField, EmailField등



**파이썬 데이터타입과 데이터베이스 데이터타입을 매핑**

AutoField -> int

BinaryField -> bytes

BooleanField -> bool

CharField, SlugField, URLField, EmailField -> str -> 위의 varchar와 차이점은 디폴트 적용된 유효성 검사 등의 차이가 있다



**같은 모델 필드라 할지라도 DB에 따라 다른 타입이 될 수도 있다**





자주쓰이는 필드 공통옵션

blank : 장고단에서 validation시에 empty 허용 여부

null : null 허용 여부

db_index : 인덱스 필드 여부

default : 디폴트 값 지정, 혹은 값 리턴해줄 함수 지정

unique : 현재 테이블 내에서 유일성 여부 

choices : select 박스 소스로 사용

validators : validators를 수행할 함수를 다수 지정

verbose_name : 필드 레이블, 미지정시 필드명 사용

help_text : 필드 입력 도움말



설계한 데이터베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해주는 것이 입력값 오류를 막을 수 있다.

blank/null 지정은 최소화

validators들이 다양하게/타이트하게 지정된다

필요하다면, validator들을 추가로 타이트하게 지정해야한다

프론트엔드에서 유효성 검사는 사용자 편의를 위해 수행, 백엔드에서의 유효성 검사는 필수이다

직접 유효성 로직을 만들지 마라, 이미 잘 구성된 Features들을 가져다 쓰라

장고의 Form/Model을 통해 지원되며, django-rest-framework의 Serializer를 통해서도 지원된다



ORM은 SQL 쿼리를 만들어주는 역할일 뿐 성능높은 애플리케이션을 위해서는

데이터베이스에 대한 깊은 이해도가 필요하다

