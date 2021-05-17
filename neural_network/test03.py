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
print(a)

print(X)
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




