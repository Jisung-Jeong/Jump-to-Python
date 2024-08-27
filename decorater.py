# decorater.py

import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func() # 기존 함수 수행
        end = time.time()
        print("함수 수행 시간: %f초" % (end-start)) # 기존 함수의 실행시간을 출력한다.
        return result # 기존 함수의 수행 결과 리턴
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")
    
decorated_myfunc = elapsed(myfunc)
decorated_myfunc()