#문제1번
# print('"점프 투 파이썬" 문제를 풀어보자 ')

#문제2번
# print("Life is too short\nYou need Python")

#문제3번
# print("                        PYTHON")
# print(' '*24 + "PYTHON")

#문제4번
# h = "881120-1068234"
# year = int(h[0:2]) + 1900
# month = h[2:4]
# day = h[4:6]
# extra = h[7:14]
# print("홍길동씨의 생년월일은",year,"년도",month,"월",day,"일 입니다")
# print("나머지 숫자는",extra)

#문제5번
# pin = "881120-1068234"
# if int(pin[7:8]) == 1:
#     print("남자")
# else:
#     print("여자")

#문제6번
# str = "1980M1120"
# print(str[4:5] + str[0:4] + str[5:9])

#문제7번
# print(' '*24 + "PYTHON")

#문제8번
# str = "Life is too short, you need python"
# print(str.find("short"))

#문제9번
# str = "a:b:c:d"
#
# a = str.replace("a:b:c:d","a#b#c#d")
#
# print(a)

#문제10번
str = "a:b:c:d"
a = str.split(":")
b = "#"
c = b.join(a)
print(c)