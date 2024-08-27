### 05장 파이썬 날개 달기
# 05-4 예외 처리

### 오류는 언제 발생하는가?
# 다음은 존재하지 않는 파일을 사용하려고 시도했을 때 발생하는 오류이다: FileNotFoundError
'''
>>> f = open("나없는파일", 'r')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
'''

# 이번에는 0으로 다른 숫자를 나누는 경우에 발생하는 오류이다: ZeroDivisionError
'''
>>> 4 / 0

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
'''

# 다음은 값이 채워지지 않은 인덱스를 참조할 경우 발생하는 오류이다: IndexError
'''
>>> a = [1, 2, 3]
>>> a[3]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
'''

### 오류 예외 처리 기법
## try-except 문
'''
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
'''

# 1. try-except만 사용하는 방법
'''
try:
    ...
except:
    ...
'''

# 2. 발생 오류만 포함한 except 문
'''
try:
    ...
except 발생오류:
    ...
'''

# 3. 발생 오류와 오류 변수까지 포함한 except문
'''
try:
    ...
except 발생오류 as 오류변수:
    ...
'''

# 예시: try문에서 오류가 발생하면 except블록이 실행되고, 오류변수 e에 담기는 오류 메시지를 출력할 수 있다.
'''
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
'''

## try-finally 문
# try절에는 finally절을 사용할 수 있다. finally절은 try절의 예외 발생 여부와 관계없이 실행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 때 많이 사용한다.
# try_finally.py 파일 참고


## 여러 개의 오류 처리하기
# try문 안에서 여러 개의 오류를 같이 처리하려면 다음과 같이 사용해야 한다.
'''
try:
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
'''

# 즉, 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다. 
# many_error.py 참고

# 오류 메시지도 다음과 같이 처리된다.
try:
    a=[1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

# 인덱싱 에러가 첫 번째로 발생하므로, 해당 에러만 출력된다: list index out of range


## 다음과 같이 ZeroDivisionError와 IndexError를 함께 처리할 수도 있다.
# 두 개 이상의 에러를 동일하게 처리하기 위해서는 아래와 같이 괄호를 사용하여 함께 묶어 처리하면 된다.
# 매개변수 순서와 관계없이, 첫 번째 발생한 오류만 출력된다.
try:
    a=[1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


## try-else문
# finally와는 달리, try-else문에서의 else는 오류가 발생하지 않아야 수행된다.
# 즉, 오류가 발생하면 except문이, 오류가 발생하지 않으면 else문이 수행된다. 
# try_else.py 참조
'''
try:
    ...
except [발생오류[as 오류변수]]:
    ...
else: # 오류가 없을 경우에만 수행
    ...
'''


## 오류 회피하기
# 코드를 작성하다 보면 특정 오류가 발생했을 경우 그냥 통과시켜야 할 때가 있다. 
# error_pass.py 참조


## 오류 일부러 발생시키기
# 프로그래밍을 하다 보면 의도적으로 에러를 발생시켜야 하는 경우가 존재한다.
# 파이썬은 raise 명령어를 사용하여 오류를 강제적으로 발생시킬수 있다. # error_raise.py 참조


## 예외 만들기
# 프로그램을 만들다 보면 특수한 경우에만 예외 처리를 하려고 종종 예외를 만들어서 사용한다.
# 예외를 직접 만들어 보자.

# 예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    pass

# 그리고 별명을 출력하는 함수를 다음과 같이 작성해 보자.
def say_nink(nink):
    if nink=='바보': # 별명을 바보로 설정했을 시 에러 발생시키기!
        raise MyError()
    print(nink)

'''
say_nink('천사')
say_nink('바보')
'''

# 이번에는 예외 처리 기법을 통해 MyError 발생을 예외 처리해 보자.
'''
try:
    say_nink('천사')
    say_nink('바보')
except MyError:
    print('허용되지 않는 별명입니다.')
'''

# 만약 오류 메시지를 사용하고 싶다면 다음처럼 예외 처리를 하면 된다.
try:
    say_nink('천사')
    say_nink('바보')
except MyError as e:
    print(e)
# 하지만 프로그램을 실행해 보면 오류 메시지가 출력되지 않는 것을 볼 수 있다. 
# 오류 메시지를 출력하기 위해 __str__ 메소드를 구현해야 한다. 
# __str__메소드는 print(e) 처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메소드이다.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    
# 클래스 재 정의 이후에 확인해보면 오류 메시지가 정상적으로 출력된다.
