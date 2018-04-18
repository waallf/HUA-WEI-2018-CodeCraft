#coding=utf-8
'''
77分
'''
import math

from collections import Counter
def cumsum(arr):
    sum = 0
    res = []
    for a in arr:
        sum = sum + a
        res.append(sum)
    return res
def easy_pre(flavor_list,test_time):
    flavor_list = cumsum(flavor_list)
    mean_add = flavor_list[-1] /float(len(flavor_list))
    efficity_add = len(list(set(flavor_list))) /float(len(flavor_list))

    predict1 = math.ceil(mean_add * efficity_add *test_time)

    mean_add = flavor_list[-1] *1.45 / float(len(set(flavor_list)) -1)

    predict2 = math.ceil(mean_add  * test_time)

    # d = flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.8)]
    #
    # s = float(int(len(flavor_list) * 0.2))
    if len(set(flavor_list[int(len(flavor_list) * 0.9):])) ==1:
        mean_add = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.9)]) / float(len(set(flavor_list[int(len(flavor_list) * 0.9):])))
    else:
        mean_add = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.9)]) / float(
            len(set(flavor_list[int(len(flavor_list) * 0.9):]))-1)


    predict3 = math.ceil(mean_add * test_time)
    if len(set(flavor_list[int(len(flavor_list) * 0.6):])) ==1:
        mean_add = ( flavor_list[-1] -  flavor_list[int(len(flavor_list) * 0.6)]) / float(len(set(flavor_list[int(len(flavor_list) * 0.6):])))
    else:
        mean_add = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.6)]) / float(
            len(set(flavor_list[int(len(flavor_list) * 0.6):])) - 1)
    predict4 = math.ceil(mean_add * test_time)
    #(predict2 *0.8055 +predict3 * 0.1797 + predict4*0.0148)
    return (predict2 *0.8055 +predict3 * 0.1797 + predict4*0.0148)
    # return ( predict2 )


# theta1 = 0.4
# theta2 = 1-theta1
#
#
# import math
# from collections import Counter
# def easy_pre(flavor_list,test_time): #test_time 是需要预测的时间长度
#     mean_add = flavor_list[-1] /float(len(flavor_list))   #均值，
#     efficity_add = len(list(set(flavor_list))) /float(len(flavor_list)) # 有效增长天数/总天数，有效增长天数是申请量不为0的天数
#
#     predict1 = math.ceil(mean_add *test_time)
#     '''
#      #总申请量/有效增长天数 1.5 瞎几把写的，-1是减去 一开始几天申请量为0 ，这里没加判断，也许前几天申请量不为0
#     '''
#     mean_add = flavor_list[-1] *1.5 / float(len(set(flavor_list)) -1)
#
#     predict2 = math.ceil(mean_add  * test_time)
#     # predict2 = (predict1*theta1 + predict2*theta2)
#
#     '''
#     predict1 < Truth < predict2
#     '''
#
#     '''
#     总申请量减去前面一段时间，然后除以这段时间内的有效申请天数，最后乘以权重
#     '''
#     mean_add1 = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.9)]) / float(len(set(flavor_list[int(len(flavor_list) * 0.9):])))
#     mean_add2 = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.9)]) / float(len(flavor_list[int(len(flavor_list) * 0.9):]))
#     mean_add = (mean_add1*theta1 + mean_add2 * theta2)
#     predict3 = math.ceil(mean_add * test_time)
#
#     mean_add1 = ( flavor_list[-1] -  flavor_list[int(len(flavor_list) * 0.6)]) / float(len(set(flavor_list[int(len(flavor_list) * 0.6):])))
#     mean_add2 = (flavor_list[-1] - flavor_list[int(len(flavor_list) * 0.6)]) / float(
#         len(flavor_list[int(len(flavor_list) * 0.6):]))
#     mean_add = (mean_add1 * theta1 + mean_add2 * theta2)
#     predict4 = math.ceil(mean_add * test_time)
#
#     rate = (flavor_list[-1] - flavor_list[len(flavor_list) - test_time])/(flavor_list[len(flavor_list) - test_time] - flavor_list[len(flavor_list) - 2*test_time])
#
#     mean_add1 = (flavor_list[-1] - flavor_list[len(flavor_list) -  test_time]) *1.5/ float(
#         len(set(flavor_list[len(flavor_list) -  test_time:])))
#     mean_add2 = (flavor_list[-1] - flavor_list[len(flavor_list) - test_time]) * 1.5 / float(
#         len(flavor_list[len(flavor_list) - test_time:]))
#     mean_add = (mean_add1 * theta1 + mean_add2 * theta2)
#     predict5 = math.ceil(mean_add * test_time)
#
#     return (predict2 *0.7+predict3 * 0.2 + predict4*0.1+ predict5 * 0.3)
#     # return ( predict2 )
#
