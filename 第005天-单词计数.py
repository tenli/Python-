"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re
from collections import Counter
with open('G:\\Python\\PythonWorkSpace\\Python练习册\\Python_Day_After_Day\\第005天-english_text.txt',encoding='utf-8') as f:
    content=f.read()
    words=re.findall(r'[a-zA-Z]+',content)
summary_list = Counter(words)
sort_list = sorted(summary_list.items(), key=lambda x: x[1], reverse=True)

for key, value in dict(sort_list).items():
    print('单词：{0} 出现次数：{1}'.format(key,value))