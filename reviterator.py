# reviterator.py

class ReverseItertor:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) -1 # 포지션 변수를 리스트의 마지막 객체의 인덱스로 설정한다.

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0: # 포지션 변수가 0 이 되면 호출 시 StopIteration 예외를 발생시킨다.
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1 # 포지션 변수가 0이 될 때 까지 호출 시 마다 값을 1 씩 감소시킨다.
        return result

if __name__ == "__main__":
    i = ReverseItertor([1,2,3])
    for item in i:
        print(item)