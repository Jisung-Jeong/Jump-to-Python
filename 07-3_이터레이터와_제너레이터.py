# 07장 파이썬 날아오르기
# 07-3 이터레이터와 제너레이터

### 이터레이터란?
# 반복 가능한 객체를 iterable 객체라고 한다. 그렇다면 Iterator 란 무엇인가?
# 이터레이터는 next() 함수 호출 시 계속 그다음 값을 리턴하는 객체이다.
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
# print(next(ia)) # StopIteration 예외 발생

# 더 이상 반환할 값이 없다면 이터레이터는 StopIteration 예외를 발생시킨다.

# 한 번 출력한 값은 다시 출력하지 못한다.
# 위에서 print(next()) 함수로 전부 출력했기에 더 이상 출력할 값이 없다.
for i in ia:
    print(i)


### 이터레이터 만들기
# iter 함수를 사용하면 리스트를 이터레이터로 만들 수 있다.
# 이번에는 클래스로 이터레이터를 만들어 보자.
# iterator.py 첨조



### 제너레이터란?
# 제너레이터는 이터레이터를 생성해 주는 함수이다. 제너레이터로 생성한 객체는 이터레이터와 마찬가지로 next()함수 호출 시 그다음 값을 얻을 수 있다.
# 이 때 제너레이터에서는 차례대로 결과를 반환하고자 return 대신 yield 키워드를 사용한다.

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()

# mygen 함수는 yield 구문을 포함하므로 제너레이터이다. 
# 제너레이터 객체는 g=mygen() 과 같이 제너레이터 함수를 호출하여 만들 수 있다.
# type 명령어로 확인하면 g 객체는 제너레이터 타입의 객체임을 알 수 있다.
print(type(g))
# <class 'generator'>

print(next(g))
print(next(g))
# 이처럼 제너레이터 객체 g로 next 함수를 실행하면 mygen 함수의 첫 번째 yield 문에 따라 'a' 값을 리턴한다. 
# 제너레이터는 yield라는 문장을 만나면 그 값을 리턴하되 현재 상태를 그대로 기억한다. next 함수를 실행할 때 마다 그다음 값을 리턴한다.
# mygen 함수에는 총 3개의 yield 문이 있으므로 네 번째 next를 호출할 때는 더는 리턴할 값이 없으므로 StopIteration 예외가 발생한다.


### 제너레이터 표현식
# generator.py 참조

### 제너레이터와 이터레이터
# 제너레이터와 이터레이터는 서로 비슷한 성질을 띈다. 클래스를 이용해 이터레이터를 작성하면 좀 더 복잡한 행동을 구현할 수 있다.
# 이와 달리 제너레이터를 이용하면 간단하게 이터레이터를 만들 수 있다.
# 따라서 이터레이터의 성격에 따라 클래스로 만들 것인지, 제너레이터로 만들 것인지를 선택해야 한다.

# 제너레이터는 어떤 경우에 사용하면 좋을까? 다음의 예제를 통해 생각해보자.
# generator2.py 참조