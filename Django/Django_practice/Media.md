# Django Media

Media파일

FileField/ImageField를 통해 저장한 모든 파일

DB필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장

**실제로는 문자열을 저장하는 필드**

프로젝트 단위로 저장/서빙한다



Django의 ImageField는 pillow 라이브러리가 필요하다