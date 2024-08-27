# error_pass.py
# try문 안에서 FileNotFoundError가 발생했을 경우, pass를 이용하여 오류를 그냥 회피하도록 작성한 예제이다.

try:
    f=open('없는파일', 'r')
except FileNotFoundError:
    pass # 오류회피

