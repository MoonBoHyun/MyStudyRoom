#문제1번
# a = [1,2,3]
# b = [1,2,3]
# c = a is b
# print(c)
#리스트는 같지만 서로 다른 객체이다

#문제2번
# a = [1,2,3]
# b = a
# c = a is b
# print(c)
#b = a 로 해줌으로써 바라보는 객체가 같아진다.

# 문제1번과 문제2번의 차이점을 명확히 알아두자!

#문제3번
# a = b = [1,2,3]
# a[1] = 4
# print(a)
# print(b)
#a와b 모두 동일한 [1,2,3]이라는 리스트 객체를 가리키고 있다.

#문제4번
# a = [1,2,3]
# b = a[:]
# c = a is b
# print(c)
#복사를 해줌으로써 새로운 값을 바라본다

#문제5번
# a = [1,2,3]
# b = a[:]
#
# a[1] = 4
# print(a)
# print(b)
#copy를 해서 새로운 값을 바라보기 때문에  서로 다른 객체이기때문에 값을 다르게 출력해준다

#문제6번
#더하기를 해주면 새로운 리스트가 리턴되지만 extend를 해주면 주소값이 변하지 않고 그대로 유지된다.

#문제7번
a = [1, [2, 3], 4]
b = a[:]
a[1][0] = 5
print(a)
print(b)