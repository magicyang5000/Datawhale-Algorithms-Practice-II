# 1.混淆矩阵
在介绍各项指标含义之前，先介绍混淆矩阵。因为指标都是从婚讯矩阵引申出来的。  
**混淆矩阵**是用来总结一个分类器结果的矩阵。对于k元分类，其实它就是一个k x k的表格，用来记录分类器的预测结果。  
对于最常见的二元分类来说，它的混淆矩阵是2乘2的，如下  
 |        |     预测值=1      |    预测值=0    |
 ------- | ----------------- |--------------
真实值=1  |  True Positive   |  False Negative
真实值=0 |   False Positive  |  True Negative

* 真阳性（True Positive，TP）：样本的真实类别是正例，并且模型预测的结果也是正例
* 真阴性（True Negative，TN）：样本的真实类别是负例，并且模型将其预测成为负例
* 假阳性（False Positive，FP）：样本的真实类别是负例，但是模型将其预测成为正例
* 假阴性（False Negative，FN）：样本的真实类别是正例，但是模型将其预测成为负例


# 2.指标

  
# 参考资料：  
https://en.wikipedia.org/wiki/Confusion_matrix 
https://zhuanlan.zhihu.com/p/42475636  
http://sofasofa.io/forum_main_post.php?postid=1000597
