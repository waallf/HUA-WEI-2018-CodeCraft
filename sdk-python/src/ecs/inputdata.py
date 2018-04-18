#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

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

	startTime = data[shuliang + 6].strip("\n").strip("\r")
	stopTime = data[shuliang + 7].strip("\n").strip("\r")
	label_Mat = read_train_file(train_fileapth, flavor_name,threshold)
	test_time = getday(startTime,stopTime) +1
	return guige,flavor_name,cpu_mem,label_Mat,test_time


def read_train_file(train_fileapth,flavor_name,threshold):

	data2 = open(train_fileapth).readlines()

	# 计算第一天的Unix时间戳
	start = data2[0].split("\t")[2].strip("\n").strip("\r")
	# 计算最后一天
	stop = getday(start,data2[-1].split("\t")[2].strip("\n").strip("\r"))
	# 定义二维数组用以计数

	N = [[0] * (stop + 1) for x in xrange(len(flavor_name.keys()))]
	# 计数
	sumup = 0
	for j in data2:
		m = j.strip("\n").split("\t")
		try:
			q = m[1]
			a= list(flavor_name.keys())
			mm = list(flavor_name.keys()).index(m[1])

			N[mm][getday(start,m[2].strip("\r"))] = N[mm][getday(start,m[2].strip("\r"))]+1


		except:
			continue
	# 捋一捋
	for N_index,i in enumerate(N):

		i = flouth_data(i, threshold)
		n = i[:]
		index = i.index(0, 1)
		for j in range(index ,len(i)):

			n[j] = sum(i[:j+1])
		N[N_index] = n[:]
	# ######################################################################################
	return N
#用于日期换算
def date_change(date):
	timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
	timeStamp = int(time.mktime(timeArray))
	return timeStamp/86400
def getday(start,stop):
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
	guige, flavor_name, cpu_mem, label_Mat, test_time = read_inputfile("TrainData_2015.1.1_2015.2.19.txt","input_5flavors_cpu_7days.txt",threshold = 2)
	# print(guige)
	# print(flavor_name)
	print(cpu_mem)
	print(label_Mat)
	print(test_time)

