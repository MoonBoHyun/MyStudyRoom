import re

def algo(list_1, list_2):
    print("검색")
    list_1 = re.sub('[^가-힣ㄱ-ㅎa-zA-Z]+', "", list_1) #string에서 pattern과 일치하는 부분에 대하여 교체하고 결과 문자열을 반환(정규표현식 사용)
    list_2 = re.sub('[^가-힣ㄱ-ㅎa-zA-Z]+', "", list_2)

    list_1 = list(list_1) #문자열을 리스트로 변환
    list_2 = list(list_2)

    print(list_1)
    print(list_2)

    list_intersection = list(set(list_1).intersection(list_2)) #intersection함수를 이용하여 list_1과 list_2의 교집합을 구해준다

    temp = [x for x in list_1 if x not in list_2] #list_2에 없는 요소를 list_1과 비교하여 출력해준다

    try:
        a = 0
        while True:
            if list_1 == list_2:
                print("검색한 문자열이 정확히 일치합니다")
                break
            if list_1[a:a + len(list_2)] == list_2 and a == 0: #0부터 시작해서 list_2의 길이까지가 list_2와 일치하며 시작점이 0일때
                print("검색한 문자열을 앞에서 찾았습니다")
                return list_1
                break
            if list_1[a:a + len(list_2)] == list_2 and 0 < a and list_1[-1] != list_2[-1]: #0부터 시작하였지만 a값이 0이상이고 list_1과 list_2의 맨 뒷자리가 일치하지 않을때
                print("검색한 문자열을 중간에서 찾았습니다")
                return list_1

            if list_1[a:a + len(list_2)] == list_2 and 0 < a and list_1[-1] == list_2[-1]: #0부터 시작하고 a값이 0이상이고 list_1과 list_2의 맨 뒷자리가 일치할때
                print("검색한 문자열을 뒤에서 찾았습니다")
                return list_1

            a = a + 1

            if a == len(list_1) + len(list_2): #a의 값이 list_1의 길이와 list_2의 길이를 합친것과 같아지면
                break

    except ValueError:
        print("값이 없습니다")

    if len(list_intersection) > 0 or len(list_2) < 2:
        print("부정확")
    elif temp == list_1 or temp not in list_1:
        print("불일치")



def main():

    str1 = input('문자열1을 입력하세요 : ') #문자열로 입력 받음
    str2 = input('문자열1에서 검색할 문자열을 입력하세요 : ') #문자열로 입력 받음

    if len(str1) < len(str2): #만약 str1 문자열의 길이보다 str2 문자열의 길이가 더 길면
        print("참고할 만한 글자의 갯수가 더 적습니다.")
    algo(str1, str2) #아닐경우에 algo() 실행

main()