# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:06:43 2020

@author: x_shi
"""

import pandas as pd


cp0=pd.read_csv('car_complain.csv')
# print(cp0)

cp=cp0.drop(['id','type','desc','datetime','status'],axis=1)
print(cp)
data=cp['problem'].str.split(',',expand=True)
# print(data)


df=pd.merge(cp,data,left_index=True, right_index=True)
print(df)
df.to_excel('new.xls')
df['count']=data.shape[1]-(df.isnull().sum(axis=1)+1)
print(df)

df0=df.groupby(['brand','car_model'])['count'].sum()

print('品牌和车型故障统计：')

print(df0)
df0.to_excel('品牌和车型故障统计.xls')


#品牌投诉最多
brand=df.groupby(['brand'])['count'].sum()
a=pd.DataFrame(brand)
print('品牌投诉数')
sorted_brand=a.sort_values(by='count',ascending=False)
print(sorted_brand)
sorted_brand.to_excel('品牌投诉数.xls')


#车型投诉最多
model=df.groupby(['car_model'])['count'].sum()
b=pd.DataFrame(model)
sorted_model=b.sort_values(by='count',ascending=False)
print('车型投诉数')
print(sorted_model)
sorted_model.to_excel('车型投诉数.xls')


#平均车型投诉最多的品牌
#各品牌车型数量
car_type=df.groupby(['brand'])['car_model'].nunique()
c=pd.DataFrame(car_type)
print(c)

ave=pd.merge(sorted_brand,c,on='brand')
print(ave)
ave['ave']=ave['count']/ave['car_model']
print('平均每个车型投诉数：')
print(ave)
ave.to_excel('平均每个车型投诉数.xls')
