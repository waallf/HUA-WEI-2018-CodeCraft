#coding=utf-8
import math
import pymatrix

def fun_diff(train_data):
    return [train_data[i]- train_data[i-1] for i in range(1,len(train_data))]

def fluth_data(train_data):
    # print("测试数据："+str(train_data))
    #差分
    diff = fun_diff(train_data)
    
    diff_sum = sum(diff)
    # print("差分: "+str(diff))
    #均值
    diff_average = diff_sum/float(len(diff))
    # print("均值："+str(diff_average))

    #标准差
    diff_delta  = sum([(diff_ - diff_average) **2 for diff_ in diff]) / float(len(diff))
    diff_delta = math.sqrt(diff_delta)
    # print("标准差："+str(diff_delta))


    yuzhi_high = diff_average + 1.5 * diff_delta
    # yuzhi_low = diff_average - 1.5* diff_delta
    


    ## 正向
    for i in range(0,len(train_data)-1):
        if train_data[i+1]-train_data[i]>yuzhi_high:
            train_data[i+1] = train_data[i]
            #diff = fun_diff(train_data)
            # print(str(diff[i])+"偏大")
        # elif diff[i]<yuzhi_low:
        #     train_data[i] = train_data[i-1]
        #     # print(str(diff[i])+"偏小")
        # else:
        #     pass
    ## 逆向
    for i in range(len(train_data)-2,-1,-1):
        #print(i)
        if (train_data[i] - train_data[i+1])>yuzhi_high:
            train_data[i] = train_data[i+1]
            #train_data[len(diff)-i] = train_data[len(diff)-i+1]
            #diff = fun_diff(train_data)
    return train_data
    
def quZao2(arr,input_nos):
    train_data=[]
    M = pymatrix.matrix(arr)
    M = M.transpose()
    for input_no in input_nos:
        temp = M.rowAt(input_no+1)
        #print(input_no,temp,type(temp))
        temp = fluth_data(temp)
        #print(temp)
        train_data.append(temp)
    #print(M)
    return train_data
    
if __name__ =="__main__":
    train_data = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(train_data))
    print("结果："+str(fluth_data(train_data))+str(len(fluth_data(train_data))))