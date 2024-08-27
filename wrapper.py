# wrapper.py

def mul(m):
    def wrapper(n): # __call__과 비슷한 느낌
        return m * n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)
    
    print(mul3(5))
    print(mul5(3))

# 외부 함수 mul 안에 내부 함수 wrapper을 구현하였다.
# 함수를 받을 변수 하나를 두고 mul을 호출하면 인자로 받은 m이 wrapper 함수 내에 적용되어 반환된다.
# 마치 클래스가 생성자를 통해 객체를 생성하는 것과 비슷하다.

# 여기서 mul과 같은 함수를 파이썬에서는 '클로저' 라고 한다.