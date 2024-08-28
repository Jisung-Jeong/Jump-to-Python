# generator2.py

# 제너레이터 표현식
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
'''
list_job = [longtime_job() for i in range(5)]
print(list_job[0])
'''

# longtime_job 함수는 실행 시간이 1초이다. 
# 이 예제는 longtime_job 함수를 5번 실행해 리스트에 그 결괏값을 담고 그 첫번째 결괏값을 호출하는 예제이다.
'''
실행 결과
job start
job start
job start
job start
job start
done
'''
# 리스트를 만들 때 이미 5개의 함수를 모두 실행하므로 5초의 시간이 소요되고 이와 같은 결과를 출력한다.
# 이 예제에 제너레이터를 적용해보자.

# 제너레이터 표현식 사용
list_job = (longtime_job() for i in range(5))
print(next(list_job))

# 제너레이터 표현식을 사용하므로써 실행 시 1초만 소요되고 출력되는 결과도 전혀 다르다.
'''
job start
done
'''
# 왜냐하면 제너레이터 표현식으로 인해 longtime_job 함수가 next 함수를 호출할 때에만! 5회가 아닌 1회만 호출되기 때문이다.
# 이러한 방식을 느긋한 계산(LAZY evaluation) 이라고 부른다.
# 시간이 오래 걸리는 작업을 한꺼번에 처리하기보단 필요한 경우에만 호출하여 사용할 때 제너레이터는 매우 유용하다.