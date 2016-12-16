# -*- coding: utf-8 -*-
#统计分析
#数据视图
def DataView(inputTable,featureColNames,labelColName=None,enumerateCol=None,bins=100,isSparse=False):
    """
    inputTableName:必选，输入表
    featureColNames:必选，特征列，任意类型都会转成double
    labelColName:可选，分类标签列
    enumerateCol:可选，特殊枚举列，勾选的特征将被试做枚举特征处理
    bins:可选，连续特征离散区间数，默认为100
    isSparse:可选，是否为稀疏格式，默认为False
    
    outputTableName:转换后的数据输出表
    EigMapTable:string字段特征值映射表
    """
    return outputTable,EigMapTable
    
#协方差
def Covariance(inputTable,selectedColNames=colNames,**kwargs):
    """
    selectedColNames:输入列，默认全选
    
    outputTableName:输出协方差数据表（图）
    """
    return outputTable
    
#经验概率密度图
def Empirical_Probability_Density(inputTable,selectedColNames,labelColName=None,bins=None,**kwargs):
    """
    selectedColNames:必选，输入列
    labelColName:可选，标签列
    bins:可选，计算频次区间数
    """
    return outputTable
    
#全表统计
def Statistics(inputTable,selectedColNames,**kwargs):
    """
    selectedColNames:必选，输入列
    """
    return outputTable
#卡方拟合性检验
def chisq_Test(inputTable,colName,probConfig):
    """
    colName:必选，检验列
    probConfig:可选，类别概率，默认为所有类别概率相等
    """
    return SampleDataTable,outputTable
    
#卡方独立性检验
def Chisq_Independence_Test(inputTable,xLabel,yLabel):
    """
    xLabel:必选，x列
    yLabel:必选，y列
    
    outputWordsTable:停用词表
    """
    return outputTable,outputWordsTable
    
#箱线图
def boxplot_Linear(inputTable,continuousCol,enumerateCol,Sample=1000):
    """
    continuousCol:必选，连续类型特征，可多选
    enumerateCol:必选，枚举类型特征
    Sample:可选，分层样本采用数，可多选
    
    输出为箱线图可视化
    """
    return 0
    
#散点图
def Scatter(inputTable,featureColNames,labelColName=None,Sample=1000):
    """
    featureColNames:必选，特征列
    labelColName:可选，分类标签列
    Sample:可选，抽样样本数，默认为1000
    
    输出为散点图可视化
    """
    return 0
    
#相关系数矩阵
def Correlation_Coefficient(inputTable,selectedColNames=colNames,**kwargs):
    """
    selectedColName:可选，默认全选
    
    outputTableName:输出相关系数矩阵
    """
    return outputTable
    
#双样本T检验
def Two_Sample_Ttest(leftTable,rightTable,leftColNames,rightColNames,testType=0,alternative='two.sided',confidence=0.95,mu=0,VarIsEqual=False):
    """
    leftTableName:必选，输入表，样本1
    rightTableName:必选，输入表，样本2
    leftColNames:必选，样本1所在列
    rightColNames:必选，样本2所在列
    testType:必选，T检验类型，支持独立性T检验（0），配对性T检验（1），默认为0
    alternative:可选，对立假设类型，支持two.sided,less,greater,默认为two.sided
    confidence:可选，置信度，默认为0.95
    mu:可选，假设均值，默认为0
    VarIsEqual:可选，两总体方差是否相等，默认为False
    
    outputTableName:输出T检验结果
    """
    return outputTable
    
#单样本T检验
def T_Test(inputTable,selectedCol,alternative='two.sided',mu=0,confidence=0.95):
    """
    alternative:可选，对立假设类型，支持two.sided,less,greater,默认为two.sided
    confidence:可选，置信度，默认为0.95
    mu:可选，假设均值，默认为0
    VarIsEqual:可选，两总体方差是否相等，默认为False
    """
    return outputTable
    
#Quantile
def Quantile(inputTable,selectedColNames,quantile=100,**kwargs):
    """
    selectedTableName:必选，字段列
    quantile:可选，分位数，默认为100
    """
    return outputTable
    
#百分位
def percentile(inputTable,selectedColNames,**kwargs):
    """
    selectedTableName:必选，输入列
    """
    return outputTable
    
#皮尔森系数
def Pearson(inputTable,col1Name,col2Name):
    """
    col1Name:必选，输入列1
    col2Name:必选，输入列2
    """
    return outputTable

#直方图
def Histogram(inputTable,selectedColNames,bins=100):
    """
    selectedColNames:必选，字段列
    bins:可选，区间个数，默认为100
    
    
    
    """
    return outputTable
    
#离散值特征分析
def Enum_Feature_Selection(inputTable,labelColName,featureColNames,isSparse=False):
    """
    labelColName:必选，标签列
    featureColNames:必选，特征列
    isSparse:可选，是否为稀疏格式，默认为False
    
    outputCntTableName:输出离散特征的枚举值分布数表
    outputValueTableName:输出离散特征的gini，entroy表
    outputEnumValueTableName:输出离散特征枚举值gini，entropy表
    """
    return outputCntTable,outputValueTable,outputEnumValueTable