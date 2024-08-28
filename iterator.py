# iterator.py

# 이터레이터는 클래스에 __iter__와 __next__라는 두개의 메소드를 구현하여 만들 수 있다.

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data): # len은 length로, data의 개수를 반환한다.
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result


if __name__ == "__main__":
    i = MyIterator([1, 2, 3])
    for item in i:
        print(item)

# 파이썬에서 __iter__과 __next__ 는 특별한 의미를 가지는 이름이다.
# 클래스에 __iter__ 메서드를 구현하면 해당 클래스로 생성한 객체는 반복 가능한 객체가 된다.

# __iter__ 메서드는 반복 가능한 객체를 리턴해야 하며, 보통 클래스의 객체를 의미하는 self를 리턴한다.
# 클래스에 __iter__ 함수를 구현할 경우, 반드시 __next__ 함수를 구현해야 한다.

# __next__ 메서드는 반복 가능한 객체의 값을 차례대로 반환하는 역할을 한다.
# __next__ 메서드는 for 문을 수행하거나 next() 함수 호출 시 수행된다.
# 객체를 생성할 때 전달한 data를 하나씩 리턴하고, 리턴할 값이 없으면 StopIteration 예외를 발생시킨다.

# __next__ 메서드를 조작하여 next() 함수 호출 시 값을 역순으로 받아 올 수도 있다.
# reviterator.py 참조