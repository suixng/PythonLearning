# 对MNIST数据集做卷积操作

#-*- codeing = utf-8 -*-
#@Time :2021/5/17 21:10
#@Author :Onion
#@File :ConMnistDemo.py
#@Software :PyCharm

# 对MNIST数据集做卷积操作

import tensorflow as tf
# 导入 MINST 数据集

mnist=tf.keras.datasets.mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_v2_behavior()
tf.compat.v1.disable_eager_execution()
tf.compat.v1.reset_default_graph()

# 封装定义权重变量的函数(对于权重,统一使用函数truncated_normal来生成标准差为0.1的随机数为其初始胡)
def weight_variable(shape):
    initial = tf.compat.v1.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)
# 封装定义偏置变量的函数
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# 封装卷积操作
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

# 封装最大池化操作
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')
# 封装平均池化操作
def avg_pool_7x7(x):
    return tf.nn.avg_pool(x, ksize=[1,7,7,1], strides=[1,7,7,1], padding='SAME')
# 定义参数
learning_rate = 0.001
training_epochs = 3000
batch_size = 50
display_step = 1

# 定义网络结构
n_input = 784
n_labels = 10

# 输入数据x和y,y是图片的标签数据
x = tf.compat.v1.placeholder("float", [None, n_input])
y = tf.compat.v1.placeholder("float", [None, n_labels])

# 定义权重和偏置参数(在卷积神经网络中,滤波器或者说卷积核就是神经元的权重参数)
# ①定义权重
weight = {
    'W_conv1': weight_variable([5, 5, 1, 32]),
    'W_conv2': weight_variable([5, 5, 32, 64]),
    'W_conv3': weight_variable([5, 5, 64, 10])
}
# ②定义偏置
bias = {
    'b_conv1': bias_variable([32]),
    'b_conv2': bias_variable([64]),
    'b_conv3': bias_variable([10])
}


# 定义卷积层和池化层(向前传播)
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
x_image = tf.reshape(x,[-1,28,28,1])

h_conv1 = tf.nn.relu(conv2d(x_image,weight['W_conv1'])+bias['b_conv1'])
h_pool1 = max_pool_2x2(h_conv1)

h_conv2 = tf.nn.relu(conv2d(h_pool1,weight['W_conv2'])+bias['b_conv2'])
h_pool2 = max_pool_2x2(h_conv2)

h_conv3 = tf.nn.relu(conv2d(h_pool2,weight['W_conv3'])+bias['b_conv3'])
h_pool3 = avg_pool_7x7(h_conv3)

# 对最后的池化输出结果进行sotfmax映射
h_pool3_flat = tf.reshape(h_pool3,[-1,10])
y_output = tf.nn.softmax(h_pool3_flat)

# 定义损失函数和优化器(交叉熵损失函数),Adam优化器
loss = -tf.reduce_sum(y*tf.compat.v1.log(y_output))
train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(loss)
# 计算平均错误率
correct_prediction = tf.equal(tf.argmax(y_output,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 运行卷积操作
init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    sess.run(init)
    # 总共训练3000次
    for i in range(training_epochs):
        batch = mnist.batch(batch_size=batch_size)  # 50
        # 每训练20次打印一次准确率
        if i % 20 == 0:
            train_accuracy = accuracy.eval(feed_dict={
                x: batch[0], y: batch[1]})
            print("step %d, training accuracy %g" % (i, train_accuracy))
        train_step.run(feed_dict={x: batch[0], y: batch[1]})

    # 使用测试集对模型的准确率进行测试
    print("test accuracy %g" % accuracy.eval(feed_dict={
        x: test_images, y: test_labels}))
