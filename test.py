#!/usr/bin/env python
#coding:utf-8

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split


# 随机森林
class RandomForest(RandomForestClassifier):
    """
    inputTableName:必选，输入表
    labelColName:必选，输入的标签列列名
    weightColName:可选，权重列，默认为空
    featureColName:可选，特征列，默认为除标签列的所有列
    excludedColNames:可选，排除列，即不参与特征训练的列，与特征列不共存，默认为空
    forceCategorical:可选，强制转换列，即把连续特征转换为离散特征，默认为空
    treeNum:可选，森林中树的个数，正整数，默认为100
    algorithmTypes:可选，单棵树算法在森林中的位置，默认为None，则算法在森林中均分；若有则格式为a,b。即假设有n棵树，[0,a)算法为id3；[a,b)为cart；[b,n)是c4.5
    randomColNum:可选，单棵树随机特征数，范围为[1,N]，默认为log2N
    minNumObj:可选，叶节点数据的最小个数，正整数，默认为2
    minNumPer:可选，叶节点数据个数占父节点的最小比例，[0,1]，默认为0
    maxTreeDeep:可选，单棵树的最大深度，默认为None, 为无穷
    maxRecorSize:可选，单棵树输入的随机数据个数，(1000,1000000]，默认为100000
    """
    class AttributeException(Exception):
        def __init__(self):
            super(RandomForest.AttributeException, self).__init__("both featureColName and excludedColNames are None")


    def __init__(self, inputTableName,labelColName,weightColName=None,featureColName=None,
                 excludedColNames=None,forceCategorical=None,treeNum=100,algorithmTypes=None,
                 randomColNum='log2',minNumObj=2,minNumPer=0,maxTreeDeep=None,maxRecorSize=100000):
        super(RandomForest, self).__init__(n_estimators=treeNum, max_depth=maxTreeDeep, max_features=randomColNum)
        if excludedColNames == None and featureColName == None:
            raise RandomForest.AttributeException()

        if excludedColNames == None:
            X_train = inputTableName.ix[:, featureColName]
        else:
            tmp = []
            tmp.append(labelColName)
            X_train = inputTableName.drop(excludedColNames + tmp, axis=1)
        y_train = inputTableName.ix[:, [labelColName]]
        self.fit(X_train, y_train)
    # def predict(self, X):
    #     y_test = super(RandomForest, self).predict(X)
    #     return pd.DataFrame(y_test, columns=['label'])


if __name__ == '__main__':

    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        iris_X, iris_y, test_size=0.3)
    input = np.concatenate((X_train, y_train[:, np.newaxis]), axis=1)
    inputTable = pd.DataFrame(input, columns=['fea_a', 'fea_b', 'fea_c', 'fea_d', 'label'])
    f = randomForest(inputTableName=inputTable, labelColName='label', excludedColNames=[])
    print(predict(f, X_test))
    predict(rd(feature.trans(preprocess.trans(data))), fea(pre(X_test)))
    class pre:
        def trans(self):
    interface trans:
        def trans()

    class pip:
        def do(self,train):
            self.model = rd( fea(pre(train)))
        def do_test(self, test, pre, fea):
            model.predict(prefea(data_test))