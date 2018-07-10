# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:14:55 2018

@author: INSIS-rongbin
"""

import codecs
import json
from matplotlib import pyplot
import matplotlib
#import numpy
from collections import Counter


def counter2list(_counter):   #将字典转换为list，key与value分别对应两个list
    item_name_list = []
    item_num_list = []
    
    for item in _counter:
        item_name_list.append(item[0])
        item_num_list.append(item[1])
        
        
    return item_name_list,item_num_list

if __name__ == '__main__':
    matplotlib.rcParams["font.family"]="sans-serif"
    matplotlib.rcParams["font.sans-serif"]=u'SimHei'
    
    in_file_name = './data/friends.json'
    with codecs.open(in_file_name,encoding='utf-8') as f:
        friends = json.load(f)
    
    item_name_list = []
    item_num_list = []
    
    province_counter = Counter()
    for friend in friends:
        if friend['Province'] == '':
            friend['Province'] = '其他'
        province_counter[friend['Province']] += 1
    
    item_name_list,item_num_list = counter2list(province_counter.most_common(10))
    #index = numpy.arange(6)
    
    print(item_name_list)
    print(item_num_list)
    #index = ['按你',2,3,4,5,6]
    #y = [4,78,5,9,23,20]
    pyplot.bar(left=item_name_list,height = item_num_list,color = 'pink',width = 0.5)
    pyplot.show()
    