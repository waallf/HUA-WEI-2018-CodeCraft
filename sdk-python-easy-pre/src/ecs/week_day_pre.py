#coding=utf-8
'''
按星期建立字典
'''
import math
def week_day_pre(start_weekday,labelMat,start_test_weekday,test_time):
    week_dict = {}
    pre= 0
    for j in range(7):

        weekday = (start_weekday + j) % 7
        weekday = str(weekday)
        week_dict[weekday] = list(labelMat[i] for i in range(j, len(labelMat),7))
    '''
    需要预测的星期
    '''
    for i in range(test_time):
        need_pre_week = (start_test_weekday + i) %7
        start_weeneed_pre_weekkday = str(need_pre_week)
        s = week_dict[start_weeneed_pre_weekkday]
        # pre += math.ceil((sum(week_dict[start_weeneed_pre_weekkday])/float(len(week_dict[start_weeneed_pre_weekkday]))))
        pre += 1.5 *(week_dict[start_weeneed_pre_weekkday][-1] *1+week_dict[start_weeneed_pre_weekkday][-2] *0+week_dict[start_weeneed_pre_weekkday][-3] *0)+1
    return int(pre)
