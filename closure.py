# closure.py
class Mul:
    def __init__(self, m): # 생성자
        self.m = m
    
    def mul(self, n):
        return self.m * n
    
    def __call__(self, n): # __call__을 사용하면 함수를 바로 사용할 수 있다.
        return self.m * n
    


if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)
    
    print(mul3.mul(5))
    print(mul5.mul(3))

    print(mul3(6)) # __call__을 이용한 호출