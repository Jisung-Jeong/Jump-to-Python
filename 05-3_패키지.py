### 05장 파이썬 날개 달기
# 05-3 패키지

# 파이썬에서 패키지란 관련 있는 모듈들의 집합이다.
# 패키지는 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해 준다. (파이썬에서 모듈은 하나의 .py 파일이다.)

### 가상의 game 패키지 예시
'''
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''

# game, sound, graphic, play가 디렉터리, .py 파일이 파이썬 모듈이다.
# game 디렉터리는 루트 디렉터리이고, sound, graphic, play는 서브 디렉터리이다.

# 파이썬 패키지 구조는 공동 개발 작업이나 유지 보수 등 여러 면에서 유리하고,
# 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.


### 패키지 만들기(game으로 실습)
# 1. 루트 디렉터리 game 및 서브 디렉터리들을 만든다.
# 2. 각 디렉터리에 __init__.py 를 만들어 둔다.
# 3. echo.py 파일의 내용은 다음과 같이 작성한다. (./game/sound/echo.py 참조)
# 4. render.py 파일의 내용은 다음과 같이 작성한다. (./game/graphic/render.py 참조)
# 5. 방금 만든 game 패키지를 참조할 수 있도록 cmd 상에서 set 명령어로 PYTHONPATH 환경 변수에 C:/PracPython 디렉터리를 추가하고 실행한다.

### 패키지 안의 함수 실행하기
# echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

# echo 모듈이 있는 디렉터리까지 from...import 하여 실행하는 방법
from game.sound import echo
echo.echo_test()

# echo 모듈의 echo_test() 모듈을 직접 import하는 방법
from game.sound.echo import echo_test
echo_test()

# 그러나, import game; game.sound.echo.echo_test 과 같이 사용하는 것은 불가능하다.
# import game을 실행하면 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.
# 또 다음처럼 echo_test 함수를 사용하는 것도 불가능하다. >>> import game.sound.echo.echo_test

# 도트 연산자(.)를 사용해서 import a.b.c 처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈, 또는 패키지여야 한다.


### __init__.py의 용도
# __init__.py는 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py가 없다면 패키지로 인식되지 않는다.
# __init__.py 파일은 패키지와 관련된 '설정'이나 '초기화 코드'를 포함할 수 있다. (./game/__init__.py 참조)
import game
print(game.VERSION)
game.print_version_info()

### 패키지 내 모듈을 미리 import (./game/__init__.py 참조)
import game
game.render_test() # game/__init__.py에 모듈을 미리 import 하여, 패키지명만 import 해도 모듈 사용이 가능함

### 패키지 초기화 (./game/__init__.py 참조)
# __init__.py 파일에 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성할 수 있다. 
# 예를 들어 데이터베이스 연결이나 설정 파일 로드와 같은 작업을 수행할 수 있다.

# game 패키지의 초기화 코드는 game 패키지의 하위 모듈의 함수를 import 할 경우에도 실행된다.
from game.graphic.render import render_test

# 단, 초기화 코드는 한 번 실행된 후에는 다시 import를 하더라도 실행되지 않는다.
# 예를 들어 다음과 같이 game 패키지를 import 한 후에 하위 모듈을 다시 import 하더라도 초기화 코드는 처음 한 번만 실행된다.
import game
from game.graphic.render import render_test

### __all__
# 인터프리터에서 실행
from game.sound import *
echo.echo_test()

# 위 코드 실행 시 오류 발생!
# 특정 디렉토리의 모듈을 *를 사용하여 import 할 때에는 해당 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야 한다.
# ./game/sound/__init__.py 참조
# __all__ = ['echo'] 와 같이 작성!

# 주의사항: 모듈을 직접 import 할 때에는 not defined 오류가 발생하지 않는다.
# from [디렉터리] import * 할 경우에 오류 발생하는 것이다!

### relative 패키지
# 만약 graphic 디렉터리의 render.py 모듈에서 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 다음과 같이 수정한다. (모듈 내 모듈 import)
# ./game/graphic/render.py 참조

# 인터프리터에서 실행
from game.graphic.render import render_echo_test
render_echo_test() # 잘 실행된다!