# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:09:33 2018

@author: INSIS-rongbin
"""

import itchat
import os
import codecs
import json

sex_dict = {'0':'其他','1':'男','2':'女'}


def download_images(friend_list):
    image_dir = './images/'
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    num = 1
    print('begin to download friend\'s avatar')
    num = 1
    for friend in friend_list:
        image_name = str(num) + '.jpg'
        num += 1
        img = itchat.get_head_img(userName=friend['UserName'])
        with open(image_dir + image_name,'wb') as file:
            file.write(img)
    print('download friend\'s avatar complete!')
    
def download_data(friend_list):
    data_dir = './data/'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    out_file_name = './data/friends.json'
    print('begin to download friend\'s data ')
    with codecs.open(out_file_name,'w',encoding='utf-8') as json_file:
        json_file.write(json.dumps(friend_list,ensure_ascii=False))
        
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    
    friends = itchat.get_friends(update=True)[1:]
    friend_list = []
    for friend in friends:
        item = {'NickName':friend['NickName'],'HeadImgUrl':friend['HeadImgUrl'],'Sex':sex_dict[str(friend['Sex'])],
                'Province':friend['Province'],'Signature':friend['Signature'],'UserName':friend['UserName']}
        friend_list.append(item)
    
    download_images(friend_list) 
    download_data(friend_list)
