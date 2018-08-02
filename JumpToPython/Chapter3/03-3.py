#문제1번
# for i in range(1,101):
#     print(i)

#문제2번
# result = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         result += i
# print(result)

#문제3번
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += score # A학급의 점수를 모두 더한다.
# average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
# print(average) # 평균 79.0이 출력된다

#문제4번
# blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB', 'A']
# result = {}
# for i in blood:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# print(result)

#문제5번
number = [1,2,3,4,5]
result = [n*2 for n in number if n %2 == 1]

print(result)
