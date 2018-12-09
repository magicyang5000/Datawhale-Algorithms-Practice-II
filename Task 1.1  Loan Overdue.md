# 1.业务理解（Business Understanding）

本次任务目标是根据用户情况(历史记录、消费情况等)预测是否会贷款逾期。  
贷款逾期只判断是或否。所以属于二分类问题。

# 2.数据理解（Data Understanding）
该数据集包含85个属性，4754条数据。  
除了目标属性status(值为0 or 1)外，其他84个属性大致可分为以下几类：  
* 历史及近期交易状况
* 历史及近期消费状况
* 历史及近期贷款的申请和审核状况
* 历史及近期查询状况
* 历史及近期信用记录
* 其他

# 3.数据准备（Data Preparation）
由于本次数据是基本处理好的，所以只是简单查看下数据情况和类别是否平衡问题。  
通过代码结果，可见数据无缺失值；  
status的两个类别间严重不平衡，逾期:不逾期 ≈ 1:3  
该问题通过直接建模的结果也可以看出来。
  
这里通过imblearn包中的SMOTE功能，将逾期的数据量扩大。详见代码。  

# 4.建模（Modeling）
本次采用Logistic回归、SVM和决策树3个模型，评分方式采用准确度和AUC结合的方式，并且查看评分报告。  
直接建模，未调整参数。各模型对应代码为：
  
* Logistic回归  
  
```Python
  lr = LogisticRegression(random_state =2018)  
  lr.fit(over_samples_X, over_samples_y)  
  predict_Y = lr.predict(X_test) 
```
* 决策树  
  
```Python
  dt = tree.DecisionTreeClassifier(random_state =2018)  
  dt.fit(over_samples_X, over_samples_y)  
  predict_Y = dt.predict(X_test)  
```
* SVM  
  
```Python
  clf = svm.SVC(random_state =2018)  
  clf.fit(over_samples_X, over_samples_y)  
  predict_Y = clf.predict(X_test)  
```
  
# 5.评估（Evaluation）
* 第一次：  
未处理数据不平衡问题，三个模型结果如下  
  
|               | ACC           |AUC     |  
| ------------- | ------------- | ------------- |
|Logistic回归  |   0.748423265592     |  0.5 | 
|决策树  |       0.68465311843      |  0.5  |
|SVM  |         0.748423265592     |   0.5  |
  
仅看ACC的话，三个模型还行，其中Logistic和SVM较高。 但是三者的AUC都一样，且很低。  
查看下三者的评分report： 
  
```Python
  print(metrics.classification_report(Y_test, predict_Y))  
```
**Logistic的：**  
  
|            |precision   | recall  |f1-score | support  |
| -----------| -----------| -----------|-----------| -----------|
|        0   | 0.75       |1.00     |0.86     | 1068     |
|        1   | 0.00       |0.00     |0.00     | 359      |
|avg / total | 0.56       |0.75    | 0.64    | 1427     |
  
**决策树：**  
  
|          |precision    |recall  |f1-score   |support |   
| ------------- | ------------- | ------------- | ------------- |------------- |
|        0       |0.75      |1.00      |0.86      |1068  |  
|          1       |0.00      |0.00      |0.00       |359  |  
|avg / total       |0.56      |0.75      |0.64      |1427  |  
  
 **SVM：**
   
|           |precision    |recall  |f1-score   |support | 
| ------------- | ------------- | ------------- | ------------- |------------- |
|       0       |0.75      |1.00     | 0.86      |1068  |  
|     1       |0.00     | 0.00     | 0.00      | 359  |  
|avg / total       |0.56     | 0.75     | 0.64      |1427  |  
   
可以看到所有结果都是预测为不逾期，逾期的预测准确度为0。  
  
* 第二次：  
处理数据不平衡之后。  
  
|               | ACC           |AUC     |  
| ------------- | ------------- | ------------- |
|Logistic回归  |   0.679046951647     |  0.657986708815 | 
|决策树  |       0.687456201822      |  0.609978300105 |
|SVM  |         0.748423265592     |   0.5  |
  
Logistic回归和决策树，在数据平衡后效果较大的提升，AUC达到了0.6，但是这个准确度依然不够。常规意义上，一般认为AUC>0.8模型效果较好。  

# 6.总结（Summary）
* ① 初步来看，该项目数据不平衡问题较为严重。但是不知道为什么SVM不受影响？
* ② 看数据的分布，是看原始全部数据？  
    还是看拆分后的数据？（或者说拆分后的training和testing的分布也要保持一致？）  
* ③ 该项目属性较多，之后可以尝试先做一遍属性筛选。
  
  
  
  
baseline代码链接：https://github.com/magicyang5000/Datawhale-Algorithms-Practice-II/blob/master/Task%201.1%20Loan%20Overdue%20-%20oversample.py  
  
处理数据不平衡后代码链接：https://github.com/magicyang5000/Datawhale-Algorithms-Practice-II/blob/master/Task%201.1%20Loan%20Overdue%20-%20oversample.py
