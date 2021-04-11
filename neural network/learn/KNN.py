







#准备数据：使用python解析文本文件

def file2matrix(filename):
    """
    Desc:
        导入训练数据
    parameters:
        filename:数据文件路径
    return:
        数据矩阵 returnMat和对应的类别 classLabelVector
    """
    fr = open(filename)
    #获取文件中的数据行的行数
    numberOfLines = len(fr.readlines())
    #生成对应的空矩阵
    #例如：zeros(2,3)就是生成一个2*3的矩阵，各个位置上全是0
    returnMat = zeros((numberOfLines,3))    #prepare matrix to return
    classLabelVector = []   #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        #str.strip([chars])--返回已移除字符串头尾指定字符生成的新字符串
        line = line.strip()
        #以'\t'切割字符串
        listFromLine = line.split('\t')
        #每列的属性数据
        returnMat[index,:] = listFromLine[0:3]
        #每列的类别数据，就是label标签数据
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    #返回数据矩阵returnMat和对应的类别classLabelVector
    return returnMat,classLabelVector

#分析数据：使用Matplotlib画二维散点图

import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()

#归一化数据

def autoNorm(dataSet):
    """
    Desc:
        归一化特征值,消除特征之间量级不同导致的影响
    parameter:
        dataSet：数据集
    return:
        归一化后的数据集normDataSet. ranges和minVals即最小值与范围，并没有用到

    归一化公式：
        Y = (X-Xmin)/(Xmax=Xmin)
        其中的min和max分别是数据集中的最小特征值和最大特征值。该函数可以自动将数字特征值转化为0到1的区间
    """
    #计算每种属性的最大值、最小值、范围
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    #极差
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #生成与最小值之差组成的矩阵
    normDataSet = dataSet -tile(minVals,(m,1))
    #将最小值之差除以范围组成矩阵
    normDataSet = normDataSet / tile(ranges,(m,1))  #element wise divide
    return normDataSet,ranges,minVals


#训练算法：此步骤不适用于k-近邻算法

def classify0(inX,dataSet,labels,k):
    """
    对于每一个在数据集中的数据点：
        计算目标的数据点(需要分类的数据点)与该数据点的距离
        将距离排序：从小到大
        选取前K个最短距离
        选取这K个中最多的分类类别
        返回该类别来作为目标数据点的预测值
    """
    dataSetSize = dataSet.shape[0]
    #距离度量 度量公式为欧氏距离
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    #将距离排序：从小到大
    sortedDistIndicies = distances.argsort()
    #选取前K个最短距离，选取这K个中最多的分类类别
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][10]

#测试算法：使用提供的部分数据作为测试样本。如果预测分类与实际分类不同，则标记为一个错误
def datingClassTest():
    """
    Desc:
        对网站的测试方法
    parameters:
        none
    return:
        错误数
    """
    #设置测试数据的一个比例(训练数据集比例=1-hoRatio)
    hoRatio = 0.1   #测试范围，一部分测试一部分作为样本
    #从文本中加载数据
    datingDataMat,datingLabels = file2matrix('learn/datingTestSet2.txt')  #load data setfrom file
    #归一化数据
    normMat,ranges,minVals = autoNorm(datingDataMat)
    # m表示数据的行数，即矩阵的第一维
    m = normMat.shape[0]
    # 设置测试的样本数量，numTestVecs:m表示训练样本的数量
    # numTestVecs = int(m*hoRatio)
    # print 'numTestVecs=',numTestVecs
    # errorCount = 0.0
    # for i in range(numTestVecs):
    #     #对数据进行测试
    #     classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
    #     print"the classifier came back with: %d,the real answer is: %d" %(classifierResult,datingLabels[i])
    #     if(classifierResult != datingLabels[i]):
    #         errorCount += 1.0
    #     print "the total error rate is: %f" %(errorCount / float(numTestVecs))
    #     print errorCount

#使用算法：产生简单的命令行程序，然后可以输入一些特征数据以判断对方是否为自己喜欢的类型
def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent filer miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLables = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentsTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLables,3)
    print"You will probably like this person:",resultList[classifierResult - 1]
   
