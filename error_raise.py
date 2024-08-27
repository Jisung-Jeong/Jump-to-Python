# error_raise.py

# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현하도록 만들고 싶은 경우, raise를 사용한다.

class Bird:
    def fly(self):
        raise NotImplementedError # 에러 발생시키기

# 만약 Bird 클래스를 상속받는 자식 클래스가 fly 함수를 오버라이딩(구현)하지 않았다면 에러를 발생시킨다.
# NotImplementedError는 파이썬에 이미 정의되어 있는 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 발생시키기 위해 사용한다.


class Eagle(Bird): # Bird를 상속받음
    pass

eagle = Eagle()
eagle.fly() # Bird 클래스의 fly함수를 오버라이딩 하지 않았기 때문에 NotImplementedError 오류 발생!


# NotImplementedError가 발생하지 않도록 하려면 fly함수를 구현하면 된다!
