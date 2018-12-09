# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:43:00 2018

@author: magic
"""
# In[1] 载入包
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn import svm
from sklearn import metrics
from imblearn.over_sampling import SMOTE

# In[2] 读取并分割数据
data_all = pd.read_csv('./data_all.csv')
Y = data_all['status']
X = data_all.drop('status', axis=1)

# 按7:3拆分成training和testing集，随机种子为2018。随机种子的目的是使每次拆分的结果一致
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=2018)

# In[3] 数据初探
X_train.info() # 查看数据信息以及是否有缺失值

# 查看label的分布，存在数据不平衡问题的。直接初步建模也验证了这一现象。
plt.hist(Y_train, bins=3)
plt.show()
plt.hist(Y_test, bins=3)
plt.show()


# In[4] 数据平衡处理
over_samples = SMOTE(random_state=2018) 
over_samples_X,over_samples_y = over_samples.fit_sample(X_train, Y_train)

# 重抽样前的类别比例
print(Y_train.value_counts()/len(Y_train))
# 重抽样后的类别比例
print(pd.Series(over_samples_y).value_counts()/len(over_samples_y))

# In[5] 建模: Logistic回归
lr = LogisticRegression(random_state =2018)
lr.fit(over_samples_X, over_samples_y)
predict_Y = lr.predict(X_test)
acc = metrics.accuracy_score(Y_test,predict_Y)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
print(metrics.classification_report(Y_test, predict_Y))
# 0.679046951647 0.657986708815
# 准确度下降了，AUC提升，但是依然不够，最佳的是要有AUC>0.8

# In[6] 建模: Decision Tree
dt = tree.DecisionTreeClassifier(random_state =2018)
dt.fit(over_samples_X, over_samples_y)
predict_Y = dt.predict(X_test)
acc = metrics.accuracy_score(Y_test,predict_Y)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
print(metrics.classification_report(Y_test, predict_Y))
# 0.679046951647 0.657986708815
# 准确度下降了，AUC提升，但是依然不够，最佳的是要有AUC>0.8

# In[7] 建模：SVM支持向量机
clf = svm.SVC(random_state =2018)
clf.fit(over_samples_X, over_samples_y)
predict_Y = clf.predict(X_test)
acc = metrics.accuracy_score(Y_test,predict_Y)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
print(metrics.classification_report(Y_test, predict_Y))
# 0.748423265592 0.5
# 数据平衡前后对SVM无影响。

# In[8] Summary
'''
1.对拆分后的数据查看分布，还是拆分之前的总数据，并且要使得train和test的分布保持一致？
2.全都预测为不逾期，模型无意义。存在数据不平衡问题
'''
