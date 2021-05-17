import numpy as np
red = np.load("F:/class/neural_network/mnist.npz")
print(red.files)
x_train,y_train = red['x_train'],red['y_train']
x_test,y_test = red['x_test'],red['y_test']
print(x_train)
red.close()