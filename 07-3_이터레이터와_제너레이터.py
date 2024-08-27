# 07장 파이썬 날아오르기
# 07-3 이터레이터와 제너레이터

# 반복 가능한 객체를 iterable 객체라고 한다. 그렇다면 Iterator 란 무엇인가?
'''
>>> a = [1, 2, 3]
>>> next(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
'''

# a 라는 리스트로 next(a)를 호출했더니 리스트는 이터레이터 객체가 아니라는 오류가 발생한다.
# 즉, 반복이 가능하다고 하여 이터레이터는 아니라는 것이다.
# 하지만 반복 가능하다면 다음과 같이 iter 함수를 이용해 이터레이터로 만들 수 있다.

a = [1, 2, 3]
ia = iter(a)
type(ia)
# <class 'list_iterator'>


# 위 코드로 리스트를 이터레이터로 변경했으므로 next 함수를 호출해 보자.
print(next(ia))
print(next(ia))
print(next(ia))