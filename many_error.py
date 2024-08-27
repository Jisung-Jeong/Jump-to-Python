# many_error.py

try:
    a = [1, 2]
    print(a[3]) # IndexError
    4 / 0 # ZeroDivisionError
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
    
# IndexError가 먼저 발생했으므로, 이후에 발생할 ZeroDivisionError은 출력되지 않는다.