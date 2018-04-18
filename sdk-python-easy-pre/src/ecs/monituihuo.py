#coding=utf-8
from memory_alloction_ import get_memory_allocation
import random
import math
def add_noise(change_list,orig_list,index1,index2):
    (change_list[index1], change_list[index2]) = (orig_list[index2], orig_list[index1])

def tuihuo(zero_one,pre_box_memory,append_limit,memory_reqquest_list,memory_reqquest_list_limit,all_hat_name):

    '''
    :param cpu_mem: 0 or 1
    :param flavor_list: [flavor_name,
                        cpu,
                        mem,...]
    :return:
    '''
    T0 = 100
    T_end = 0.5
    alpha = 0.99

    best_severe_num = len(memory_reqquest_list)#最优箱子数
    markov = 10
    new_severe_num = best_severe_num
    T = T0
    floavor_dict = {
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

    }
    predict_flavor_num_list= range(len(memory_reqquest_list))#预测虚拟机总数

    best_memory_reqquest_list = memory_reqquest_list[:]
    best_memory_reqquest_list_limit = memory_reqquest_list_limit[:]
    best_all_hat_name = all_hat_name[:]


    while T>T_end:
        for i in range(markov):
            random.shuffle(predict_flavor_num_list)
            change_index1,change_index2,change_index3,change_index4 = predict_flavor_num_list[:4]
            while memory_reqquest_list[change_index2]==memory_reqquest_list[change_index1] or \
                            memory_reqquest_list[change_index2]==memory_reqquest_list[change_index3] or\
                memory_reqquest_list[change_index3] == memory_reqquest_list[change_index1]:

                random.shuffle(predict_flavor_num_list)
                change_index1, change_index2, change_index3, change_index4 = predict_flavor_num_list[:4]
            # if memory_reqquest_list[change_index3] == memory_reqquest_list[change_index4]:
            #     continue
            change_memory_reqquest_list = memory_reqquest_list[:]
            change_memory_reqquest_list_limit = memory_reqquest_list_limit[:]
            change_all_hat_name = all_hat_name[:]
            # (change_memory_reqquest_list[change_index1],change_memory_reqquest_list[change_index2],change_memory_reqquest_list[change_index3],change_memory_reqquest_list[change_index4]) = \
            #     (memory_reqquest_list[change_index2],memory_reqquest_list[change_index1],memory_reqquest_list[change_index4],memory_reqquest_list[change_index3])
            # (change_memory_reqquest_list_limit[change_index1], change_memory_reqquest_list_limit[change_index2],change_memory_reqquest_list_limit[change_index3], change_memory_reqquest_list_limit[change_index4]) =\
            #     (memory_reqquest_list_limit[change_index2], memory_reqquest_list_limit[change_index1],memory_reqquest_list_limit[change_index4], memory_reqquest_list_limit[change_index3])
            # (change_all_hat_name[change_index1], change_all_hat_name[change_index2],change_all_hat_name[change_index3], change_all_hat_name[change_index4]) = \
            #     (all_hat_name[change_index2], all_hat_name[change_index1],all_hat_name[change_index4], all_hat_name[change_index3])
            o_1 = [0,1]
            random.shuffle(o_1)
            if o_1[0]:

                add_noise(change_memory_reqquest_list, memory_reqquest_list, change_index1, change_index2)
                add_noise(change_memory_reqquest_list_limit, memory_reqquest_list_limit, change_index1, change_index2)
                add_noise(change_all_hat_name, all_hat_name, change_index1, change_index2)
            else:
                o_1_2 = [0,1,2]
                random.shuffle(o_1_2)
                for i,o_ in enumerate(o_1_2):
                    change_memory_reqquest_list[predict_flavor_num_list[i]]  = memory_reqquest_list[predict_flavor_num_list[o_]]
                    change_memory_reqquest_list_limit[predict_flavor_num_list[i]]= memory_reqquest_list_limit[predict_flavor_num_list[o_]]
                    change_all_hat_name[predict_flavor_num_list[i]]= all_hat_name[predict_flavor_num_list[o_]]


            accury0 =0
            accury1 =0
            result,delet  = get_memory_allocation(zero_one,pre_box_memory,append_limit,memory_reqquest_list,memory_reqquest_list_limit,all_hat_name)
            wuliji_num = len(result)#箱子数
            # print("箱子数",wuliji_num)
            for i in result[-1]:
                accury0 += (floavor_dict[i][0])
                accury1 +=(floavor_dict[i][1])
            accury0 = accury0/float(pre_box_memory)#最后一个箱子所要优化的维度利用率
            accury1 = accury1/float(append_limit)#最后一个箱子另一个维度的利用率
            # cpu :new_severe_num = wuliji_num -1 + 最后一个箱子cpu资源利用率
            # mem:

            new_severe_num =  wuliji_num -1 + accury0
            # print(new_severe_num)
            print("best_severe_num:",best_severe_num)
            if new_severe_num < best_severe_num:#更新
                # print("更新1")
                best_severe_num = new_severe_num
                best_result = result[:]

                best_memory_reqquest_list = change_memory_reqquest_list[:]
                best_memory_reqquest_list_limit = change_memory_reqquest_list_limit[:]
                best_all_hat_name = change_all_hat_name[:]

                memory_reqquest_list = change_memory_reqquest_list[:]
                memory_reqquest_list_limit = change_memory_reqquest_list_limit[:]
                all_hat_name = change_all_hat_name[:]
            else:
                if random.random() < math.exp((best_severe_num - new_severe_num)/T ):
                    # print("更新2")
                    memory_reqquest_list = change_memory_reqquest_list[:]
                    memory_reqquest_list_limit = change_memory_reqquest_list_limit[:]
                    # all_hat_name = change_all_hat_name[:]
        T = T *alpha
    print (best_result)
    return best_result


if __name__ == "__main__":
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

    _ = tuihuo(zero_one, pre_box_memory, append_limit, memory_reqquest_list, memory_reqquest_list_limit, all_hat_name)







