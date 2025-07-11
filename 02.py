'''
파이썬 대화형 인터프리터. ( 파이썬 셸. python shell )
대화형. ( 입력에 따른 결과값이 바로 출력. 간단한 예제를 풀 때 결과를 바로 확인할 수 있어 학습하는데 효과적 )
인터프리터. ( 사용자가 입력한 소스 코드를 실행하는 환경 )
프롬프트. ( prompt. >>>. 입력하는 부분 )
종료. ( Ctrl + Z 누른 후 Enter or quit() or exit() or import sys. sys exit() )
파이썬은 대소문자를 구별한다.
ex. print ( o ), PRINT ( x )
아직 입력 중인 문장이 끝나지 않음. ( ... )

파이썬 대화형 인터프리터.
장점. 
간단한 예제를 풀 때는 편리하다.

단점. 
여러 줄의 복잡한 소스 코드를 가진 프로그램을 만들 때는 불편하다.
인터프리터를 종료하면 작성한 프로그램이 사라져 다시 사용하지 못한다.

해결방법.
에디터 사용.
에디터. ( editor. 소스 코드를 편집할 수 있는 프로그래밍 도구 )
ex. IDLE( 아이들. Integrated development and learning environment. 파이썬 프로그램 작성을 도와주는 통합 개발 환경 )

명령 프롬프트 창에서 파이썬 파일 실행. ( python 파일명.py )
'''

# 사칙연산
'''
print("더하기:", 1 + 2)
print("나누기:", 3 / 2.4)
print("곱하기:", 3 * 9)
a = 1
b = 2
print(a + b)
a = "Python"
print(a)
'''

# Spacebar 4개 or Tab 을 이용해 반드시 들여쓰기
# 조건문 if
'''
a = 3
if a > 1:
    print("a는 1보다 크다.")
'''

# 반복문 for
'''
for a in [1, 2, 3]:
    print(a)
'''
    
# 반복문 while
'''
i = 0
while i < 3:
    i = i + 1
    print(i)
'''

# 함수
# def. ( 파이썬에서 함수를 정의할 때 사용하는 예약어 )
# 예약어. ( 프로그래밍 언어에서 이미 문법적인 용도로 사용하고 있는 단어를 말한다. )
# a, b. ( 입력값 )
# a + b. ( 결과값 )
# 리턴 ( return. 함수에서 값을 반환할 때 사용 )
'''
def add(a, b):
    return a + b

print(add(3, 4))
'''