
#使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
#data = pd.read_csv('Mall_Customers.csv', encoding='gbk')
data = pd.read_csv('car_data.csv',encoding='gbk')
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数", "百户拥有汽车量"]]
train_x=train_x.copy()
print(train_x)


# LabelEncoder 将性别字段转化为数值 
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# train_x['Gender'] = le.fit_transform(train_x['Gender'])
# print(train_x['Gender'])


#规范化到 [0,1] 空间，相当于转化成了一个无量纲数，归一化处理
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
#对所有数据做规范化，相当于把每一列都转化成同一个min-max
#如（0，1）之间的数值，方便比较
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x) 


# # ### 使用KMeans聚类，没有可视化方式
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(train_x) #训练数据
# predict_y = kmeans.predict(train_x)

# # 合并聚类结果，插入到原数据中
# result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
# result.rename({0:u'聚类结果'},axis=1,inplace=True)
# print(result)
# # 将结果导出到CSV文件中
# result.to_csv("car_cluster_result.csv",index=False,encoding='gbk')



# # K-Means 手肘法：统计不同K取值的误差平方和
#类别中心点成为质点，计算所有类别内的点与质点的误差大小

# import matplotlib.pyplot as plt
# sse = []
# for k in range(1, 11):
#  	# kmeans算法
#  	kmeans = KMeans(n_clusters=k)
#  	kmeans.fit(train_x)
#  	# 计算inertia簇内误差平方和
#  	sse.append(kmeans.inertia_)
# x = range(1, 11)
# plt.xlabel('K')
# plt.ylabel('SSE')
# plt.plot(x, sse, 'o-')
# plt.show()




### 使用层次聚类
##经过K-Means手肘法得出较好的分类数为5
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=5)
y = model.fit_predict(train_x)
print(y)


# #层次聚类画图，可视化
linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()
