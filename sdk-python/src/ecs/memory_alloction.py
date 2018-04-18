# coding=utf-8
def commonFit(free_spaces, memory_requests, fit_func,all_hat_name):
    fit_spaces = [0]*(len(free_spaces))
    fit_blocks = [[] for i in range(len(free_spaces))]
    num_fitted = 0

    for index,memory_request in enumerate(memory_requests):
        all_hat_name_ = all_hat_name[index]
        fitted = fit_func(free_spaces, memory_request, fit_spaces, fit_blocks,all_hat_name_)
        num_fitted += fitted

    success = num_fitted / float(len(memory_requests))
    # use_accury = [sum(fit_block) for fit_block in fit_blocks]
    return success, fit_blocks


## First-Fit implementation.
import math
def firstFit(free_spaces, memory_requests,all_hat_name):
    def fit_func(free_spaces, memory_request, fit_spaces, fit_blocks,all_hat_name_):
        for i in range(len(free_spaces)):
            if fit_spaces[i] + memory_request <= free_spaces[i]:
                fit_blocks[i].append(all_hat_name_)
                fit_spaces[i] += memory_request
                return 1
        return 0

    return commonFit(free_spaces, memory_requests, fit_func,all_hat_name)

def get_memory_allocation(pre_box_memory,memory_reqquest_list,all_hat_name):
    '''
    
    :param pre_box_memory: CPU或内存容量
    :param memory_reqquest_list: 容量申请列表
    :return: 
    '''
    dic = list(zip(all_hat_name,memory_reqquest_list))
    dic = sorted(dic,key= lambda x:x[1],reverse=True)

    memory_reqquest_list = list(i[1] for i in dic )
    all_hat_name =  list(i[0] for i in dic )

    pre_box_memory = float(pre_box_memory)
    need_num = math.ceil(sum(memory_reqquest_list)/pre_box_memory)
    free_sapces = [pre_box_memory] * int(need_num)
    succes, fit_blocks = firstFit(free_sapces, memory_reqquest_list,all_hat_name)

    return fit_blocks



if __name__ =="__main__":
    fit_blocks = get_memory_allocation(56,[16,16,16,16,16,16,16,8,8,8,8,4,4,4,4,2,2,2,1,1,1],["5","5","5","5","5","5","5","4","4","4","4","3","3","3","3","2","2","2","1","1","1"])
    print( fit_blocks)


