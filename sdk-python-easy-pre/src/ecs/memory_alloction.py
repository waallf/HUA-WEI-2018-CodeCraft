# coding=utf-8
from collections import  Counter
import time
def commonFit(free_spaces,append_limit, memory_requests, fit_func,memory_reqquest_list_limit,all_hat_name):
    fit_spaces = [0]*(len(free_spaces))
    fit_spaces_limit = [0]*(len(free_spaces))
    fit_blocks = [[] for i in range(len(free_spaces))]
    fit_blocks_usefull = [[] for i in range(len(free_spaces))]
    num_fitted = 0
    delte = {}

    for index,memory_request in enumerate(memory_requests):
        all_hat_name_ = all_hat_name[index]
        memory_reqquest_list_limit_ = memory_reqquest_list_limit[index]
        fitted,fit_spaces,fit_spaces_limit,fit_blocks,fit_blocks_usefull= fit_func(free_spaces, append_limit,memory_request, fit_spaces, fit_spaces_limit,fit_blocks,fit_blocks_usefull,memory_reqquest_list_limit_,all_hat_name_)
        num_fitted += fitted
        if fitted ==0:
            free_spaces.append(free_spaces[0])
            return 0,0,0,0
    success = num_fitted / float(len(memory_requests))
    '''
    判断前几个物理机的利用率是否是百分之一百，如果是，而且最后一个物理机利用率较低就将其去掉，因为分配的利用率分支影响会比预测值的影响要大
    
    '''
    use_full = list(sum(i) for i in fit_blocks_usefull)
    use_full = dict(Counter(use_full))
    if use_full.get(free_spaces[0],0) == (len(fit_blocks_usefull) -1) and len(fit_blocks_usefull[-1]) < 2:#如果前几个物理机的利用率都是100 ，而且最后一个物理机只有小于两个申请，那么久把这几个给去掉
        delte = dict(Counter(fit_blocks_usefull[-1]))


    for inedx in range(len(fit_blocks_usefull)):
        if fit_blocks_usefull[-1] == []:
            fit_blocks_usefull.pop(-1)
    all_sum =0#用于计算物理机的利用率
    for i in fit_blocks_usefull:
        all_sum += sum(i)
        print(sum(i),":",free_spaces[0])
    liyonglv = all_sum / sum(free_spaces)
    # assert (all_sum/float(sum(free_spaces)))>0.5

    return num_fitted, fit_blocks,delte,liyonglv


## First-Fit implementation.
import math
def firstFit(free_spaces, append_limit,memory_requests,memory_reqquest_list_limit,all_hat_name):
    def fit_func(free_spaces, append_limit,memory_request, fit_spaces, fit_spaces_limit,fit_blocks,fit_blocks_usefull,memory_reqquest_list_limit_,all_hat_name_):
        for i in range(len(free_spaces)):
            a = fit_spaces[i] + memory_request
            b = fit_spaces_limit[i] + memory_reqquest_list_limit_
            if (fit_spaces[i] + memory_request <= free_spaces[i]) and (fit_spaces_limit[i] + memory_reqquest_list_limit_<=append_limit) :
                fit_blocks[i].append(all_hat_name_)
                fit_blocks_usefull[i].append(memory_request)
                fit_spaces[i] += memory_request

                fit_spaces_limit[i] +=memory_reqquest_list_limit_
                return 1

        return 0

    return commonFit(free_spaces, append_limit,memory_requests, fit_func,memory_reqquest_list_limit,all_hat_name)

# def bestFit(free_spaces, append_limit,memory_requests,memory_reqquest_list_limit,all_hat_name):
#     def fit_func(free_spaces, append_limit,memory_request, fit_spaces, fit_spaces_limit,fit_blocks,fit_blocks_usefull,memory_reqquest_list_limit_,all_hat_name_):
#         free_min = 1000
#         fit_id = -1
#         for i in range(len(free_spaces)):
#             if (fit_spaces[i] + memory_request <= free_spaces[i]) and (fit_spaces_limit[i] + memory_reqquest_list_limit_<=append_limit) :
#                 free_space = free_spaces[i] - (fit_spaces[i] + memory_request)
#
#                 if free_space < free_min:
#                     free_min = free_space
#                     fit_id = i
#         if fit_id > -1:
#             fit_blocks[fit_id].append(all_hat_name_)
#             fit_spaces[fit_id] += memory_request
#             fit_spaces_limit[fit_id] += memory_reqquest_list_limit_
#             fit_blocks_usefull[fit_id].append(memory_request)
#             return 1
#         return 0

    # return commonFit(free_spaces, append_limit,memory_requests, fit_func,memory_reqquest_list_limit,all_hat_name)

def firstFit_(free_spaces, append_limit, memory_requests, memory_reqquest_list_limit, all_hat_name):
    while True:
        a,b,c,d = commonFit(free_spaces, append_limit, memory_requests, fit_func, memory_reqquest_list_limit, all_hat_name)
        if a !=0:
            break
    return a,b,c,d

def fit_func(free_spaces, append_limit, memory_request, fit_spaces, fit_spaces_limit, fit_blocks,
             fit_blocks_usefull, memory_reqquest_list_limit_, all_hat_name_):

    fit_spaces_,fit_spaces_limit_,fit_blocks_,fit_blocks_usefull_= zip(*list(sorted(zip(fit_spaces,fit_spaces_limit,fit_blocks,fit_blocks_usefull))))
    fit_spaces_ = list(fit_spaces_)
    fit_spaces_limit_ = list(fit_spaces_limit_)
    fit_blocks = list(fit_blocks_)
    fit_blocks_usefull = list(fit_blocks_usefull_)
    for i in range(len(free_spaces)):


        if (fit_spaces_[i] + memory_request <= free_spaces[i]) and (
                        fit_spaces_limit_[i] + memory_reqquest_list_limit_ <= append_limit):
            fit_blocks[i].append(all_hat_name_)
            fit_blocks_usefull[i].append(memory_request)
            fit_spaces_[i] += memory_request

            fit_spaces_limit_[i] += memory_reqquest_list_limit_

            return 1,fit_spaces_,fit_spaces_limit_,fit_blocks,fit_blocks_usefull
    return 0,fit_spaces_,fit_spaces_limit_,fit_blocks,fit_blocks_usefull
def get_memory_allocation(zero_one,pre_box_memory,append_limit,memory_reqquest_list,memory_reqquest_list_limit,all_hat_name):
    start_time = time.time()
    '''
    
    :param pre_box_memory: CPU或内存容量
    :param memory_reqquest_list: 容量申请列表
    :return: 
    '''

    # ratio = list(map(lambda x:x[0]/float(x[1]), zip(memory_reqquest_list,memory_reqquest_list_limit)))
    # sort_dic ={
    # "flavor1 "
    # "flavor2 "
    # "flavor3 "
    # "flavor4 "
    # "flavor5 "
    # "flavor6 "
    # "flavor7 "
    # "flavor8 "
    # "flavor9" 
    # "flavor10 "
    # "flavor11" 
    # "flavor12" 
    # "flavor13" 
    # "flavor14"
    # "flavor15" 
    # }

    dic = list(zip(all_hat_name,memory_reqquest_list,memory_reqquest_list_limit))

    dic = sorted(dic,key= lambda x:x[-1],reverse=False)
    dic = sorted(dic,key= lambda x:x[1],reverse=True)

    memory_reqquest_list = list(i[1] for i in dic )
   

   
    all_hat_name =  list(i[0] for i in dic )
    memory_reqquest_list_limit =  list(i[2] for i in dic )
    # print(list(zip(memory_reqquest_list,memory_reqquest_list_limit)),"sssssssssssssss")
    pre_box_memory = float(pre_box_memory)
    append_limit = float(append_limit)
    need_num = math.ceil(sum(memory_reqquest_list)/pre_box_memory)
    # o = sum(memory_reqquest_list_limit)
    need_num_ =  math.ceil(sum(memory_reqquest_list_limit)/float(append_limit))
    need_num = max(need_num,need_num_)
    free_sapces = [pre_box_memory] *int(need_num )
    # free_sapces = [pre_box_memory]

    num_fitted, fit_blocks, delet,liyonglv = firstFit_(free_sapces, append_limit, memory_reqquest_list, memory_reqquest_list_limit,
                                         all_hat_name)

    for inedx in range(len(fit_blocks)):
        if fit_blocks[-1] == []:
            fit_blocks.pop(-1)
    # print(fit_blocks)
    # assert num_fitted == len(memory_reqquest_list)
    end_time = time.time() - start_time
    print("time:", end_time)
    return fit_blocks,delet,liyonglv


if __name__ == "__main__":
    start_time = time.time()
    zero_one = 1
    pre_box_memory = 56
    append_limit = 128
    '''
    1 :63
    3 :6
    5:10
    8 :90
    9 :13
    10 :5


    "flavor1":[1,1],
         "flavor2":[1,2],
        "flavor3":[1,4],
        "flavor4":[2,2],
        "flavor5":[2,4],
        "flavor6":[2,8],
        "flavor7":[4,4],
        "flavor8":[4,8],
        "flavor9":[4,16],
        "flavor10":[8,8],
        "flavor11":[8,16],
        "flavor12":[8,32],
        "flavor13":[16,16],
        "flavor14":[16,32],
        "flavor15":[16,64]

    '''
    memory_reqquest_list = [1] * 93 +[1] *50+ [1] * 6 + [2] * 10 + [4] * 103+ [4] * 53 + [8] * 25 + [16] * 5
    memory_reqquest_list_limit = [1] * 93 +[2]*50+ [4] * 6 + [4] * 10 + [8] * 103 + [16] * 53 + [8] * 25 +[64] * 5
    all_hat_name = ["flavor1"] *93 + ["flavor2"] *50+["flavor3"] * 6 + ["flavor5"] * 10 + ["flavor8"] * 103 + ["flavor9"] * 53 + ["flavor10"] * 25 +["flavor15"]*5

    s,_ = get_memory_allocation(zero_one, pre_box_memory, append_limit, memory_reqquest_list, memory_reqquest_list_limit, all_hat_name)
    end_time = time.time() - start_time
    # print("time:",end_time)
    # print(len(s))


