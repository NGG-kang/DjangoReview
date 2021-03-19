# CodeUp Python 기초 100제



CodeUp Python 기초 100제에서 배운 내용들을 정리하는 페이지 입니다





```python
a, b = input().split()			# a,b를 띄어쓰기를 기준으로 나눠서 입력받음
a, b = input().split('-')		# a,b를 '-'기준으로 나눠서 입력받음

print(a,b, sep=':')				# a,b를 ':'기호를 사이에 두고 출력

print('%x'% n)					# n이 int일때 n을 16진수로 출력
print('%o'% n)					# n이 int일때 n을 8진수로 출력

n = int(a, 16)					# a를 16진수로 인식한다
n = ord(input())				# input을 유니코드로 반환

chr(n)							# n을 유니코드로 변환
```



