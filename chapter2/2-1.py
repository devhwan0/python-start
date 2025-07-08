# Ctrl + / -> 주석
# ''' ''' 감싸기 -> 주석
# Ctrl + F -> 찾기, 바꾸기
# Ctrl + Alt + 위, 아래 방향키 -> 범위 선택
# Alt + 위, 아리 방향키 -> 위치 이동

# ------------- 자료형 숫자 -------------
# a = 3
# b = 1.2
'''
print("정수형 => 양의 정수, 음의 정수, 숫자 0 :", a)
print("실수형 => 소수점이 포함된 숫자 :", b)
'''

# type(a) => (a) 의 type
'''
print("a 의 type :", type(a))
print("b 의 type :", type(b))
'''

# a = 3
# b = 4
'''
print ("+ 더하기 :", a + b)
print ("- 빼기 :", a - b)
print ("* 곱하기 :", a * b)
print ("/ 나누기 :", a / b)
print ("// 몫 :", a // b)
print("% 나머지 :", a % b)
print("** 제곱 :", a ** b)
'''

# ------------- 자료형 문자 -------------
# a = "String"
# b = "b"
# c = "123"
# d = "'d'"
# e = "\"e\""
# f = "줄바꿈 '\\n' \n완료"
# g = """줄바꿈
# 완료"""
'''
print(g)
print(type(g))
'''

# head = "a"
# tail = " is String"
'''
print(head + tail)
print(head * 3)
print("=" * 50)
print("Dev")
print("=" * 50)
print(len(tail))
print("인덱싱", tail[1])
print(tail[-1])
print("슬라이싱 => a[이상:미만:간격] :", tail[4:7])
print(tail[:3])
print(tail[4:])
print(tail[::2])
print(tail[::-1])
print(tail[4:-3])
'''

# a = "20250622Rainy"
# year = a[:4]
# day = a[4:8]
# weather = a[8:]
'''
print(year)
print(day)
print(weather)
'''

# 문자열 포매팅 1
# a = "Formatting %d" % 5
# b = "Formatting %s" % "five"
# number = 3
# day = "three"
# c = "Formatting %d" % number
# d = "Formatting number %d day %s" % (number, day)
# e = "Formatting %s%%" % 3
# f = "%3s" % "hi" 
# g = "%-3sHwan" % "hi"
# h = "%10.3f" % 3.42134 
'''
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
'''

# 문자열 포매팅 2
# a = "Formattiong {1} String {0}".format(3, "three")
# b = "Formattiong {number} String {day}".format(number = 3, day = "three")
'''
print(a)
print(b)
'''

# 정렬
# a = "{0:<10}".format("hi")
# print(a)
# a = "{0:>10}".format("hi")
# print(a)
# a = "{0:^10}".format("hi")
# print(a)
# a = "{0:=^10}".format("hi")
# print(a)
# b = 3.4213
# a = "{0:.2f}".format(b)
# print(a)
# a = "{{and}}".format()
# print(a)

# 문자열 포매팅 최종
# name = "환"
# age = 27
# a = f"이름 : {name}, 나이 : {age + 1}"
# b = f"{'hi':=<10}"
# c = f"{3.423:10.2f}"
# d = f"{{and}}"
# e = 3000000
# f = f"{e:,}"
'''
print(a)
print(b)
print(c)
print(d)
print(f"{e:,}")
print(f)
'''

# 문자열 자료형
# a = "hobby"
'''
print(a.count("b"))
print(a.find("b"))
print(a.find("x"))
print(a.index("b"))
print(a.index("x"))
'''

# a = " and ".join("abcd")
# a = " and ".join(["a", "b", "c"])
# a = "hi".upper()
# a = "HI".lower()
# a = "Hi".lower()
# a = " hi ".lstrip()
# a = " hi ".rstrip()
# a = " hi ".strip()
# a = "a and b"
# a = a.replace("a ", "c and d ")
# a = a.split()
# a = "a:b:c"
# a = a.split(":")
'''
print(a)
'''

# ------------- 자료형 리스트 -------------
# odd = [1, 3, 5, 7, 9]
# odd1 = [1, 2, "3", "4"]
# odd2 = [1, "hi", ["3", "4"]]
'''
print(type(odd))
print(odd1[0] + odd1[1])
print(odd1[2] + odd1[3])
print(odd1[-1])
print(odd2[2][0])
print(odd2[1][0])
print(odd2[0][0])
'''

# a = [1, 2, 3, 4, 5]
'''
print(a[0:2])
print(a[0:2:1])
print(a[0:2:2])
print(a[0::2])
'''

# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[2:5])

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = 3
'''
print(a + b)
print(a * c)
print(len(a))
'''

# string 문자열 ( 문자 + 리스트( 배열 ) )
# char 문자

# a = [1, 2, 3]
# # print(a[2] + "hi")
# print(str(a[2]) + "hi")
# print(a[2] * "hi")
# #print(a[2] / "hi")
# a[2] = 4
# print(a)
# del a[0]
# print(a)

# a = [1, 2, 3, 7, 8]
# # b = [4,5,6]
# # print(a[0] + b[0])
# # print(b)
# # del a[1:]
# # print(a)
# del a[1:3]
# print(a)

# a = [1, 2 ,3]
# a.append(4)
# print(a)
# a.append([5, 6])
# print(a)

# a = [1, 4, 3, 2]
# a.sort()
# print(a)
# b = ['a', 'c', 'b']
# b.sort()
# print(b)
# c = ['a', 'c', 'b']
# c.sort()
# c.reverse()
# print(c)

a = [1, 2, 3, 2, 3, 4]
# print(a.index(2))
# print(a.index(5))
# a.insert(1, 4)
# print(a)
# 맨 첫 3 을 지운다
# a.remove(3)
# print(a)

# 뒤집고 지우고 뒤집고 -> 뒤에서 부터 삭제
# a.reverse()
# a.remove(3)
# a.reverse()
# print(a)

# 맨 뒤를 지운다 -> append 반대
# print(a.pop())
# print(a.pop(0))
# print(a)
# print(a.append(4))
# print(a)
# print(a.count(3))

# a = [1, 2, 3]
# a += [4]
# print(a)

# a = [1, 2, 3]
# a.extend([4, 5])
# a.append([6, 7])
# print(a)