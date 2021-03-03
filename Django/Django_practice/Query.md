# Query 약간

`Post.objects.all()` select all

`Post.objects.all().order_by('-id')[:10]` /  마이너스 사용시 역순 / 

위의 order_by 사용시 model의 class Meta의 ordering은 무시가된다

**QuerySet**

SQL을 생성해주는 인터페이스

순회가능한 객체

Model Manager를 통해 해당 Model에 대한 QuerySet을 획득

[Django QuerySet](https://docs.djangoproject.com/en/3.1/ref/models/querysets/) 각종 쿼리셋들이 나와있다



**QuerySet은 Lazy**한 특성

QuerySet을 만드는 동안에는 DB접근을 하지 않는다

실제로 데이터가 필요한 시점에 접근함

**데이터가 필요한 시점**

1. queryset
2. print(queryset)
3. list(queryset)
4. for instance in queryset: print(queryset)



.filter()를 사용시

예를들어 gt(grater than), istartswith(대소문자 구분하지 않는 시작)을 쓸때 언더바 2개를 쓴다

`Post.object.filter(id__gt=1)`

`Post.object.filter(id__istartswitch='1')`



filter() 포함하는 항목

exclude() 포함하지 않는 항목



and조건은 콤마를 사용하면 and조건이다

OR 조건을 사용하려면 Q를 사용해야한다

Q에서의 and = & / or = |  한번씩만 사용한다

[Q객체를 사용한 조회](https://docs.djangoproject.com/en/3.1/topics/db/queries/#complex-lookups-with-q)



문자열 인덱싱처럼 퀘리셋도 인덱싱처럼 자를 수 있다

`Post.objects.all()[1,10,1]`  1부터 10까지 1스텝으로 가져온다

스텝같은 경우는 django딴에서 처리해주는것, 쿼리에서 지원하지 않는다



order_by가 있듯이 reverse()로 거꾸로 정렬도 있다