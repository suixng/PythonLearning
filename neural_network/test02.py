import numpy 
import numpy as np
import scipy.special
import matplotlib.pyplot
import pylab
 
#神经网络类
class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes,learningrate):
        # inputnodes输入节点数目，即图像的宽*高=28*28=784
        self.inodes = inputnodes
        self.hnodes= hiddennodes
        self.onodes = outputnodes
 
        #初始化权重服从正态分布
        self.wih= numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
 
        self.lr = learningrate
 
        #激活函数
        self.activation_function = lambda x:scipy.special.expit(x)
        pass
 
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
 
        #正向推算
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
 
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
 
        #误差反向推算
        output_errors = targets - final_outputs
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
 
        hidden_errors = numpy.dot(self.who.T, output_errors)
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass
 
    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
 
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
 
        return final_outputs
 
#训练神经网络
input_nodes = 784
hidden_nodes = 100
output_nodes = 10
 
learning_rate = 0.05
 
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
 
#training_data_file = open("F:/class/neural_network", 'r')
red = np.load("F:/class/neural_network/mnist.npz")
training_data_file = red.files
training_data_file = red['x_train']
training_data_list = training_data_file.readlines()
training_data_file.close()
 
epochs = 20
 
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99)+0.01
 
        targets = numpy.zeros(output_nodes)+0.01
        targets[int(all_values[0])] = 0.99
 
        n.train(inputs, targets)
        pass
    pass
 
#测试神经网络
#test_data_file = open("F:/class/neural_network", 'r')
read = np.load("F:/class/neural_network/mnist.npz")
test_data_file = read.files
test_data_file = read['x_test']
test_data_list = test_data_file.readlines()
test_data_file.close()
 
scorecard = []
 
for record in test_data_list:
    record_value = record.split(',')
 
    image_array = numpy.asfarray(record_value[1:]).reshape(28, 28)
    matplotlib.pyplot.imshow(image_array, cmap="Greys", interpolation='None')
    pylab.show()
 
    inputs = (numpy.asfarray(record_value[1:]) / 255.0 * 0.99) + 0.01
    correct_label = int(record_value[0])
 
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
 
    if(label == correct_label):
        print("right:", label)
        scorecard.append(1)
    else:
        print("wrong:", label,"v", correct_label)
        scorecard.append(0)
        pass
    pass
 
scorecard_array = numpy.asarray(scorecard)
print("performance= ", scorecard_array.sum() / scorecard_array.size)