# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:45:45 2018

@author: CodingAllTheWay
"""

from collections import Counter
from pyecharts import Pie
import codecs
import json
import os

def get_pie(item_name,item_name_list,item_num_list):
    totle = item_num_list[0] + item_num_list[1] + item_num_list[2]
    subtitle = '共有：%d个好友' % totle
    
    pie = Pie(item_name,page_title = item_name,title_text_size=30,title_pos='center',
              subtitle=subtitle,subtitle_text_size = 25,width=800,height=800)
    
    pie.add('',item_name_list,item_num_list,is_lable_show=True,center=[50,45],radius=[0,50],
            legend_pos='left',legend_orient='vertical',lable_text_size=20)
    analyse_path = './analyse/'
    if not os.path.exists(analyse_path):
        os.mkdir(analyse_path)
        
    out_file_name = analyse_path + item_name + '.html'
    pie.render(out_file_name)

def dict2list(_dict):
    name_list = []
    num_list = []
    
    for key,value in _dict.items():
        name_list.append(key)
        num_list.append(value)
    
    return name_list,num_list
    
if __name__ == '__main__':
    
    in_file_name = './data/friends.json';
    with codecs.open(in_file_name,encoding='utf-8') as f:
        friends = json.load(f)
    sex_counter = Counter()
    
    for friend in friends:
        sex_counter[friend['Sex']] += 1
    
    name_list, num_list = dict2list(sex_counter)
    get_pie('性别统计',name_list,num_list)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
