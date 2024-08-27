# render.py

def render_test():
    print("render")
    
### relative 패키지
# 만약 graphic 디렉터리의 render.py 모듈에서 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 다음과 같이 수정한다.
from game.sound.echo import echo_test
def render_echo_test():
    print("render")
    echo_test()

# 위 예제처럼 전체 경로를 입력해 import 할 수도 있지만, 다음과 같이 relative하게 import하는 것도 가능하다.(상대경로)
# 파이썬의 상대 경로는 일반적인 경로 입력 방법과 문법이 살짝 다르다.
from ..sound.echo import echo_test
