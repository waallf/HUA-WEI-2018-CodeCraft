#coding=utf-8
import math
def cumsum(arr):
    sum = 0
    res = []
    for a in arr:
        sum = sum + a
        res.append(sum)
    return res
def zsph_(train_data,test_time,alpha):
    print("qian:",train_data)
    # train_data = train_data[:55]
    slice_num  =math.ceil(test_time/2.0)


    # print("leijia", train_data)
    train_data = slice(train_data,slice_num)
    train_data = cumsum(train_data)
    print("leijia", train_data)
    s1 = [0] * len(train_data)
    s2 = [0] * len(train_data)
    s3 = [0] * len(train_data)
    # alpha = [0.4] * 30


    t = train_data

    s1[0] = t[1]
    for j in range(1, len(s1), 1):
        s1[j] = alpha * train_data[j] + (1 - alpha) * s1[j - 1]
    s2[0] = s1[1]
    for j in range(1, len(s2), 1):
        s2[j] = alpha * s1[j] + (1 - alpha) * s2[j - 1]
    s3[0] = s2[1]
    for j in range(1, len(s3), 1):
        s3[j] = alpha * s2[j] + (1 - alpha) * s3[j - 1]
    print("s1= " + str(s1))
    print("s2= " + str(s2))
    print("s3= " + str(s3))

    a = 3 * s1[-1] - 3 * s2[-1] + s3[-1]
    b = alpha / (2.0 * (1 - alpha) ** 2) * (
                (6 - 5 * alpha) * s1[-1] - 2 * (5 - 4 * alpha) * s2[-1] + (4 - 3 * alpha) * s3[-1])
    c = alpha ** 2 / (2 * ((1 - alpha) ** 2)) * (s1[-1] - 2 * s2[-1] + s3[-1])
    print("a= " + str(a))
    print("b= " + str(b))
    print("c= " + str(c))

    yuce1 = a + b + c
    sign =((slice_num - 1) / slice_num)
    yuce2 = (a + (2 + sign)* b + ((2 + sign)**2)* c)
    # yuce3= (a + 3 * b + 9 * c) *

    yuce = yuce2 - yuce1
    yuce = round(yuce)
    if yuce < 0:
        yuce = 0
    # print(u"预测值为 " + str(yuce))
    # name = "flavor" + str(i + 1)
    yuce_flvorname_flavornum_s = int(yuce)

    return yuce_flvorname_flavornum_s
def preprocess(arr, N):
    N = int(N)
    t1 = len(arr) % N
    t2 = int(len(arr) / N)

    res = []
    for i in range(t2):
        temp = arr[t1 + N * i:t1 + N * i + N:1]
        # print(temp)
        # print(sum(temp))
        res.append(sum(temp))
        # print(i,t1+N*i,t1+N*i+N)
    return res


def slice(arr, N):
    arr = [0] + arr
    temp = preprocess(arr[1::1], N)
    return [0] +temp
if __name__ =="__main__":
    train_data =  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1];

    test_time = 7
    # pre = zsph_(train_data,test_time)
    # print(pre)
    print(preprocess(train_data,test_time))

