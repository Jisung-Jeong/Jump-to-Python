# decorater2.py

import time

def elapsed(original_func):
    def wrapper(*args, **kwargs): # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs) # 기존 함수 수행
        end = time.time()
        print("함수 수행 시간: %f초" % (end-start)) # 기존 함수의 실행시간을 출력한다.
        return result # 기존 함수의 수행 결과 리턴
    return wrapper

@elapsed # 어노테이션처럼 사용 가능
def myfunc(msg):
    print("'%s' 를 출력합니다." % msg)
    
# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc("you need python") # 그대로 실행하면 오류가 난다. 파라미터를 데코레이터로 전달할 수 없기 때문이다.