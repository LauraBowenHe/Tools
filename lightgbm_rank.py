### just find that lightgbm can also be used for ranking with lambdarank
### and in my experiments, with public dataset Microsoft, it's much faster than xgboost
### below is my demo


import lightgbm as lgb

clf = lgb.LGBMRanker(boosting_type='gbdt', num_leaves=63, max_depth=5, learning_rate=0.1, n_estimators=500)
clf.fit(train[names], train['label'], group=train_group, eval_set=[(test[names], test['label'])],
        eval_group=[test_group], eval_at=[1, 3, 5, 10], early_stopping_rounds=100)
modelpath = '../graph'
modelname = 'msltr_lgb_train.model'
if not os.path.exists(modelpath):
    os.mkdir(modelpath)
print("save model...")
joblib.dump(clf, os.path.join(modelpath, modelname))

print("predict...")
### num_iteration can limit how many estimators you finally use for ranking
pred_300 = clf.predict(test[names], group=test_group, num_iteration=300)
