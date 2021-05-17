import pandas
import matplotlib.pyplot as plt
import numpy as np

iris = pandas.read_csv("F:/class/neural_network/2/iris.csv")
# shuffle rows
shuffled_rows = np.random.permutation(iris.index)
iris = iris.loc[shuffled_rows,:]
print(iris.head())
# There are 2 species
print(iris.species.unique())

# 添加一个值全为1的属性iris["ones"]，截距
iris["ones"] = np.ones(iris.shape[0])
X = iris[['ones', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
# 将Iris-versicolor类标签设置为1，Iris-virginica设置为0
y = (iris.species == 'Iris-versicolor').values.astype(int)
a = []
for i in shuffled_rows:
    if(iris['species'][i]=='Iris-setosa'):
        a.append(0)
        i+=1
    elif(iris['species'][i]=='Iris-virginica'):
        a.append(1)
        i+=1
    else:
        a.append(2)
        i+=1
#print(a)
# a = np.asarray(a)
# y = a
#print(X)
print (y)

# The first observation
x0 = X[0]

# 随机初始化一个系数列向量
theta_init = np.random.normal(0,0.01,size=(5,1))
def sigmoid_activation(x, theta):
    x = np.asarray(x)
    theta = np.asarray(theta)
    return 1 / (1 + np.exp(-np.dot(theta.T, x)))

a1 = sigmoid_activation(x0, theta_init)
print(a1)

# First observation's features and target
x0 = X[0]
y0 = y[0]

theta_init = np.random.normal(0,0.01,size=(5,1))
def singlecost(X, y, theta):
    # Compute activation
    h = sigmoid_activation(X.T, theta)
    # Take the negative average of target*log(activation) + (1-target) * log(1-activation)
    cost = -np.mean(y * np.log(h) + (1-y) * np.log(1-h))
    return cost

first_cost = singlecost(x0, y0, theta_init)

# Initialize parameters
theta_init = np.random.normal(0,0.01,size=(5,1))

# Store the updates into this array
grads = np.zeros(theta_init.shape) # (5,1)

# Number of observations 
n = X.shape[0]
for j, obs in enumerate(X):
    # 计算预测值h(xi)
    h = sigmoid_activation(obs, theta_init)
    # 计算参数偏导δi
    delta = (y[j]-h) * h * (1-h) * obs
    # 对δi求平均
    grads += delta[:,np.newaxis]/X.shape[0]
print(grads)

theta_init = np.random.normal(0,0.01,size=(5,1))

# set a learning rate
learning_rate = 0.1
# maximum number of iterations for gradient descent
maxepochs = 10000       
# costs convergence threshold, ie. (prevcost - cost) > convergence_thres
convergence_thres = 0.0001  

def learn(X, y, theta, learning_rate, maxepochs, convergence_thres):
    costs = []
    # 计算一个样本产生的误差损失
    cost = singlecost(X, y, theta) 
    # 0.01+阈值是为了在第一次迭代后与前一次（初始化为第一个样本的误差）误差的差值大于阈值
    costprev = cost + convergence_thres + 0.01  
    counter = 0 
    for counter in range(maxepochs):
        grads = np.zeros(theta.shape) # 初始化梯度为全0向量
        for j, obs in enumerate(X): # for循环计算总样本的平均梯度
            h = sigmoid_activation(obs, theta)   
            delta = (y[j]-h) * h * (1-h) * obs  
            grads += delta[:,np.newaxis]/X.shape[0]  
        # 更新参数，由于J(Θ)前面加了负号，因此求最大值，所有此处是+
        theta += grads * learning_rate
        counter += 1 
        costprev = cost  # 存储前一次迭代产生的误差
        cost = singlecost(X, y, theta) # compute new cost
        costs.append(cost)
        if np.abs(costprev-cost) < convergence_thres: # 两次迭代误差大于阈值退出
            break

    plt.plot(costs)
    plt.title("Convergence of the Cost Function")
    plt.ylabel("J($\Theta$)")
    plt.xlabel("Iteration")
    plt.show()
    return theta

theta = learn(X, y, theta_init, learning_rate, maxepochs, convergence_thres)





