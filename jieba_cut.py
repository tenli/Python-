# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:21:00 2017

@author: XingZhe
"""

import pandas as pd
import numpy as np
import jieba

jieba.load_userdict('goods_cutword.txt')
stopword = pd.read_csv('goods_stopword.txt', encoding='utf8', index_col=False)

data = pd.read_csv('C:\\Users\\fangs\\Desktop\\buy1.csv', encoding='GBK').astype(str)

# data = pd.read_csv('D:\\uu_input_spyder_data\\result.txt')
# ==============================================================================
# data.isnull().sum()
# data.shape           
# data.columns
# data.dtypes
# ==============================================================================

# data = data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5'], axis=1)  # 删除列

# data['time_day'] = pd.to_datetime(data['取消']).dt.day
# data['time_hour'] = pd.to_datetime(data['取消']).dt.hour

time_hours = []
segments = []

for index, row in data.iterrows():
    # time_hour = row['time_hour']
    content = row['note']
    segs = jieba.cut(content)
    for seg in segs:
        if seg not in stopword.values and len(seg.strip()) > 0:
            segments.append(seg)

note = pd.DataFrame(
    {
        #'time_hour': time_hours,
        'seg': segments,
    }
)

note_agg = pd.pivot_table(
    note, index=['seg'], aggfunc=np.size,
)

column = ['pinci']
note_agg = pd.DataFrame(note_agg)
note_agg.columns = column
note.agg = note_agg.sort_values(by='pinci', ascending=False)  # 根据列的值进行排序，倒叙

# note_agg = note_agg.sort_values(by = 'time_hour',ascending=False)
