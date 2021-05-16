import numpy as np
red = np.load("F:/class/neural_network/mnist.npz")
print(red.files)
read = red['x_test']
print(read)