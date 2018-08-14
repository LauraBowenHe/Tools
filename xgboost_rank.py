### xgboost can be used for ranking task
### a simple demo I created 

"""
Created on Wed Aug  8 15:26:32 2018

@author: bwhe
"""

import xgboost as xgb
import hickle as hkl
import os
from sklearn.externals import joblib

"""
train_x: contains all the features, data belonging to a same group are put together in consecutive
train_y: corresponding labels for tran_x
train_group: corresponding group size for train_x
"""
path = '../data/'
train_x = hkl.load(os.path.join(path, 'train_x.hkl'))
train_y = hkl.load(os.path.join(path, 'train_y.hkl'))
train_group = hkl.load(os.path.join(path, 'train_group.hkl'))
xgb_train = xgb.DMatrix(train_x, label=train_y)
xgb_train.set_group(train_group)

test_x = hkl.load(os.path.join(path, 'test_x.hkl'))
test_y = hkl.load(os.path.join(path, 'test_y.hkl'))
test_group = hkl.load(os.path.join(path, 'test_group.hkl'))
xgb_test = xgb.DMatrix(test_x, label=test_y)
xgb_test.set_group(test_group)

# train_mat.set_group(group)
print(train_x.shape)
print(train_y.shape)

print("train model...")
params = {'base_score':0.5,
	  'reg_alpha': 0.05, 
	  'colsample_bytree': 0.8, 
	  'learning_rate': 0.1, 
          'alpha': 0, 
          'gamma': 0,
          'max_depth': 8, 
          'min_child_weight': 100, 
          'missing': -999, 
          'n_estimators': 500, 
          'nthread': 40,
          'objective': 'rank:pairwise',
          'scale_pos_weight': 1, 
          'seed': 2016, 
          'silent': False, 
          'eval_metric': 'ndcg@1',
          'subsample': 0.8}

plst = list(params.items())
num_rounds = 1000 # 迭代次数
watchlist = [(xgb_train, 'train'),(xgb_test, 'test')]
clf = xgb.train(plst, xgb_train, num_rounds, watchlist,early_stopping_rounds=100)
modelpath = '../xgb_model/'
if not os.path.exists(modelpath):
	os.mkdir(modelpath)
print("save model...")
joblib.dump(clf, os.path.join(modelpath, 'xgb.model'))

print("predict...")

xgb_test = xgb.DMatrix(test_x)
xgb_test.set_group(test_group)
ypred = clf.predict(xgb_test)
hkl.dump(ypred, os.path.join(path, 'yahoo_test_pred.hkl'), mode='w', compression='gzip')
