# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:59:46 2018

@author: INSIS-rongbin
"""

from collections import Counter
from pyecharts import WordCloud
import codecs
import json
import os
import jieba.analyse

def word_cloud(item_name,item_name_list,item_num_list,word_size_range):
    wordcloud = WordCloud(width = 1400,height=900)
    
    wordcloud.add('',item_name_list,item_num_list,word_size_range = word_size_range,shape='pentagon')
    
    analyse_path = './analyse/'
    if not os.path.exists(analyse_path):
        os.mkdir(analyse_path)
    out_file_name = analyse_path + item_name + '.html'
    wordcloud.render(out_file_name)
    
    
def get_tag(text,cnt):
    #print('正在分析句子')
    tag_list = jieba.analyse.extract_tags(text) #jieba分词
    for tag in tag_list:
        cnt[tag] += 1
        

def counter2list(_counter):
    name_list = []
    num_list = []
    
    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1])
    
    return name_list,num_list    

if __name__ == '__main__':
    in_file_name = './data/friends.json'
    with codecs.open(in_file_name,encoding='utf-8') as f:
        friends = json.load(f)   #fiends是一个字典
        print('friends 的类型是' +str(type(friends)))    
        
    Signature_couter = Counter() #字典,待统计参数
    print('Signature_couter 的类型是 '+str(type(Signature_couter)))
    
    for friend in friends:
        signature = friend['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
        #signature = friend['Signature'] 
        get_tag(signature,Signature_couter)
        
    name_list,num_list = counter2list(Signature_couter.most_common(200))
    word_cloud('微信好友签名关键词',name_list,num_list,[20,100])
        
    
    