import numpy as np
red = np.load("F:/class/neural_network/mnist.npz")
print(red.files)
x_train,y_train = red['x_train'],red['y_train']
x_test,y_test = red['x_test'],red['y_test']
print(x_train)
red.close()
import numpy as np
import tensorflow as tf

#导入mnist数据（以one_hot的格式）

mnist=tf.keras.datasets.mnist
#遍历两次
for i in range(2):
    #每次返回两个训练集的数据
    batch=mnist.train.next_batch(2)
    #输出它的内容
    print (batch)
    #输出它的类型
    print (type(batch))
