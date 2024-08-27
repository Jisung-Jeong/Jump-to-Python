# 05장 파이썬 날개 달기
# 05-2 모듈

### 모듈 학습 전 간단한 모듈 만들어보기
# mod1.py

import mod1 # 모듈 불러오기
# import는 현재 디렉터리에 있는 파일이나, 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 모듈의 사용은 mod1.add(), mod.sub와 같이 [모듈명].[메소드]와 같이 사용한다.

from mod1 import add, sub # 메소드를 바로 사용하고 싶을 경우, from [모듈명] import [메소드]와 같이 사용한다.
from mod1 import * # import 뒤 와일드 카드를 사용하는 방법도 있다.


### if __name__ == "__main__":의 의미
# print 함수가 작성된 모듈 mod2.py

import mod2 # mod2.py를 불러오고 현재 파일을 실행하는 순간, mod2.py의 print함수가 실행되어 버린다.
# 이러한 문제를 방지하기 위해 mod2.py를 mod3.py와 같이 수정하여야 한다. -> mod3.py 확인

# __name__ 변수란 파이썬 내부적으로 사용하는 변수 이름이다.
# 만약 python mod2.py처럼 모듈을 직접 실행하면 __name__값은 __main__값이 저장된다.
# 그러나 다른 파일에서 mod2.py 모듈을 import할 경우, __name__ 변수에는 mod2.py의 모듈 이름인 mod2가 저장된다.
import mod2
print(mod2.__name__) # 실행

# 따라서 모듈 내 이슈가 있는 라인에 if __name__ == "__main__": 문장을 삽입하여 모듈 파일을 직접 실행하지 않는 한, 이슈 라인이 실행되지 않도록 한다.


### 클래스나 변수 등을 포함한 모듈
# mod4.py

import mod4
print(mod4.PI) # mod4 모듈에 저장된 변수값은?

e = mod4.Math()
print(e.solv(2)) # mod4 모듈에 저장된 클래스 내 메소드 실행 결과는?

print(mod4.add(mod4.PI, 4.4)) # 모듈 내 메소드와 변수끼리 연산이 되는가?


### 다른 디렉터리에 있는 모듈 불러오기
# ./05-2_moduleFile/mod5.py

# 먼저 sys 모듈을 불러온다.
# sys 모듈은 파이썬 기본 라이브러리 모듈이다. sys 모듈 사용 시 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.
import sys

# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리 리스트를 보여준다. 
# 해당 리스트의 디렉터리 안에 저장된 파이썬 모듈은 설치된 디렉터리로 이동할 필요 없이 바로 불러와 사용할 수 있다.
# print(sys.path)

# 다른 디렉터리에 사용하고자 하는 모듈이 있다면, 그 경로를 sys.path에 기입하면 된다.
# sys.path.append()를 사용하면 sys.path 리스트에 새 항목을 추가할 수 있다. (모듈 추가 시 .py 확장자는 기입하지 않는다!)
sys.path.append("C:/Js_Study/PracPython/05-2_moduleFile")

# 이로 인해 다른 디렉터리에 있는 모듈인 mod5를 불러와 사용할 수 있다.
import mod5
print(mod5.add(3, 4))

# sys 모듈을 사용하지 않는 방법으로는 PYTHONPATH 환경 변수를 사용하는 방법이 있다.
# set PYTHONPATH=C:\Js_Study\PracPython\05-2_moduleFile (마찬가지로 .py 확장자를 기입하지 않는다!)
# 맥이나 유닉스 환경에서는 set 대신 export를 사용하여야 한다.