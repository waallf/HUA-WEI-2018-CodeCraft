# coding=utf-8
import re
from  logist import create_result
from memory_alloction import get_memory_allocation
from inputdata import read_inputfile
from collections import Counter
def predict_vm(ecsDataPath, inputFilePath,resultFilePath,k,threshold ):
    # Do your work from here#
    all_hat =[]
    all_hat_name = []
    pre_dic={}
    #徐劲夫，将源文件转化为列表,dataMat = [1,2,3,4,.....] 按时间序列排序，labelMat = [] #对应申请量
    guige, flavor_name, cpu_mem, label_Mat,test_time = read_inputfile(ecsDataPath, inputFilePath,threshold )

     #要申请的是CPU OR MEM
    if cpu_mem =="CPU":
        zero_one = 0
    elif cpu_mem =="MEM":
        zero_one = 1
    else:
        raise ("memory_alloction_name must be CPU OR MEM")
    dateMat = [i for i,_ in enumerate(label_Mat[0])]
    testMat =  [i+len(dateMat) for i  in range(test_time)]
    for index,f_n in enumerate(flavor_name):
        flavor = flavor_name.values()[index]
        flavor_cpu_or_mem = int(flavor[zero_one] if not zero_one else flavor[zero_one] /1024)
        labelMat = label_Mat[index]


        yhat = create_result(testMat,dateMat,labelMat,k)# 每一预测种类返回一个预测序列
        pre = yhat[-1] - labelMat[-1] #计算预测 申请了多少台虚拟机
    #将Yhat 传入memory_alloction 进行内存分配
        all_hat.extend( [flavor_cpu_or_mem]* pre)
        all_hat_name.extend([f_n]*pre)
        pre_dic[f_n] = pre  #{"flavor" :pre,....}

    result = get_memory_allocation(guige[zero_one], all_hat,all_hat_name)
    all_flavor = len(all_hat) #预测虚拟机总数
    need_xuniji_num = len(result)
    output_writer(all_flavor,pre_dic,result,need_xuniji_num,resultFilePath)

    '''
    6
    flavor5  3
    flavor10  2
    flavor15  1
   
    4
    1  flavor5  2
    2  flavor5  1  flavor10  1
    3  flavor15  1
    4  flavor10  1
    '''

def output_writer(all_flavor,pre_dic,result,need_xuniji_num,resultFilePath):
    file = open(resultFilePath,"w")
    result_list = []
    for i in result:
        result_list.append(dict(Counter(i)))
    file.write(str(all_flavor)+"\n")
    pre_dic = sorted(pre_dic.items(), key=lambda x: x[0])
    [file.write(key+"\t"+str(value)+"\n") for (key,value) in pre_dic]
    file.write("\n")
    file.write(str(need_xuniji_num)+"\n")

    for index,i in enumerate(result_list):
        i = dict(i)
        file.write(str(index+1)+"\t")
        [file.write(key + "\t" + str(value)+"\t") for  key, value in i.items()]
        file.write("\n")




if __name__ == "__main__":
    threshold = 2
    k = 0.7
    predict_vm("TrainData_2015.1.1_2015.2.19.txt","input_5flavors_cpu_7days.txt","out_put.txt",k,threshold)
