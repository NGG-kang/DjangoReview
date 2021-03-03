# render 약간

view 딴에서 값을 돌려줄때 사용한다

보통 아래와 같이 사용한다

```django
return render(reuqest, 'templates_url', {
	'context_name1': 'context1',
	'context_name2': 'context2',
})
```

