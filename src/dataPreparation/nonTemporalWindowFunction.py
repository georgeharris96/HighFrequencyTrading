# Import requried libraries
import pandas as pd
import tensorflow as tf
import numpy as np

def nonTemporalTransform(X, y, window_size):
    """

    :param X: X values in pandas dataframe format
    :param y: y values in pandas dataframe format
    :param window_size: size of prediction window
    :return:
    """
    # Convert to tensor format
    X_tensor = tf.convert_to_tensor(X)
    y_tensor = tf.convert_to_tensor(y)

    # Create list for stack
    X_tensor_stack = []

    # Package loop
    for i, _ in enumerate(X_tensor):
        i += window_size

        packet = X_tensor[:-1][i-window_size:i]
        X_tensor_stack.append(packet)

    # Convert stack into one tensor
    X_reshape = tf.stack(X_tensor_stack[:len(X_tensor_stack)-window_size])

    # Find target values
    y_reshape = y_tensor[window_size:]

    return X_reshape, y_reshape

