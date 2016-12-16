# -*- coding: utf-8 -*-
# -*- 数据预处理 -*-
#加权采样
def Weight_Sample(inputTable,probCol,sampleSize=None,sampleRatio=None,replace=False,**kwargs):
    """inputTableName:必选，输入表表名
    #probCol:必选，要加权的列
    #inputTablePartitions:可选，输入表需参加采样的分区（属性）,默认为全表
    
    #sampleSize:可选，采样个数，与采样比例二选一，正整数，默认为空
    #sampleRatio:可选，采样比例，与采样个数二选一，float，（0,1）,默认为空
    #当sampleSize,sampleRatio都为空时，报错，否则，以sampleSize为准
    
    #replace:可选，是否放回，boolean，默认为False，不放回
    
    # **kwargs:包含randomSeed,lifecycle,coreNum,memSizePerCore
    #randomSeed:可选，随机数种子，正整数，默认系统自动生成
    #lifecycle:可选，输出表生命周期，[1,3650]，默认输出表没有生命周期
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配"""
    return outputTable #输出结果表
    
#随机采样
def Random_Sample(inputTable,sampleSize=None,sampleRatio=None,replace=False,**kwargs):
    """#inputTableName:必选，输入表表名
    #inputTablePartitions:可选，输入表需参加采样的分区（属性）,默认为全表
    
    #sampleSize:可选，采样个数，与采样比例二选一，正整数，默认为空
    #sampleRatio:可选，采样比例，与采样个数二选一，float，（0,1）,默认为空
    #当sampleSize,sampleRatio都为空时，报错，否则，以sampleSize为准
    
    #replace:可选，是否放回，boolean，默认为False，不放回
    
    # **kwargs:包含randomSeed,lifecycle,coreNum,memSizePerCore
    #randomSeed:可选，随机数种子，正整数，默认系统自动生成
    #lifecycle:可选，输出表生命周期，[1,3650]，默认输出表没有生命周期
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配"""
    return outputTable
    
#过滤与映射
def Filter_and_Mapping(inputTable,filter_,**kwargs):
    """#inputTableName:必选，输入表表名
    
    #inputPartitions:可选，输入字段（输入表对应的输入分区），默认为全选
    #outputPartitions:可选，输出字段（用户自定义），默认为空，若为空，则输出字段即为输入字段，否则，输出字段为inputPartitions重命名为outputPartitions后的字段
    #inputPartitions和outputPartitions即可组合成映射规则
    
    #filter_:必选，过滤条件，where后的条件语句"""
    return outputTable

#分层采样    
def Stratified_Sample(inputTable,strataColName,sampleSize=None,sampleRatio=None,**kwargs):
    """#inputTableName:必选，输入表表名
    #strataColName:必选，分层列，按照此列作为key分层
    
    #sampleSize:可选，采样个数，与采样比例二选一，可为整数和字符串。整数时表示每个层次的采样个数；字符串时：格式为strata0:n0,strata1:n1表示每个stranum分别的采样个数
    #sampleRatio:可选，采样比例，与采样个数二选一，可为数字和字符串，范围（0,1）。数字时表示每个层次的采样比例；字符串时：格式为strata0:r0,strata1:r1表示每个stranum分别的采样比例
    #当sampleSize,sampleRatio都为空时，报错，否则，以sampleSize为准
    
    #randomSeed:可选，随机数种子，正整数，默认123456
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配"""
    return outputTable

#JOIN    
def Join(inputLeftTable,inputRightTable,joinType,condition,leftColNames,rightColNames,outputLeftColName=None,outputRightColName=None,**kwargs):
    """#inputLeftTableName:必选，输入左表
    #inputRightTableName:必选，输入右表
    #joinType:必选，连接类型，可有左连接，右连接，内连接，全连接
    #condition:必选，关联条件，可增加或删除关联条件，关联条件支持等式（猜测可能是字符串类型，关联条件之间用逗号分隔）？？？？
    #leftColNames:左表输入字列
    #rightColNames:右表输入列名
    #outputLeftColName:可选，左表输出字段列，字符串（为用户自定义的输出列名），用于对左表输入字列的rename
    #outputRightColName:可选，右表输出字段列，字符串（为用户自定义的输出列名），用于右表输入字列的rename"""
    return outputTable

#合并列 
#左表和右表行数需相同  
def Columns_Merge(inputLeftTable,inputRightTable,leftSelectCol=leftcols,rightSelectCol=rightcols,leftRenameCol=None,rightRenameCol=None,autoRenameCol=True,**kwargs):
    """#inputLeftTableName:必选，输入左表
    #inputRightTableName:必选，输入右表
    #leftSelectCol:可选，左表选择输出列名，若不选，默认为输出全表
    #rightSelectCol:可选，右表选择输出列名，若不选，默认输出全表
    #leftRenameCol:可选，左表rename列，默认为空
    #rightRenameCol:可选，右表rename列，默认为空
    #autoRenameCol:可选，默认为True，即自动重命名输出表重复列"""
    return outputTable ##leftrenamecol怎么和leftselectcol对应
    
#合并行
def Union(inputLeftTable,inputRightTable,leftCondition,rightCondition,leftSelectCol=leftcols,rightSelectCol=rightcols,leftRenameCol=None,rightRenameCol=None,Deduplicate=True,**kwargs):
    """#inputLeftTableName:必选，输入左表
    #inputRightTableName:必选，输入右表
    #leftCondition:必选，左表过滤条件
    #rightCondition:必选，右表过滤条件
    
    #leftSelectCol:可选，左表选择输出列名，若不选，默认为输出全表
    #rightSelectCol:可选，右表选择输出列名，若不选，默认输出全表
    #左右表选择的列数需一致，对应列的类型需一致
    
    #leftRenameCol:可选，左表rename列，默认为空
    #rightRenameCol:可选，右表rename列，默认为空
    #Deduplicate:可选，去重复行，默认为True"""
    return outputTable
    
#稠密转稀疏
def Dense_to_Sparse(inputTableName,convertCol=tablecols,retainCol=None,**kwargs):
    """#inputTableName:必选，输入表
    #convertCol:可选，转换列，默认为全选
    #retainCol:可选，保持原样列，默认为空"""
    return outputTableName
    
#类型转换
def Type_Transform(inputTable,double_selectCols=None,int_selectCols=None,string_selectCols=None,double_default=0.0,int_default=0,string_default=None,keepOriginal=False,**kwargs):
    """#inputTableName:必选，输入表
    #double_selectCols:可选，要转换为double的列，默认为空
    #int_selectCols:可选，要转换为int的列，默认为空
    #string_selectCols:可选，要转换为string的列，默认为空
    #double_default:转换为double异常时填充的值，默认为0.0
    #int_default:转换为int异常时填充的值，默认为0
    #string_default:转换为string异常时填充的值，默认为空
    #keepOriginal:可选，是否保留原列，默认为False，即不保留，若保留，增加列名“typed”"""
    return outputTable
    
#增加序号列
def Append_ID(inputTable,IDColName='append_id',selectedColNames=cols,**kwargs):
    """#inputTableName:必选，输入表
    #IDColName:可选，追加的ID列列名，默认为“append_id”
    #selectedColNames:可选，要保留的字段名，默认为保留全表"""
    return outputTable
    
#拆分
def Split(inputTable,fraction=0.8,**kwargs):
    """#inputTableName:必选，输入表
    #fraction:可选，切分比例，float，范围（0,1）,默认为0.8；假设切分比例为0.8，即将输入数据集按80:20比例划分成两个数据集，outputTableName1为80，outputTableName2为20
    # **kwargs可包含random_seed
    #random_seed:默认系统自动生成"""
    return outputTable1,outputTable2
    
#缺失值填充
def Fill_Missing_Values(inputTable,configs,inputParaTableName=None,**kwargs):
    """#inputTableName:必选，输入数据表
    
    #configs:必选，缺失值填充配属。格式为：字段名1，原值，替换值；字段名2，原值，替换值
    #原值可选：null,empty,null-empty,user-defined
    #替换值可选：min,max,mean,median(针对数值型),或者自定义(针对string型)
    #如果原值选择user-defined，则格式为：字段名，user-defined,原值，替换值（只有string型可选择user-defined）
    
    #inputParaTableName:可选，输入配属表
    #outputTableName：填充缺失值后的输出数据表
    #outputParaTableName:填充缺失值后的输出参数表
    
    # **kwargs可包含lifecycle,cpreNum,memSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配"""
    return outputTable,outputParaTable
    
#归一化
def Normalize(inputTable,inputParaTable=None,selectedColNames=cols,keepOriginal=False,**kwargs):
    """#inputTableName:必选，输入数据表
    #inputParaTableName:可选，输入参数表
    #selectedColName:可选，选择需要归一化的列（float,int型），默认为全选
    #keepOriginal:可选，保留原始列，默认为False，不保留，若保留，则处理过的列增加“normalized_”前缀
    
    # **kwargs:可包含lifecycle,coreNum,menSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配
    
    #outputTableName:输出数据表
    #outputParaTableName:输出参数表"""
    return outputTable,outputParaTable
    
#标准化
def Standardize(inputTable,inputParaTable=None,selectedColNames=cols,keepOriginal=False,**kwargs):
    """#inputTableName:必选，输入数据表
    #inputParaTableName:可选，输入参数表
    #selectedColName:可选，选择需要归一化的列（float,int型），默认为全选
    #keepOriginal:可选，保留原始列，默认为False，不保留，若保留，则处理过的列增加“normalized_”前缀
    
    # **kwargs:可包含lifecycle,coreNum,menSizePerCore
    #lifecycle:可选，输出表生命周期，[1,3650]，默认不设置
    #coreNum:可选，计算的核心数目，正整数，默认系统自动分配
    #memSizePerCore:可选，每个核心的内存，正整数(1,65536)，默认系统自动分配
    
    #outputTableName:输出数据表
    #outputParaTableName:输出参数表"""
    return outputTable,outputParaTable