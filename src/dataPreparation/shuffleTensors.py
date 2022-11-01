# Import required libraries
import tensorflow as tf


def shuffle_tensors(X, y, seed=None):
    '''

    :param X:
    :param y:
    :param seed:
    :return:
    '''
    assert tf.shape(X)[0] == tf.shape(y)[0], 'X and y MUST be the same length'
    shuffled_indices = tf.random.shuffle(
        tf.range(start=0, limit=tf.shape(X)[0]),
        seed=seed
    )

    shuffled_X = tf.gather(X, shuffled_indices, axis=0)
    shuffled_y = tf.gather(y, shuffled_indices, axis=0)

    return shuffled_X, shuffled_y

