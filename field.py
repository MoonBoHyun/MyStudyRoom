#!/usr/bin/python
# -*- coding:utf-8 -*-
  
import string
import os
import sys
path = os.getcwd();

f = open('/user1/sireroot/DATASET/sireroot/data1/searchfile/PoiData_All.txt','r')
result1 = open('result_field.txt','w')
lines = f.readlines()

count = 0

for line in lines:
	words_list = line.split('|')
	
	if line.count('|') > 22:
		print(line)
		count += 1
	elif words_list[12] == '':
		
		result1.write(line)
		line222 = line
	else:
		pass


print(' |가 초과된 갯수')
print(count)

result1.close()
result1 = open('result_field.txt','r')
print('13번쨰의 필드의 공백인 수는')
print(result1.read().count('\n')+1)
result1.close()

f.close()
