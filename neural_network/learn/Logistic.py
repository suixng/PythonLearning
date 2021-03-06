

#准备数据：由于需要进行距离计算，因此要求数据类型为数值型。另外结构化数据则最佳

#解析数据
def loadDataSet(file_name):
    '''
    Desc:加载并解析数据
    Args：file_name 要解析的文件路径
    Returns：
            dataMat    原始数据的特征
            labelMat    原始数据的标签，也就是每条样本对应的类别，即目标向量
    '''
    #dataMat为原始数据，labelMat为原始数据的标签
    dataMat = []
    labelMat = []
    fr = open(file_name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        #为了方便计算，我们将X0的值设为1.0，也就是在每一行开头添加一个1.0作为x0
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

#训练算法：使用梯度上升找到最佳参数

#定义Sigmoid阶跃函数
def sigmoid(inX):
    #return 1.0/(1+exp(-inX))
    #Tanh是Sigmoid的变形，与sigmoid不同的是，tanh是0的均值。因此，实际应用中tanh会比sigmoid更好
    return 2*1.0/(1+exp(-2*inX)) - 1

#Logistic回归梯度上升优化算法
#正常的处理方案
#两个参数：第一个参数==>dataMatIn是一个二维Numpy数组，每列分别代表每个不同的特征，每行则代表每个训练样本
#第二个参数==>classLabels是类别标签，他是一个1*100的行向量。为了便于矩阵计算，需要将该行向量转换为列向量，做法是将原向量转置，，再将它赋值给labelMat。
def gradAscent(dataMatIn,classLabels):
    #转化为矩阵[[1,1,3],[1,,1,2]....]
    dataMatrix = mat(dataMatIn) #转化为Numpy矩阵
    #转化为矩阵[[0,1,0,1,0,1....]],并转制[[0],[1],[0]....]
    #transpose()行列转置函数
    #将行向量转换为列向量 =>    矩阵的转置
    labelMat = mat(classLabels).transpose() #首先将数组转换为Numpy矩阵，然后将行向量转置为列向量
    #m->数据量，样本数n->特征数
    m,n = shape(dataMatrix)
    # print m, n, '__'*10, shape(dataMatrix.transpose()), '__'*100
    # alpha代表向目标移动的步长
    alpha = 0.001
    # 迭代次数
    maxCycles = 500
    # 生成一个长度和特征数相同的矩阵，此处n为3 -> [[1],[1],[1]]
    # weights 代表回归系数， 此处的 ones((n,1)) 创建一个长度和特征数相同的矩阵，其中的数全部都是 1
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        # m*3 的矩阵 * 3*1 的矩阵 ＝ m*1的矩阵
        # 那么乘上矩阵的意义，就代表: 通过公式得到的理论值
        # 参考地址:  矩阵乘法的本质是什么？ https://www.zhihu.com/question/21351965/answer/31050145
        # print 'dataMatrix====', dataMatrix 
        # print 'weights====', weights
        # n*3   *  3*1  = n*1
        h = sigmoid(dataMatrix*weights)     # 矩阵乘法
        # print 'hhhhhhh====', h
        # labelMat是实际值
        error = (labelMat - h)              # 向量相减
        # 0.001* (3*m)*(m*1) 表示在每一个列上的一个误差情况，最后得出 x1,x2,xn的系数的偏移量
        weights = weights + alpha * dataMatrix.transpose() * error # 矩阵乘法，最后得到回归系数
    return array(weights)


#画出数据集和 Logistic 回归最佳拟合直线的函数

def plotBestFit(dataArr, labelMat, weights):
    '''
        Desc:
            将我们得到的数据可视化展示出来
        Args:
            dataArr:样本数据的特征
            labelMat:样本数据的类别标签，即目标变量
            weights:回归系数
        Returns:
            None
    '''
    
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    """
    y的由来，卧槽，是不是没看懂？
    首先理论上是这个样子的。
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    w0*x0+w1*x1+w2*x2=f(x)
    x0最开始就设置为1叻， x2就是我们画图的y值，而f(x)被我们磨合误差给算到w0,w1,w2身上去了
    所以:  w0+w1*x+w2*y=0 => y = (-w0-w1*x)/w2   
    """
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X'); plt.ylabel('Y')
    plt.show()


#测试算法: 使用 Logistic 回归进行分类

def testLR():
    # 1.收集并准备数据
    dataMat, labelMat = loadDataSet("data/5.Logistic/TestSet.txt")

    # print dataMat, '---\n', labelMat
    # 2.训练模型，  f(x)=a1*x1+b2*x2+..+nn*xn中 (a1,b2, .., nn).T的矩阵值
    # 因为数组没有是复制n份， array的乘法就是乘法
    dataArr = array(dataMat)
    # print dataArr
    weights = gradAscent(dataArr, labelMat)
    # weights = stocGradAscent0(dataArr, labelMat)
    # weights = stocGradAscent1(dataArr, labelMat)
    # print '*'*30, weights

    # 数据可视化
    plotBestFit(dataArr, labelMat, weights)