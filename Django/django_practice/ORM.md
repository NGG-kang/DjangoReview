# Django ORM

#### 1. ORM

Object Relational Mapping

장고는 ORM을 통해 SQL을 생성/실행한다

내가 작성된 ORM코드를 통해 어떤 SQL이 실행되고 있는 지, 파악하고, 최적화를 할 수가 있어야 한다

django-debug-toolbar를 활용하여 SQL 수행 구문을 쉽게 확인이 가능하다!

django ORM은 RBS만을 지원한다



장고의 강점은 Model과 Form

SQL을 직접 실행 할 수는 있으나, 가능하면 ORM을 쓰는게 좋다

예시로 쓰는법 / 나중에 쓸 일이 있을지는 모르겠다

```python
from django.db import connection, connections
with connection.cursor() as cursor:
	cursor.excute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
	cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
	print(row)
```



#### 2. DB 테이블과 파이썬 클래스는 1:1로 매핑된다

`models.py`에서 설계한 class들은 DB와 1:1로 매핑됨

서비스에 맞춰서 데이터베이스 설계가 필요하다





