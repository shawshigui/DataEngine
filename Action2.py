# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:22:49 2020

@author: xiaoshigui
"""

import pandas as pd


data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=pd.DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'])
print(df)

print(df.describe())

print('\n语文平均成绩是:%.2f,最小成绩是：%.2f,最大成绩是：%.2f,方差是：%.2f,标准差是：%.2f'  %( df['语文'].mean() , df['语文'].min(), df['语文'].max(), df['语文'].var(), df['语文'].std()))
print('\n英语平均成绩是:%.2f,最小成绩是：%.2f,最大成绩是：%.2f,方差是：%.2f,标准差是：%.2f'  %( df['英语'].mean() , df['英语'].min(), df['英语'].max(), df['英语'].var(), df['英语'].std()))
print('\n数学平均成绩是:%.2f,最小成绩是：%.2f,最大成绩是：%.2f,方差是：%.2f,标准差是：%.2f\n'  %( df['数学'].mean() , df['数学'].min(), df['数学'].max(), df['数学'].var(), df['数学'].std()))


df['总成绩']=df['语文']+df['数学']+df['英语']
print('unsorted df:')
print(df)
print('\n')
#goupby方法，如何生成的新的groupby的列名称
#result=df.groupby(['语文','数学','英语']).agg(np.sum)
#print('\n')
#df.rename('','总成绩1')
#print(df)
sorted_df=df.sort_values(by='总成绩',ascending=False)
print('sorted df:')
print(sorted_df)

#输出排名
print('\n按成绩高低排名为：%s'% sorted_df['总成绩'].index.tolist())