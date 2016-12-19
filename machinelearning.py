# -*- coding: utf-8 -*-
#机器学习
import numpy as pd
import pandas as pd
import sklearn
def GBDT_Classification(inputTable,FeatureColNames,LabelColName,GroupColName=columns,metricType='NDCG',treeNum=500,learnRate=0.05,trainSampleRatio=0.6,trainFeaRatio=0.6,maxLeafNum=32,testDataRatio=0,maxDeep=10,leafLeastSampleNum=500,randomSeed=0,maxSplitNum=500,**kwargs):
    """inputTableName:必选，输入数据集
    FeatureColName:必选，选择特征列，支持double,bigint
    LabelColName:必选，标签列，支持bigint，只能是二分类
    GroupColName:可选，默认全表，支持double,bigint
    metricType:可选，默认NDCG，支持DCG,NDCG
    treeNum:数的数目
    learnRate:学习速率
    trainSampleRatio:训练采集样本比例
    trainFeaRatio：训练采集特征比例
    maxLeafNum：最大叶子数
    testDataRatio：测试数据比例
    maxDeep：树最大深度
    leafLeastSampleNum：叶节点最少样本数
    randomSeed：随机数产生器种子
    maxSplitNum：一个特征的最大分割数量
    
    outputModel:模型输出"""
    print outputModel
    
#SVM
def SVM(inputTable,FeatureColNames,LabelColName,positiveLabel=None,positiveCost=1.0,negativeCost=1.0,ConverCoefficient=0.001,isSparse=False,**kwargs):
    """inputTableName:必选，输入表
    FeatureColNames:必选，特征列，支持bigint,double
    LabelColName:必选，标签列，支持bigint,double,string
    positiveLabel:可选，若没填写，则从label值中随机选择一个
    positiveCost:可选，正例惩罚因子，默认为1.0
    negativeCost:可选，负例惩罚因子，默认为1.0
    converCoefficient:可选，收敛系数，默认为0.001
    isSparse:可选，是否为稀疏特征，默认为False
    
    # **kwargs可包含cpreNum,memSizePerCore
    #coreNum:可选，计算的核心数目，默认自动分配
    #memSizePerCore:可选，每个核心的内存，默认系统自动分配
    """
    return outputModel

#逻辑回归二分类
def Logistic(inputTable,trainFeaColNames,targetCol,positiveValue=1,regular=None,maxIterations=100,regularCoefficient=1,minConverCoefficient=0.000001,isSparse=False,**kwargs):
    """inputTableName:必选，输入表
    trainFeaColNames:必选，训练特征列，支持double,int
    targetCol:必选，目标列
    positiveValue:必选，默认为1
    regular:可选，正则项，默认为None，支持L1，L2
    maxIteratons:可选，默认为100
    regularCoefficient:可选，正则系数，默认为1，正则项为None时此值无效
    minConverCoefficient:最小收敛误差，默认为0.000001
    isSparse:可选，是否为稀疏特征，默认为False
    
     # **kwargs可包含cpreNum,memSizePerCore
    #coreNum:可选，计算的核心数目，默认自动分配
    #memSizePerCore:可选，每个核心的内存，默认系统自动分配
    """
    return outputModel
    
#k近邻
def KNN(trainTable,predictTable,trainFeaColNames,trainLableCol,predictFeaColNames=None,appendColNames=None,k=100,lifecycle=7,isSparse=False):
    """trainTableName:必选，训练集
    predictTableName:必选，测试集
    trainFeaColNames:必选，选择训练表特征列
    trainLableCol:必选，选择训练表的标签列
    predictFeaColNames:可选，选择预测表的特征列
    appendColNames:可选，产出表附加ID列
    k：可选，近邻个数，默认为100
    lifecycle:输出表生命周期，可选
    isSparse:可选，是否为稀疏特征，默认为False"""
    return predictResultTable
    
#逻辑回归多分类
def Logistic_Multi_Classification(inputTable,trainFeaColNames,targetCol,regular=None,maxIterations=100,regularCoefficient=1,minEpsilon=0.000001,isSparse=False,**kwargs):
     """inputTableName:必选，输入表
    trainFeaColNames:必选，训练特征列，支持double,int
    targetCol:必选，目标列
    regular:可选，正则项，默认为None，支持L1，L2
    maxIteratons:可选，默认为100
    regularCoefficient:可选，正则系数，默认为1，正则项为None时此值无效
    minEpsilon:最小收敛误差，默认为0.000001
    isSparse:可选，是否为稀疏特征，默认为False
    """
    return outputModel
        
#随机森林
def randomForest(inputTable,labelColName,weightColName=None,featureColName=colNames,
                 excludedColNames=None,forceCategorical=None,treeNum=100,algorithmTypes=None,
                 randomColNum=log2N,minNumObj=2,minNumPer=0,maxTreeDeep=∞,maxRecorSize=100000):
    """inputTableName:必选，输入表
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
    maxTreeDeep:可选，单棵树的最大深度，默认为无穷
    maxRecorSize:可选，单棵树输入的随机数据个数，(1000,1000000]，默认为100000
    """

    return RandomForest(...)

class RandomForest:
    def __init__(self, inputTable,labelColName,weightColName=None,featureColName=colNames,
                 excludedColNames=None,forceCategorical=None,treeNum=100,algorithmTypes=None,
                 randomColNum=log2N,minNumObj=2,minNumPer=0,maxTreeDeep=∞,maxRecorSize=100000):
        self.randomForest =

#朴素贝叶斯
def NaiveBayes(inputTable,labelColName,featureColNames=colNames,excludedColNames=None,forceCategorical=None):
    """inputTableName:必选，输入表
    labelColName:必选，输入的标签列列名
    featureColName:可选，特征列，默认为除标签列的所有列
    excludedColNames:可选，排除列，即不参与特征训练的列，与特征列不共存，默认为空
    forceCategorical:可选，强制转换列，即把连续特征转换为离散特征，默认为空
    """
    return outputModel

#k均值聚类
def KMeans(inputTable,featureColNames=colNames,appendColNames=None,centerCount=10,distanceType='Euclidean',initCenterMethod='Random',initCenterTableName=None,loop=100,accuracy=0.1,seed=,isSparse=False,itemDelimiter=' ',kvDelimiter=':',**kwargs):
    """inputTableName:必选，输入数据表
    featureColNames:可选，默认为所有列，支持int和double类型
    appendColNames:可选，默认无附加列
    centerCount:可选，聚类数，[1,1000]，默认值10
    distanceType:可选，距离度量方式，默认为Euclidean,支持Euclidean,Cosine,Cityblock
    initCenterMethod:可选，质心初始化方法，默认为random，支持First k,uniform,kmeans++,使用初始质心表
    initCenterTableName:可选,默认为空
    loop:可选，最大迭代次数，[1,1000]，默认为100
    accuracy:可选，收敛标准，默认为0.1
    seed:可选，随机种子，默认为当前时间
    isSparse:可选，是否为稀疏格式，默认为False
    itemDelimiter:可选，当输入表为稀疏格式时，kv间的分割符，默认为空格
    kvDelimiter:可选，当输入表为稀疏格式时，key和value间的分割符，默认为冒号
    
    **kwargs可包含cpreNum,memSizePerCore
    coreNum:可选，计算的核心数目，默认自动分配
    memSizePerCore:可选，每个核心的内存，默认系统自动分配
    """
    return outputModel,idxTable,clusterCountTable,centerTable
    
#GBDT回归
def GBDT_Regression(inputTable,labelColName,featureColNames=colNames,groupColNames=colNames,loss='regression loss',base=1,Tau=0.6,metric=0,treeNum=500,learnRate=0.05,trainSampleRatio=0.6,trainFeaRatio=0.6,maxLeafNum=32,testDataRatio=0,maxDeep=10,leafLeastSampleNum=500,randomSeed=0,ifNewton=True,maxSplitNum=500,**kwargs):
    """
    inputTableName:必选，输入数据集
    featureColName:必选，选择特征列，支持double,bigint
    labelColName:必选，标签列，支持bigint，只能是二分类
    groupColName:可选，默认全表，支持double,bigint
    loss:可选，损失函数类型，默认为regression loss,支持gbrank loss,lambdamart dcg loss,lambdamart ndcg loss
    base:可选，gbrank和regression loss中的指数底数，默认为1，如果p>1，将样本的label映射为p&circ label；当p<=1时，不做映射，保持原来的label。范围[1,10]
    Tau:可选，gbrank loss中的Tau参数，范围[0,1]，默认0.6
    metricType:可选，默认NDCG（0），支持NDCG(0),DCG(1),AUC(2)
    treeNum:数的数目
    learnRate:学习速率
    trainSampleRatio:训练采集样本比例
    trainFeaRatio：训练采集特征比例
    maxLeafNum：最大叶子数
    testDataRatio：测试数据比例
    maxDeep：树最大深度
    leafLeastSampleNum：叶节点最少样本数
    randomSeed：随机数产生器种子
    ifNewton:是否使用newton方法来学习，默认为使用
    maxSplitNum：一个特征的最大分割数量
    """
    return outputModel
    
#线性回归
def LinearRegression(inputTable,labelColName,featureColNames,maxIter=100,epsilon=0.000001,regularType=None,regularCoefficient=1,isFitGoodness=False,isCoefficientEstimate=False,isSparse=False,**kwargs):
    """
    inputTableName:必选，输入数据表
    labelColName:必选，标签列，支持int和double类型
    featureColNames:必选，特征列
    maxIter:可选，最大迭代次数，默认为100
    epsilon:可选，最小似然误差，默认为0.000001
    regularType:可选，正则化类型，默认为None,支持L1，L2
    regularCoefficient:可选，正则化系数，默认为1
    isFitGoodness:可选，是否生成模型评估表，默认为False
    isCoefficientEstimate:可选，是否进行回归系数评估，默认为False
    isSparse:可选，是否为稀疏格式，默认为False
    
    outputTableName:输出模型评估表
    """
    return outputModel,outputTable
    
#二分类评估
def Classification_Evaluate(inputTable,labelColName,scoreColName,groupColName=None,positiveLabel=1,binCount=1000,advanced=False,predictDetail=None,drop=True,savePerformanceMetrics=True,**kwargs):
    """
    inputTableName:必选，输入表
    labelColName:必选，原始标签列列名
    scoreColName:必选，分数列列名
    groupColName:可选，分组列列名，仅支持string
    positiveLabel:可选，正样本标签列，默认为1
    binCount:可选，计算KS,PR等指标时按等频分成多少个桶
    advanced:可选，高级选项，默认为False
    predictDetail:可选，预测结果详细列
    savePerformanceMetrics:可选，是否保存性能指标，默认为True
    
    outputMetricTableName:输出综合指标表
    outputDetailTableName:输出详细数据表，包括等频详细数据和等宽详细数据表
    
    输出包括KS/PR/LIFT/ROC曲线
    """
    return outputMetricTable,outputDetailTable
    
#回归模型评估
def Regression_Evaluate(inputTable,yColName,predictionColName,intervalNum=100,**kwargs):
    """
    inputTableName:必选，输入表
    yColName:必选，原回归值
    predictionColName:必选，预测回归值
    intervalNum:可选，直方区间，默认为100
    
    输出指标包括MSE,MAE,MAPE
    """
    return indexOutputTable,residualOutputTable
    
#聚类模型评估
def Cluster_Evaluate(inputTable,inputModelName,selectedColName=colNames,isSparse=False,itemDelimiter=' ',kvDelimiter=':',**kwargs):
    """
    inputTableName:必选，输入表
    inputModelName:必选，输入聚类模型
    selectedColName:可选，参与评估列，默认为全选
    isSparse:可选，是否为稀疏格式，默认为False
    itemDelimiter:可选，当输入表为稀疏格式时，kv间的分割符，默认为空格
    kvDelimiter:可选，当输入表为稀疏格式时，key和value间的分割符，默认为冒号
    """
    return outputTable
    
#混淆矩阵
def ConfusionMatrix(inputTable,labelColName,predictionColName=None,predictionDetailColName=None,threshold=None,goodValue=None,**kwargs):
    """
    intputTableName:必选，输入表，即预测输出表
    labelColName:必选，原始标签列
    predictionColName:必选
    threshold:可选，阈值，大于该阈值为正样本
    predictionDetailColName:若指定阈值，必选，和标签列列名不能共存
    goodValue:正样本的标签值，若无阈值，可选，否则，必选
    """
    return outputTable
    
#多分类评估
def MultiClassEvaluation(inputTable,labelColName,predictionColName,predictionDetailColName=None,**kwargs):
    """
    inputTableName:必选，输入表
    labelColName:必选，原分类结果表
    predictionColName:必选，预测分类结果列
    predictionDetailColName:可选，预测结果概率列，仅对随机森林模型有效
    """
    return outputTable
    
#预测
def Prediction(inputTable,modelName,featureColNames=colNames,appendColNames=None,resultColName='prediction_result',scoreColName='prediction_score',detailColName='prediction_detail',isSparse=False,**kwargs):
    """
    inputTableName:必选，输入数据表
    modelName:必选，输入模型
    featureColNames:必选，默认全选
    appendColNames:可选，原样输出列
    resultColName:可选，输出结果列名，默认为prediction_result
    scoreColName:可选，输出结果分数列
    detailColName:输出详细列名
    isSparse:可选，是否为稀疏格式，默认为False
    
    **kwargs可包含cpreNum,memSizePerCore
    coreNum:可选，计算的核心数目，默认自动分配
    memSizePerCore:可选，每个核心的内存，默认系统自动分配
    """
    return outputTable