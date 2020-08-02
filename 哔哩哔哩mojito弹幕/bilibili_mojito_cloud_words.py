#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2020/7/8 23:28 
# @Author : 刘子豪 
# @desc : <Mojito>词云图


import jieba
import pandas as pd
from imageio import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt


import warnings
warnings.filterwarnings("ignore")


# 1.读取文件内容，并用lcut()进行分词
with open('mojito.txt', encoding='utf-8') as f:
    txt = f.read()
    f.close()
txt = txt.split()
data_cut = [jieba.lcut(x) for x in txt]  # 精确分词

# 2.读取停用词
with open(r'D:\PycharmProjects\scrapy_projects\stopwords-master\cn_stopwords.txt', encoding='utf-8') as f:
    stop = f.read()
    f.close()
stop = stop.split()
stop = [" ", "道", "说道", "说"] + stop
# 3.去掉停用词之后的最终词
s_data_cut = pd.Series(data_cut)  # 创建一个有序序列
all_word_after = s_data_cut.apply(lambda x: [i for i in x if i not in stop])  # 批量处理
# 4.词频统计
all_words = []
for i in all_word_after:
    all_words.extend(i)
word_count = pd.Series(all_words).value_counts()  # 统计数据出现的次数
# 5.词云图的制作
# 5.1读取背景图片
back_picture = imread(r'D:\PycharmProjects\scrapy_projects\cat.jpg')

# 5.2设置词云参数
wc = WordCloud(font_path="simheittf\\simhei.ttf",
               background_color="white",
               max_words=2000,
               mask=back_picture,
               max_font_size=200,
               random_state=42
              )

wc2 = wc.fit_words(word_count)

# 3）绘制词云图
plt.figure(figsize=(16,8))
plt.imshow(wc2)
plt.axis("off")
plt.show()
wc.to_file("ciyun.png")