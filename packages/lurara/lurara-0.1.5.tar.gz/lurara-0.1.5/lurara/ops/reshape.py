import numpy as np
import tensorflow as tf
from keras.layers import Reshape


class DimUp:
    def __new__(cls, inputs: tf.Tensor):
        return Reshape(inputs.shape.as_list()[1:] + [1])(inputs)


class DimDown:
    def __new__(cls, inputs):
        assert inputs.shape.as_list()[-1] == 1, f"inputs.shape is {inputs.shape.as_list()} and the last axis is not 1. Can not to reshape dim down."
        return Reshape(inputs.shape.as_list()[1:-1])(inputs)





