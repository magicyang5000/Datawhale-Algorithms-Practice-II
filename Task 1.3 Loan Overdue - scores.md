# 1.混淆矩阵
在介绍各项指标含义之前，先介绍混淆矩阵。因为指标都是从婚讯矩阵引申出来的。  
**混淆矩阵**是用来总结一个分类器结果的矩阵。对于k元分类，其实它就是一个k x k的表格，用来记录分类器的预测结果。  
对于最常见的二元分类来说，它的混淆矩阵是2乘2的，如下 

 |        |     预测值=1      |    预测值=0    |
 | ----------------- | ----------------- | ----------------- |
|真实值=1  |  True Positive   |  False Negative|
|真实值=0 |   False Positive  |  True Negative|

取一个真实数字，方便计算：

|        |     预测值=1      |    预测值=0    |
 | ----------------- | ----------------- | ----------------- |
|真实值=1  |  5   |  2|
|真实值=0 |   4  |  4|

* 真阳性（True Positive，TP）：样本的真实类别是正例，并且模型预测的结果也是正例
* 真阴性（True Negative，TN）：样本的真实类别是负例，并且模型将其预测成为负例
* 假阳性（False Positive，FP）：样本的真实类别是负例，但是模型将其预测成为正例
* 假阴性（False Negative，FN）：样本的真实类别是正例，但是模型将其预测成为负例

# 2.指标
混淆矩阵延伸出的各个评价指标： 
  
**准确度(Accuracy)** = (TP+TN) / (TP+TN+FN+TN)  
在上面的例子中，准确度 = (5+4) / 15 = 0.6  
  
**正确率(Precision)** = TP / (TP + FP)  
在上面的例子中，精度 = 5 / (5+4) = 0.556  
  
**真阳性率(True Positive Rate，TPR)，灵敏度(Sensitivity)，召回率(Recall)** = TP / (TP + FN)  
在上面的例子中，召回 = 5 / (5+2) = 0.714  
  
**真阴性率(True Negative Rate，TNR)，特异度(Specificity)** = TN / (TN + FP)  
在上面的例子中，特异度 = 4 / (4+2) = 0.667  
  
**假阴性率(False Negatice Rate，FNR)，漏诊率( = 1 - 灵敏度)** = FN / (TP + FN) = 1 - TPR  
在上面的例子中，特异度 = 2 / (5+2) = 0.286 
  
**假阳性率(False Positice Rate，FPR)，误诊率( = 1 - 特异度)** = FP / (FP + TN) = 1 - TNR
在上面的例子中，特异度 = 2 / (4+2) = 0.333
  
**F1-值(F1-score)** = 2 * TP / (2 * TP+FP+FN)   
在上面的例子中，F1-值 = 2 * 5 / (2 * 5+4+2) = 0.625  

**AUC，Area under curve**  
ROC曲线下面积。取值范围[0.5,1]，越大表示越好。  
AUC比以上指标能更为平衡的描述模型的好坏。  
  
# 参考资料：  
[混淆矩阵]https://en.wikipedia.org/wiki/Confusion_matrix   
[混淆矩阵]https://zhuanlan.zhihu.com/p/42475636   
[混淆矩阵]http://sofasofa.io/forum_main_post.php?postid=1000597  
[AUC]https://www.zhihu.com/question/39840928
