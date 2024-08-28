# generator.py

def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result # 결과를 제너레이터 내의 이터레이터에 저장한다.

gen = mygen()

print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9

# 제너레이터는 def를 이용한 함수로 만들 수 있지만, 다음과 같이 튜플 표현식으로 좀 더 간단하게 만들 수 있다.
gen = (i*i for i in range(1, 1000))

# 이 표현식은 mygen 함수로 만든 제너레이터와 완전히 똑같이 기능한다. 여기서 사용한 표현식은 리스트 컴프리헨션(list comprehension) 구문과 비슷하다. 
# 다만 리스트 대신 튜플을 이용한 점이 다르다. 이와 같은 표현식을 ‘제너레이터 표현식(generator expression)’이라고 부른다.

