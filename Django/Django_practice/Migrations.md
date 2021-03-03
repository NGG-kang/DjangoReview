# Migrations

모델의 변경 내역을 "데이터베이스 스키마"로 반영시키는 효율적인 방법을 제공



<appname>생략시 전체에 대하여 실행

마이그레이션 파일 생성

python manage.py makemigrations <appname>

지정 데이터베이스에 마이그레이션 적용

python manage.py migrate

마이그레이션 적용 현황 출력

python manage.py showmigrations <appname>

지정 마이그레이션의 SQL 내역 출력

python manage.py sqlmigrate <appname> <migration-name>

​	 migration-name이 현재 적용된 마이그레이션보다 이전이라면 역방향으로 마이그레이션

​	zero를 쓰면 처음으로 롤백





### Migration 파일

데이터베이스에 어떤 변화를 가하는 Operation들을 나열

​	테이블 생성/삭제, 필드 추가/삭제 등

​	커스텀 파이썬/SQL Operation

​		데이터 마이그레이션 등

대개 모델로부터 자동 생성 -> makemigrations 명령

​	모델 참조 없이 빈 마이그레이션 파일 만들어서 직접 채워넣기도함

같은 Migration 파일이라 할지라도, DB종류에 따라 다른 SQL이 생성된다



### 마이그레이션 파일 생성 및 적용

모델 변경내역#1 -> makemigrations -> 마이그레이션 파일#1 -> migrate -> DB에 적용



### makemigrations 하는 떄

모델 필드 관련된 어떠한 변경이라도 발생 시에 마이그레이션 파일 생성

마이그레이션 파일은 모델의 변경내역을 누적하는 역할

squashmigrations 명령으로 다수의 마이그레이션 파일을 통합할 수 있다.





### 새로운 필드가 필수라면

blank,null 옵션이 false일때 

 makemigrations 명령을 수행할 때 기존 record들에 어떤 값을 채워넣을지 물어봄



### 협업 팁

팀원 각자가 마이그레이션 파일을 생성 -> 충돌 발생

마이그레이션 파일 생성은 1명이 전담해서 생상하는게 좋다

생성한 마이그레이션 파일을 버전관리에 넣고, 다른 팀원은 이를 받아서 migrate만 수행



개발시에 서버에 아직 반영하지 않은 마이그레이션을 다수 생성했다면

이를 그대로 서버에 반영하지말고 하나의 마이그레이션으로 합쳐서 적용하는걸 권장

squashmigrations 명령