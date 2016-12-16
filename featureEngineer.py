# -*- coding: utf-8 -*-
# -*-特征工程-*-

#特征尺度变换
def Feature_Scale(inputTable,scaleCols,categoryCols=None,labelCol=None,scaleMethod=np.log2,scaleTopN=10,isSparse=False,**kwargs):
    """#inputTable:必选，输入表
    #scaleCols:必选，需要进行尺度变换的特征列列名
    #categoryCols:可选，默认为空，将勾选到的枚举特征视作枚举特征处理，不支持缩放
    #labelCol:可选，标签字段，若设该列，可视化特征到目标变量的x-y分布直方图
    #scaleMethod:可选，默认为log2,支持log2,log10,ln,abs,sqrt
    #scaleTopN:当scaleCols未被勾选时，自动挑选top10个需要缩放的特征
    #isSparse：可选，是否是k:v的稀疏特征，默认为稠密数据"""
    return outputTable

#特征异常平滑
def Feature_Soften(inputTable,softCols,categoryCols=None,labelCol=None,softmethod='zscore',cl=3,minPer=0.0,maxPer=1.0,minThresh=-9999,maxThresh=9999,softenTopN=10,isSparse=False,**kwargs):
    """#inputTable:必选，输入表
    #softCols:必选，指定进行特征平滑的列
    #categoryCols:可选，默认为空，将勾选到的枚举特征视作枚举特征处理，不支持平滑
    #labelCol:可选，标签字段，若设该列，可视化特征到目标变量的x-y分布直方图
    #softmethod:可选，平滑方法。默认为zscore，可支持阈值平滑，百分位平滑
    #cl:可选，置信水平，zscore生效时使用，默认为3
    #minPer,maxPer:最低百分位和最高百分位，当平滑方法为百分位平滑时生效
    #minThresh,maxThresh：最小阈值和最大阈值，当平滑方法为阈值平滑时生效
    #softenTopN:当softCols没有勾选时，自动挑选top10个需要平滑的特征
    #isDparse:可选，是否是k:v的稀疏特征，默认为稠密数据"""
    return outputTable
    
#one-hot编码
def One_Hot_Encoding(inputTable,binaryCols,binStrategy,labelCol=None,impurityMergeThresh=0.1,densityMergeThresh=0.01,binaryReserve=False,**kwargs):
    """#inputTable:必选，输入表
    #binaryCols:必选，二值化列
    #binStrategy:必选，二值化方式，有简单二值化，按密度二值化，按纯度二值化
    #labelCol:可选，当参数为纯度二值化时，必选
    #impurityMergeThresh:可选，默认为0.1，按纯度二值化中，前后二值化特征合并纯度提升阈值
    #densityMergeThresh:可选，默认为0.01，按密度二值化中，前后二值化特征密度合并阈值
    #binaryReserve:可选，默认为False，是否在输出表中保留原独热编码特征
    
    #outputTable:输出表
    #binaryIndexTable:输出映射表
    #modelTable:输出模型表"""
    return outputTable,binaryIndexTable,modelTable
    
#特征离散
def Feature_Discrete(inputTable,discreteCols,labelCols=None,categoryCols=None,discreteMethod='SameDistance',maxBins=100,discreteTopN=10,isSparse=False,reserve=False):
    """#inputTable:必选，输入表
    #discreteCols:必选，离散化列
    #labelCols:可选，若设该列，可视化特征到目标变量的x-y分布直方图
    #categoryCols:可选，默认为空，将勾选到的枚举特征视作枚举特征处理，不支持离散化
    #discreteMethod:可选，默认为“sameDistance”,支持sameDistance,sameFrequency,基于Gini增益，基于熵增益
    #maxBins:可选，离散区间最大值，默认为100
    #discreteTopN:当discreteCols没有勾选时，自动挑选top10个需要平滑的特征
    #isSparse:可选，是否是k:v的稀疏特征，默认为稠密数据
    #reverse:可选，是否保留原离散特征，默认为False"""
    return outputTable,modelTable
    
#主成分分析
def PCA(inputTable,selectedColNames,transType='simple',calcuType='CORR',contriRate=0.9,remainColumns=None):
    """#inputTableName:必选，输入表
    #selectedColNames:必选，参与主成分分析的特征列
    #transType:可选，原表转换为主成分表的方式，支持simple,sub_mean,normalization,默认为simple
    #calcuType:可选，对原表进行特征分解的方式，支持CORR,COVAR_SAMP,COVAR_POP,默认为CORR
    #contriRate:可选，降维后数据信息保留的百分比，默认为0.9
    #remainColumns:可选，保留原表数据的列
    
    #outputTableName:进行主成分降维后的输出表
    #eigOutputTableName:特征向量和特征值的输出表"""
    return outputTable,eigOutputTable
    
#GBDT特征重要性评估
def GBDT_Importance(inputTable,modelName,labelColName,featureColNames=feature,**kwargs):
    """#inputTableName:必选，输入数据表
    #modelName:必选，输入GBDT模型
    #labelColName:必选，标签列
    #featureColNames:可选，输入表选择的特征，默认为除标签列的所有特征
    
    # **kwargs可包含lifecycle,cpreNum,memSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，默认自动分配
    #memSizePerCore:可选，每个核心的内存，默认系统自动分配
    
    #outputTable:输出特征重要性表"""
    return outputTable

#线性模型特征重要性    
def Regression_Importance(inputTable,modelName,labelColName,featureColNames=feature,enableSparse=False,**kwargs):
    """#inputTableName:必选，输入数据表
    #modelName:必选，输入线性模型
    #labelColName:必选，标签列
    #featureColNames:可选，输入表选择的特征，默认为除标签列的所有特征
    #enableSparse:可选，输入表数据是否为稀疏格式，默认为False
    
    # **kwargs可包含lifecycle,cpreNum,memSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，默认自动分配
    #memSizePerCore:可选，每个核心的内存，默认系统自动分配
    
    #outputTable:输出特征重要性表"""
    return outputTable
#随机森林特征重要性
def RandomForest_Importance(inputTable,modelName,labelColName,featureColNames=feature,**kwargs):
    """#inputTableName:必选，输入数据表
    #modelName:必选，输入线性模型
    #labelColName:必选，标签列
    #featureColNames:可选，输入表选择的特征，默认为除标签列的所有特征
    
    # **kwargs可包含lifecycle,cpreNum,memSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，默认自动分配
    #memSizePerCore:可选，每个核心的内存，默认系统自动分配
   
    #outputTable:输出特征重要性表"""
    return outputTable
 
#特征重要性过滤(不确定)
def Importance_Filter(intputTable,featureImportanceTable,featureColNames=colNames,weightColName=,TopN=10,Descending=True):
    """
    inputTableName:必选，输入表？？？
    featureImportanceTable:必选，特征重要性表
    featureColNames:可选，特征表，默认全选
    weightColName:可选，特征权重列，默认为重要性表第二列
    TopN:可选，挑选TopN特征，默认为10
    Descending:可选，特征权重降序排列，默认为True
    """
    return outputDetailTable
    



#过滤式特征选择
def Feature_Select(inputTable,selectCols,labelCol,categoryCols=None,selectMethod='iv',topN=10,discreteMethod='auto',maxBins=100,isSparse=False,**kwargs):
    """#inputTable:必选，输入表
    #selectCols:必选，选择特征列
    #labelCols:必选，标签列
    #categoryCols:可选，枚举特征
    #selectMethod:可选，特征选择方法，默认为IV，支持IV，信息增益，Gini增益，Lasso方法
    #topN:可选，挑选topN特征，默认为10
    #discreteMethod:可选，连续特征分区方式，默认为自动化分区，支持自动化分区，等距离分区
    #maxBins:可选，分区最大值，在等距离分区下使用，默认为100
    #isSparse:可选，是否为稀疏特征，默认为False
    
    #outputTable:输出表
    #feaImportanceTable:特征权重输出表"""
    return outputTable,feaImportanceTable

#特征编码
def Feature_Encoding(inputTable,modelName,labelCol,feaColNames):
    """#inputTableName:必选，训练数据表
    #modelName:必选，输入GBDT模型
    #labelCol:必选，标签列
    #feaColNames:必选，特征列（int/float）
    
    #outputTable:输出编码后的特征数据"""
    return outputTable

#窗口变量统计
def Window_Var_Statistics(inputTable,userName,dtName,cntName,amtName,window,mapInstanceNum=2,reduceInstanceNum=2):
    """#inputTableName:必选，输入数据表
    #userName:必选，用户id列
    #dtName:必选，时间分区（列），时间窗口最小单元
    #cntName:必选，次数列，对应分区时间内的行为次数
    #amtName:必选，总和列，对应分区时间内的总和
    #window:必选，时间窗口
    #maInstanceNum:可选，Mapper并发数，默认为2
    #reduceInstanceNum:可选，Reducer并发数，默认为2"""
    return outputTable