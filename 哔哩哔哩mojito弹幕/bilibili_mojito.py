#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2020/7/8 18:03 
# @Author : 刘子豪 
# @desc : 爬取bilibili<Mojito>弹幕


import requests
import json
import chardet
import re


# 1.根据vid请求得到cid
def get_cid():
    url = "https://api.bilibili.com/x/player/pagelist?bvid=BV1PK4y1b7dt&jsonp=jsonp"
    res = requests.get(url).text
    json_dict = json.loads(res)  # 将json格式数据转换为dict
    # print(json_dict)
    return json_dict['data'][0]['cid']


# 2.根据cid请求弹幕，解析弹幕得到最终的数据
def get_data(cid):
    final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    final_res = requests.get(final_url)
    final_res.encoding = chardet.detect(final_res.content)['encoding']  # 检测文本编码
    final_res = final_res.text
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    return data


# 3.保存数据
def save_to_file(data):
    with open('mojito.txt', mode='w', encoding='utf-8') as f:
        for i in data:
            f.write(i)
            f.write('\n')
        f.close()


cid = get_cid()
data = get_data(cid)
save_to_file(data)
