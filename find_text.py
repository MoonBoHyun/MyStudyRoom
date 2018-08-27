#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import glob

path = os.getcwd(); #현재 경로 저장

#변수에다가 현재 경로와 /를 추가해줌으로써 원하는 파일을 input으로 받아준다
full_path = path + '/' + raw_input("파일 입력하시오: ")
full_path2 = path + '/' + raw_input("파일 입력하시오: ")
full_path3 = [full_path,full_path2]

#이건 그냥 .py라는 파일의 내역이 뭐가 있는지 보기위해 출력해주는 구문이다.
for x in glob.glob('*.py'):
        print(x)
        print('---------------------------------------')
try:
	#파일을 합칠지 말지의 여부를 물어봐주는 구문
        chk_dist = raw_input("합치시겠습니까?[press y to continue..] : ")
        if chk_dist.strip() == 'y' or chk_dist.strip() == 'Y':
		#만약 yes를 선택했는데 파일이 없을수도 있으니 os.path.exists
		#로 파일 여부를 확인해준다.
                if os.path.exists(full_path) and os.path.exists(full_path2):
			#만약 합칠 두개의 파일이 둘 다 존재하면 
			#result.txt라는 txt파일을 만들고 'w'로 써주기를
			#해줌으로써 한줄씩 읽고 써준다. 
                        with open('result.txt', 'w') as outfile:
                                for fname in full_path3:
                                        with open(fname) as infile:
                                                for line in infile:
                                                        outfile.write(line)\
		#만약 없다면 
                else:
                        print("파일명을 다시 확인해주세요")
	#만약 y,Y를 선택하지 않았다면
        else:
                print("ok byebye")


except Exception as err:
        print("파일이 존재하지 않습니다.")
        print(err)

