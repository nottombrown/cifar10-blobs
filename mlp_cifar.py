import tensorflow as tf

IMAGE_HEIGHT = 32
IMAGE_WDTH = 32

def mlp_conv_net(image):
    i = tf.reshape(image, shape=[-1, ])