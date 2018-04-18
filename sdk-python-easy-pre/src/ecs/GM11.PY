# coding=utf-8
import pymatrix
import math


####################################################################
## N：要预测的天数
## train_data：训练集，二维数组，其行数是测试集的天数，列数是虚拟机的规格数
## 
## 返回值：二维数组，行数是虚拟机的规格数，列数是预测的天数
####################################################################
def cumsum(arr):
    sum = 0
    res = []
    for a in arr:
        sum = sum + a
        res.append(sum)
    return res
def yuce(N,train_data):
    #train_data = pymatrix.matrix(train_data_list)
    #print(train_data)
    # size[0]是行数 size[1]是列数
    seq_len= len(train_data)
    #print(seq_len,flavor_num)
    # train_data是预测结果，数组的数组，第i个数组是规格i个预测结果
    # train_data = []
    old_train_data = train_data[:]
    print("oooooooooooooooooo",train_data)
    train_data = cumsum(train_data)
    print("SSSSSSSSSSSSS",train_data)
    res = 0   
    if(train_data[-1]==0):
        return 0
    #print(train_data)
    z = [[0]]*(seq_len-1)
    #print(u"白化之前："+str(z))
    for j in range(0,seq_len-1,1):
        z[j] = [0.5*(train_data[j]+train_data[j+1])]
    #print(u"白化背景之后： "+str(len(z))+str(z))
    z = pymatrix.matrix(z)
    z = z.numberSubMatrix(0)
    #print(u"-z="+str(z))
    B = [[1]]*(seq_len-1)
    B = pymatrix.matrix(B)
    B = z.heBing(B)
    #print(u"合并矩阵之后："+ str(B))
    
    u = B.transpose()*B
    #print(u"B的转置 "+str(B.transpose()))
    u = u.inverse()
    u = u * B.transpose()
    #print(u)
    #print(train_data)
    #print(u"子矩阵 "+str(train_data.subMatrix(2,seq_len,i,i)))
    # u = u * (train_data.subMatrix(2,seq_len,i,i))
    # u = u * train_data[1:seq_len]
    # print("u= "+str(u))
    # u1 = u[0][0]
    # u2 = u[1][0]
    sub_matrix = old_train_data[1:seq_len]

    u1 = sum(list(map(lambda x:x[0] *x[1],zip(u[0],sub_matrix))))
    u2 = sum(list(map(lambda x:x[0] *x[1],zip(u[1],sub_matrix))))
    print(u1,u2)
    left = train_data[0]- u2/u1
    #print("left= "+str(left))
    #print("u1= "+str(u1))
    right = u2/u1
    
    forecast1 = []
    # for t in range(seq_len-1,seq_len+N,1):
    for t in range(0,seq_len):
        forecast1.append(t)
    for i in range(0,len(forecast1),1):
        forecast1[i] = (-u1)*forecast1[i]
    for i in range(0,len(forecast1),1):
        forecast1[i] = math.exp(forecast1[i])
    for i in range(0,len(forecast1),1):
        forecast1[i] = left * forecast1[i]
    for i in range(0,len(forecast1),1):
        forecast1[i] = forecast1[i] + right

    #print(forecast1[-1]-forecast1[0])
    #print(forecast1)
       #exchange=[]
    #for i in range(1,len(forecast1),1):
    #    exchange.append(forecast1[i]-forecast1[i-1])
    return int(abs(round(forecast1[-1]-forecast1[0])))


if __name__ == "__main__":
    N = 7
    train_data=[2,3,4,5,6,7,8]
    print(yuce(N,train_data))
    #arr = [1,2,54,2,5]
    #print(sum(arr))
    #print(cumsum(arr))