# 05장 파이썬 날개 달기
# 05-1 클래스
    
### 객체와 인스턴스의 차이
# 객체는 클래스로 만들어낸 하나의 결과를 말할 때 사용
# 인스턴스는 특정 객체가 어떤 클래스의 객체인지 '관계 위주'로 설명할 때 어울리는 단어이다.
# ex) a = Calculator1(); a1 = Calculator2() 일 경우, 'a와 a1은 객체'라고 부르고, 'a1은 Calculator2의 인스턴스이다' 처럼 사용한다.

# 예제 시작
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result+=num
        return self.result
    
    def sub(self, num):
        self.result-=num
        return self.result
    # end of method
# end of Calculator

class FourCal:
    pass # 함수 선언과 같이 코드를 임시로 작동시키기 위해 사용

class FourCal:
    def __init__(self, first, second): # 메소드명을 __init__으로 설정할 시, 생성자로 인식되어 객체 생성 시점에 자동으로 호출된다.
        self.first = first
        self.second = second
    
    # 파이썬 메소드의 첫 번재 매개변수 이름은 관례적으로 self를 사용한다.
    # self에는 객체 자기 자신이 들어간다.
    def setData(self, first, second):
        self.first = first # self 객체의 변수로 self.first, self.second가 선언된다.
        self.second = second # 객체에 생성되는 객체만의 변수를 ‘객체변수’ 또는 ‘속성’이라고 부른다.
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
# end of FourCal

a = FourCal(4, 2)
print(type(a)) # 객체 a가 어떤 클래스의 인스턴스인지 출력한다.

a.setData(4, 2) # 클래스 메소드 호출 시, self 매개변수 자리는 생략하고 호출한다.
# a.first = 4, a.second = 2     # 객체에 생성되는 객체만의 변수를 ‘객체변수’ 또는 ‘속성’이라고 부른다.

### 생성자
# 파이썬 클래스의 생성자는 메소드 이름을 __init__으로 하여 작성한다.
# 이름이 __init__인 메소드는 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다.

### 상속
# 파이썬에서 클래스를 상속할 경우 
# 새로 작성한 클래스의 매개변수에 상속할 클래스를 넣으면 된다.
class MoreFourCal(FourCal): # 이와 같은 경우, MoreFourCal 클래스는 FourCal 클래스를 상속한다.
    pass

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second # 연산자 a**b는 a의 b제곱을 뜻한다.
        return result
    # 이와 같이 MoreFourCal은 FourCal의 필드인 self.first와 self.second를 사용할 수 있다.
# end of MoreFourCal
    
### 메소드 오버라이딩
b = FourCal(4, 0)
# print(b.div()) # 오류 발생! 0으로 나눌 때의 분기처리를 하지 않았기 때문

# 따라서 0으로 나눌 때의 분기처리를 하기 위해 해당 함수를 오버라이딩한다.
class SafeFourCal(FourCal):
    def div(self):
        if(self.second == 0 ):
            return 0 # 0으로 나눌 경우 0을 리턴하도록 수정
        else:
            return self.first / self.second
# end of SafeFourCal

c = SafeFourCal(4, 0)
print(c.div()) # 오류 분기처리 성공

### 클래스변수
# 클래스변수는 클래스 내에 생성하는 변수이다.
class Family:
    lastname = '정' # 클래스변수
    
    def __init__(self, firstName):
        self.firstName = firstName # 지성
# end of Family

c = Family('지성')
d = Family('민수')

print(Family.lastname + c.firstName)
print(d.lastname + d.firstName) # 클래스 변수는 [클래스명].[클래스변수] 혹은 self.[클래스변수]와 같이 사용 가능하다.

# 객체변수와 무엇이 다른가?
# 쉽게 말해 클래스 내 static 변수라고 보면 된다.
# 따라서 객체에서 클래스 변수값을 수정할 경우, 모든 객체에 공통적으로 적용된다.