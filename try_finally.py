# try_finally.py

try:
    f=open('foo.txt', 'w')
    # 무언가를 수행한다.

finally:
    f.close() # 중간에 오류가 발생하더라도 무조건 실행된다.

# foo.txt 파일을 쓰기 모드로 연 후 발생 여부와 상관없이 항상 파일을 닫아 주려면 try-finally문을 사용하면 된다.