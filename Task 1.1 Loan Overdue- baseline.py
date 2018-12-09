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

# In[2] 读取并分割数据
data_all = pd.read_csv('./data_all.csv')
Y = data_all['status']
X = data_all.drop('status', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=2018)

# In[3] 数据初探
X_train.info()
plt.hist(Y_train, bins=3)
plt.show()
plt.hist(Y_test, bins=3)
plt.show()
# 存在数据不平衡问题的
# In[4] 建模: Logistic回归
lr = LogisticRegression(random_state =2018)
lr.fit(X_train, Y_train)
predict_Y = lr.predict(X_test)
acc = lr.score(X_test,Y_test)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
# 0.748423265592 0.5

# In[5] 建模: Decision Tree
dt = tree.DecisionTreeClassifier(random_state =2018)
dt.fit(X_train, Y_train)
predict_Y = lr.predict(X_test)
acc = dt.score(X_test,Y_test)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
# 0.68465311843 0.5

# In[6] 建模：SVM支持向量机
clf = svm.SVC(random_state =2018)
clf.fit(X_train, Y_train)
predict_Y = clf.predict(X_test)
acc = clf.score(X_test,Y_test)
auc = metrics.roc_auc_score(Y_test,predict_Y)
print(acc,auc)
# 0.748423265592 0.5
# In[] Summary
'''
 对拆分后的数据查看分布，还是拆分之前的总数据，并且要使得train和test的分布保持一致？
'''