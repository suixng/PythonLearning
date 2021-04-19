

#收集数据：
def createDataSet():
    dataSet = [[1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#准备数据:树构建算法


#分析数据
#计算给定数据集的香农熵的函数

def calcShannonEnt(dataSet):
    #求list的长度，表示计算参与训练的数据量
    numEntries = len(dataSet)
    #计算分类标签label出现的次数
    labelCounts = {}
    #the number of unique elements and their occurrence
    for featVec in dataSet:
        #将当前实例的标签存储，即每一行数据的最后一个数据代表的是标签
        currentLabel = featVec[-1]
        #为所有可能的分类创建字典，如果当前的键值不存在，则扩展字典并将当前键值加入字典。每个键值都记录了当前类别出现的次数
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    
    #对于label标签的占比，求出label标签标签的香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        #使用所有类标签的发生频率计算类别出现的频率
        prob = float(labelCounts[key])/numEntries
        #计算香农熵，以2为底求对数
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

#按照给定特征分数据集

def splitDataSet(dataSet,index,value):
    """
    splitDataSet(通过遍历dataSet数据集,求出index对应的colnum列的值为value的行)
    就是根据index列进行分类，如果index列的数据等于value的时候，就是将index划分到创建的新数据集中
    Args:
        dataSet 数据集  待划分的数据集
        index 表示每一行的index列   划分数据集的特征
        value 表示index列对应的value值  需要返回的特征的值
    Returns:
        index列为value的数据集【该数据集需要排除index列】
    """
    retDataSet = []
    for featVec in dataSet:
        #index列为value的数据集【该数据集需要排除index列】
        #判断index列的值是否为value
        if featVec[index] == value:
            #chop out index used for splitting
            #[:index]表示前index行，即若index为2，就是取featVec的前index行
            reducedFeatVec = featVec[:index]
            '''
            请百度查询一下:  extend和append的区别
            music_media.append(object) 向列表中添加一个对象object
            music_media.extend(sequence) 把一个序列seq的内容添加到列表中 (跟 += 在list运用类似， music_media += sequence)
            1、使用append的时候，是将object看作一个对象，整体打包添加到music_media对象中。
            2、使用extend的时候，是将sequence看作一个序列，将这个序列和music_media序列合并，并放在其后面。
            music_media = []
            music_media.extend([1,2,3])
            print music_media
            #结果: 
            #[1, 2, 3]
            
            music_media.append([4,5,6])
            print music_media
            #结果: 
            #[1, 2, 3, [4, 5, 6]]
            
            music_media.extend([7,8,9])
            print music_media
            #结果: 
            #[1, 2, 3, [4, 5, 6], 7, 8, 9]
            '''

            reducedFeatVec.extend(featVec[index+1:])
            #[index+1:]表示从跳过index的index+1行，取接下来的数据
            #收集结果值index列为value的行【该行需要排除index列】
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方式

