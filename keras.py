### This file contains some utilities I find useful.

### About keras.backend

import keras.backend as K

### extract from tensor by index
index = [1,2,3,4,5]
tensor # which is a tensor, the values is [0,1,2,3,4,5,6,7,8]
K.gather(tensor, index) # -> the value is [1,2,3,4,5]

### make tensor repeat along axis
tensor = [[1],[2],[3]] #shape = [3,1]
K.repeat_elements(tensor, rep=3, axis=1) # [[1,1,1], [2,2,2], [3,3,3]]

### get the euclidian distance for two matrix
#   step1 get sample3 |sample3|^2,
#   step2 get sample4 transpose |tran(sample4)|^2
#   step3 get two matrix product sample3*tran(sample4)
#   step4 |sample3|^2 + |tran(sample4)|^2 - 2*sample3*tran(sample4)
def pairwise_dis(sample3, sample4):
    sample3_norm2 = K.repeat_elements(K.reshape(K.sum((sample3*sample3), axis=1), shape=(max_len,1)), rep=20, axis=1)
    sample4_trans = K.transpose(sample4)
    sample4_norm2 = K.repeat_elements(K.reshape(K.sum((sample4_trans*sample4_trans), axis=0), shape=(1,max_len)), rep=20, axis=0)   
    mul = K.dot(sample3, K.transpose(sample4)) # (20, 20)        
    tmp = sample3_norm2 + sample4_norm2 - 2*mul # (20, 20)
    return K.abs(K.mean(K.max(tmp, axis=1)))
    
    
### multiple output, multiple metrics
model.compile(loss=[custom_loss],
                  optimizer=sgd,
                  metrics={'output2':'categorical_accuracy'})

### 
