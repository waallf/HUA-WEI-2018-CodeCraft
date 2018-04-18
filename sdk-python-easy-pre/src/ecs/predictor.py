#coding=utf-8
from collections import Counter
import math
from inputdata import read_inputfile

from memory_alloction import get_memory_allocation

from monituihuo import tuihuo
# from draw_predict_pic import Draw

from easy_pre import easy_pre
# from Markov import Markov
# from  logist import create_result
# from week_day_pre import week_day_pre
# from Locallyweightedlinearregression import lwlrTest
# from zhishupinghua import zsph
# from GM11 import yuce
# from zhishupinghua_ import zsph_



def predict_vm(ecsDataPath, inputFilePath,resultFilePath,dict_k,threshold):
    # Do your work from here#
    all_hat =[]
    all_hat_name = []
    all_hat_limit = []
    pre_dic={}
    flavor_num_less_8 = []

    select_pre_func_thread1 =  10 #选择不同函数的阈值
    select_pre_func_thread2 = 25
    #徐劲夫，将源文件转化为列表,dataMat = [1,2,3,4,.....] 按时间序列排序，labelMat = [] #对应申请量
    guige, flavor_name, cpu_mem, label_Mat,test_time,start_weekday,start_test_weekday = read_inputfile(ecsDataPath, inputFilePath,threshold )

     #要申请的是CPU OR MEM
    if cpu_mem =="CPU":
        zero_one = 0
    elif cpu_mem =="MEM":
        zero_one = 1
    else:
        raise ("memory_alloction_name must be CPU OR MEM")


    # for index,f_n in enumerate(flavor_name):
    #     flavor = flavor_name.values()[index]
    #     flavor_cpu_or_mem = int(flavor[zero_one] if not zero_one else flavor[zero_one] /1024)
    #     labelMat = label_Mat[index]
    #
    #
    #     yhat = create_result(testMat,dateMat,labelMat,k)# 每一预测种类返回一个预测序列
    #     pre = yhat[-1] - labelMat[-1] #计算预测 申请了多少台虚拟机
    # #将Yhat 传入memory_alloction 进行内存分配
    #     all_hat.extend( [flavor_cpu_or_mem]* pre)
    #     all_hat_name.extend([f_n]*pre)
    #     pre_dic[f_n] = pre  #{"flavor" :pre,....}
    # result = get_memory_allocation(guige[zero_one], all_hat, all_hat_name)
    for index, f_n in enumerate(flavor_name):
        flavor = flavor_name.values()[index]
        flavor_cpu_or_mem = int(flavor[zero_one] if not zero_one else flavor[zero_one] / 1024)
        flavor_cpu_or_mem_limit = int(flavor[1 - zero_one] if zero_one else flavor[1-zero_one] / 1024)
        labelMat = label_Mat[index]
        dateMat = [i for i, _ in enumerate(label_Mat[index])]
        testMat = [i + len(dateMat) for i in range(test_time)]

        ##################################################################################################################################
        k = dict_k[str(f_n)]
        '''
        下面几行是使用局部加权线性回归进行预测
        '''
        # yhat = create_result(testMat, dateMat, labelMat, k)  # 每一预测种类返回一个预测序列
        '''
        下面两行，第一行是进行累积量预测，出现bug，第二行是预测单日申请量
        
        修改是累积量，还是单日申请量，在inputdata.py文件63-67行
        '''
        # pre = yhat[-1] - labelMat[-len(yhat)-1]  # 计算预测 申请了多少台虚拟机  # 预测的是累计量
        # pre = sum(yhat)  # 预测当日申请量
        # if pre <= 0: pre = 2
        ##################################################################################################

        '''
        下面两行是使用均值大法进行预测，这里必须使用累积量进行预测
        # n = labelMat[:]
        # index = labelMat.index(0, 1)
        # for j in range(index, len(labelMat)):
        #     n[j] = sum(labelMat[:j + 1])
        #
        '''
        

        yhat = easy_pre(labelMat, test_time)
        pre = int(yhat)



        # if sum(labelMat[-test_time:]) <= select_pre_func_thread1 or sum(
        #         labelMat[-test_time:]) > select_pre_func_thread2:

        # else:
        #     '''
        #     Markov 进行预测,不累加

        #     '''
        # pre = Markov(labelMat,test_time)

        '''
        使用对应的星期进行预测,按单日量进行预测

        '''
        # pre = week_day_pre(start_weekday, labelMat, start_test_weekday, test_time)

        '''
        局部加权线性回归@ 累积量
        # n = labelMat[:]
        # for j in range(len(labelMat)):
        #     n[j] = sum(labelMat[:j + 1])
        '''
        

        # yhat = lwlrTest(testMat,dateMat,labelMat,k)
        # pre = int((yhat[-1]- yhat[0]))
        print(f_n)
        '''
        指数平滑
        # n = labelMat[:]
        # for j in range(len(labelMat)):
        #     n[j] = sum(labelMat[:j + 1])
        '''
        # a = 0.3
        # yhat = zsph(labelMat,test_time,a)
        # pre = int((yhat[-1]- yhat[0]))
        # print("pre",pre)
        '''
        指数平滑_
        '''
        # pre = zsph_(labelMat,test_time,alpha = 0.6)
        # print("pre",pre)
        '''
        GM11
        '''
        # pre = yuce(test_time,labelMat)
        # print("pre",pre)
        '''
        画图
        '''
       
        # Draw(yhat, dateMat, n)




        # 将Yhat 传入memory_alloction 进行内存分配
        if pre !=0 :#pre != 0
            all_hat.extend([flavor_cpu_or_mem] * pre)
            all_hat_limit.extend([flavor_cpu_or_mem_limit] * pre)
            all_hat_name.extend([f_n] * pre)

        if int(f_n[6:]) < 8:
            flavor_num_less_8.append(f_n)
        pre_dic[f_n] = pre  # {"flavor" :pre,....}
    print("ssssss",list(sorted(pre_dic.items(),key = lambda x:x[0])))
    result, delet, liyonglv = get_memory_allocation(zero_one, guige[zero_one], guige[1 - zero_one], all_hat,
                                                    all_hat_limit, all_hat_name)
    print(liyonglv)


    '''
    对小于8的机型加个值，让分配率最大
    '''
    list_add_pre_less_8 = [0] * len(flavor_num_less_8)
    best_list_add_pre_less_8 = list_add_pre_less_8[:]
    print(len(flavor_num_less_8))
    best_liyonglv = 0
    best_result = []
    orig_all_hat = all_hat[:]
    orig_all_hat_limit = all_hat_limit[:]
    orig_all_hat_name = all_hat_name[:]
    orig_pre_dic = pre_dic.copy()
    for i in range(4**len(flavor_num_less_8)):
        t =i
        all_hat = orig_all_hat[:]
        all_hat_limit = orig_all_hat_limit[:]
        all_hat_name = orig_all_hat_name[:]
        pre_dic = orig_pre_dic.copy()
        for j in range(len(flavor_num_less_8)):
            list_add_pre_less_8[j] = t % 4
            t = t/4
        for list_index,n in enumerate(list_add_pre_less_8):
            pre_dic[flavor_num_less_8[list_index]] = pre_dic[flavor_num_less_8[list_index]] + n
            flavor = flavor_name[flavor_num_less_8[list_index]]

            flavor_cpu_or_mem = int(flavor[zero_one] if not zero_one else flavor[zero_one] / 1024)
            flavor_cpu_or_mem_limit = int(flavor[1 - zero_one] if zero_one else flavor[1-zero_one] / 1024)
            f_n =flavor_num_less_8[list_index]
            if n !=0:
                all_hat.extend([flavor_cpu_or_mem] * n)
                all_hat_limit.extend([flavor_cpu_or_mem_limit] * n)
                all_hat_name.extend([f_n] * n)
        xunhuan_result,delet,xunhaun_liyonglv = get_memory_allocation(zero_one,guige[zero_one], guige[1 - zero_one], all_hat, all_hat_limit, all_hat_name)
        print("liyonglv",xunhaun_liyonglv)
        if xunhaun_liyonglv> best_liyonglv:
            best_liyonglv = xunhaun_liyonglv
            best_result = xunhuan_result[:]
            best_pre = pre_dic.copy()
            best_all_hat = all_hat[:]
            best_list_add_pre_less_8 = list_add_pre_less_8[:]
            # best_flavor_num_less_8 = flavor_num_less_8
    print("best_liyonglv:",best_liyonglv)
    # print("list_add_pre_less_8:",list_add_pre_less_8)
    # print("pre_dic:",pre_dic)
    if  (best_liyonglv - liyonglv < 0.02) and sum(best_list_add_pre_less_8)<10:
        best_result = result[:]
        best_pre = orig_pre_dic.copy()
        best_all_hat = orig_all_hat[:]


    # result = tuihuo(zero_one, guige[zero_one], guige[1 - zero_one], all_hat, all_hat_limit, all_hat_name)

    # for key,value in delet.items():
    #     pre_dic[key] = pre_dic[key] - value
    all_flavor = len(best_all_hat) #预测虚拟机总数
    need_xuniji_num = len(best_result)

    output_writer(all_flavor,best_pre,best_result,need_xuniji_num,resultFilePath)

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
    line_result = []
    for i in result:
        line_result.extend(i)
        result_list.append(dict(Counter(i)))

    line_result_dict = dict(Counter(line_result))
    # for k,v in line_result_dict.items():
    #     assert pre_dic[k] == v


    pre_dic = sorted(pre_dic.items(), key=lambda x: x[0])
    file.write(str(all_flavor) + "\n")
    [file.write(key+" "+str(value)+"\n") for (key,value) in pre_dic]
    file.write("\n")
    file.write(str(need_xuniji_num)+"\n")

    for index,i in enumerate(result_list):
        dict_i = dict(i)
        file.write(str(index+1))
        [file.write(" "+key + " " + str(value)) for  key, value in dict_i.items()]
        if index+1<len(result_list):
            file.write("\n")




if __name__ == "__main__":
    threshold =2
    k = 6
    dict_k = {
        'flavor1':k,
        'flavor2':k,
        'flavor3':k,
        'flavor4':k,
        'flavor5':k,
        'flavor6':k,
        'flavor7':k,
        'flavor8':k,
        'flavor9':k,
        'flavor10':k,
        'flavor11':k,
        'flavor12':k,
        'flavor13':k,
        'flavor14':k,
        'flavor15':k
    }
    # predict_vm("TrainData_2015.1.1_2015.5.19.txt","input_5flavors_cpu_7days.txt","out_put_4.txt",dict_k,threshold)
    predict_vm("TrainData_2015.1.1_2015.5.19.txt","input_5flavors_cpu_7days.txt","out_put_4.txt",dict_k,threshold)
