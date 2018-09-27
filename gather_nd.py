### How to get columns of each row based on index? I get a beautiful solution from tensorflow
import tensorflow as tf

y_index = K.argmax(y_label_inputs, axis=-1)
x = tf.gather_nd(output_, tf.stack((tf.range(batch_size, 
                                    dtype=y_index.dtype),
                                    y_index), axis=1))
