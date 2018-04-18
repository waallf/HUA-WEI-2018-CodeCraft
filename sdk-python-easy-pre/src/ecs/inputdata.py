#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from fluth_data import fluth_data
def read_inputfile(train_fileapth,input_filepath,threshold ):
	'''
	
	:param train_fileapth:训练文件名称
	:param input_filepath: 测试文件名称
	:return: 
	guige:[cpu num , mem num]
	flavor_name"{"flavor" :[cpu_num,mem_num], ...}
	cpu_mem :CPU OR MEM
	label_Mat:训练数据
	test_time:需要测试的时间长度
	'''
	data = open(input_filepath).readlines()
	guige = data[0].split()
	shuliang = int(data[2])
	flavor_name = {i.split(" ")[0]:[int(i.split(" ")[1].strip("\n")),int(i.split(" ")[2].strip("\n"))] for i in data[3:shuliang + 3]}

	cpu_mem = data[shuliang + 4].strip("\n").strip("\r")

	startTime = data[shuliang + 6].strip("\n").strip("\r").split(" ")[0]
	stopTime = data[shuliang + 7].strip("\n").strip("\r").split(" ")[0]

	start_weekday,label_Mat = read_train_file(train_fileapth, flavor_name,threshold,startTime)
	test_time = getday(startTime,stopTime) 
	start_test_weekday = date_change(startTime) % 7
	return guige,flavor_name,cpu_mem,label_Mat,test_time,start_weekday,start_test_weekday


def read_train_file(train_fileapth,flavor_name,threshold,startTime):

	data2 = open(train_fileapth).readlines()

	# 计算第一天的Unix时间戳
	start = data2[0].split("\t")[2].strip("\n").strip("\r").split(" ")[0]
	start_weekday = date_change(start) % 7
	# 计算最后一天
	stop = getday(start,data2[-1].split("\t")[2].strip("\n").strip("\r"))
	# 定义二维数组用以计数
	if getday(data2[-1].split("\t")[2].strip("\n").strip("\r"),startTime)!=1:
		stop = stop + getday(data2[-1].split("\t")[2].strip("\n").strip("\r"),startTime)-1

	print(stop)
	N = [[0] * (stop + 1) for x in xrange(len(flavor_name.keys()))]
	# 计数
	sumup = 0
	for j in data2:
		m = j.strip("\n").split("\t")
		try:

			mm = list(flavor_name.keys()).index(m[1])

			s = getday(start, m[2].strip("\r"))

			N[mm][getday(start,m[2].strip("\r"))] = N[mm][getday(start,m[2].strip("\r"))]+1


		except:
			continue
	# print("N",N)
	# 捋一捋
	# print(list(flavor_name.keys()))
	print("去燥前",N)
	for N_index,i in enumerate(N):

		i = flouth_data(i, threshold)# 数据去噪
		# print("过滤前")
		# print(i)
		# i = fluth_data(i)
		# print("过滤后")
		# print(i)

		'''
		注释掉下面是预测当日申请量，不注释是累计量
		'''
		# n = i[:]
		# index = i.index(0, 1)
		# for j in range(index ,len(i)):
		# 	n[j] = sum(i[:j+1])
		# N[N_index] = n[:]
	# ######################################################################################
	print("去燥后",N)
	# print("********************************************")
	return start_weekday,N
#用于日期换算
def date_change(date):
	timeArray = time.strptime(date, "%Y-%m-%d")
	timeStamp = int(time.mktime(timeArray))
	return timeStamp/86400
def getday(start,stop):
	start= start.split(" ")[0]
	stop =  stop.split(" ")[0]
	s = date_change(start)
	e = date_change(stop)
	return e-s
def flouth_data(L, threshold):#对数据进行去燥
	if len(L) - L.count(0) !=0:
		mean_incres = float(sum(L)- L[0])/(len(L) - L.count(0))
		for i in range(len(L)-1):
			if L[i + 1] - L[i] > mean_incres * threshold:
				L[i + 1] =  0
	return L

if __name__ =="__main__":
	guige,flavor_name,cpu_mem,label_Mat,test_time,start_weekday,start_test_weekday = read_inputfile("xunlianji.txt","input.txt",threshold = 2)
	# print(guige)
	# print(flavor_name)
	print(cpu_mem)
	print(label_Mat)
	print(test_time)
# [3, 6, 2, 2, 0, 3, 4, 7, 7, 3, 4, 0, 0, 4, 1, 5, 3, 3, 3, 0, 6, 2, 4, 7, 7, 2, 1, 1, 2, 3, 1, 0, 2, 1, 1, 0, 6, 2, 1, 0, 2, 1, 4, 3, 10, 2, 3, 1, 3, 3, 2, 5, 10, 1, 2]
# [10, 2, 0, 1, 1, 0, 3, 1, 1, 6, 9, 2, 1, 0, 6, 2, 5, 4, 1, 2, 2, 5, 5, 1, 8, 3, 5, 12, 6, 6, 5, 1, 0, 1, 2, 5, 1, 9, 0, 1, 0, 7, 1, 9, 9, 2, 3, 1, 4, 0, 4, 6, 4, 6, 5]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# [2, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 2, 0, 2, 1, 2, 1, 3, 1, 1, 0, 0, 0, 2, 0, 1, 2, 0, 1, 1, 1, 6, 1, 3, 1, 1, 1, 0, 2, 2, 1, 0, 1]
# [0, 2, 3, 2, 0, 8, 4, 2, 1, 2, 1, 0, 3, 4, 4, 5, 2, 3, 2, 0, 5, 4, 4, 4, 0, 2, 4, 6, 2, 2, 3, 4, 1, 3, 3, 4, 8, 0, 1, 2, 9, 5, 0, 5, 7, 2, 0, 2, 1, 1, 2, 9, 1, 0, 1]
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 2, 2, 2, 2, 1, 1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0]
# [3, 9, 3, 0, 0, 11, 0, 0, 2, 3, 0, 0, 4, 17, 0, 4, 8, 1, 2, 0, 6, 11, 2, 12, 20, 8, 0, 0, 2, 0, 17, 1, 2, 1, 1, 6, 7, 7, 0, 0, 2, 8, 4, 11, 8, 1, 0, 5, 9, 4, 16, 10, 3, 3, 7]
# [2, 1, 1, 0, 0, 1, 0, 1, 1, 3, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 4, 4, 0, 0, 2, 0, 5, 6, 1, 0, 1, 0, 0, 5, 2, 2, 1, 5, 0, 0, 0, 1, 1, 1, 4, 0, 2, 3, 1, 3, 1, 3, 0, 1]
# [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0, 1, 2, 1, 1, 1, 0, 0, 0, 0, 5, 3, 0, 0, 1, 2, 2, 1, 1, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2, 9, 9, 0, 0, 2, 0, 5, 3, 0, 1, 1, 3, 0, 0, 3, 0, 0, 0, 2]
# [0, 0, 2, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 1, 5, 6, 0, 10, 0, 0, 3, 0, 0, 2, 0, 4, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 3, 1, 0, 0, 7, 0, 0]
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 3, 2, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]




