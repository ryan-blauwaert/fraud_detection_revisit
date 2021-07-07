# Adapted from: https://www.kaggle.com/tilii7/hyperparameter-grid-search-with-xgboost
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier, DMatrix
from load_data import load_data

def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))



# og_params = {
#         'min_child_weight': [1, 3, 5, 7,10],
#         'gamma': [0.5, 1, 1.5, 2, 5],
#         'subsample': [0.6, 0.7, 0.8, 1.0],
#         'colsample_bytree': [0.6, 0.8, 1.0],
#         'max_depth': [3, 4, 5]
#         }
# lr_param = {'n_estimators': [125,130,135,140,145,150,155]}
# param_test1 = {
#  'max_depth':[3,4,5,6,7,8,9],
#  'min_child_weight':[1,2,3,4]}

# param_test3 = {'gamma':[0,.1,.2,.3,.4,.5,.6,.7,.8,.9]}

param_test6 = {
 'reg_alpha':[1e-5, 1e-2, 0.1, 1, 100]
}

xgb = XGBClassifier(learning_rate=0.1, n_estimators=140, objective='binary:logistic',
                     nthread=4, eval_metric='logloss', max_depth=8, min_child_weight=1, gamma=0.5, subsample=0.8, colsample_bytree=0.6, scale_pos_weight=1)

if __name__=="__main__":


    X, y = load_data(True,True)
    # print(X.info())
    folds = 10
    # param_comb = 5

    skf = StratifiedKFold(n_splits=folds, shuffle = True)

    # random_search = RandomizedSearchCV(xgb, param_distributions=param_test6, n_iter=param_comb, scoring='roc_auc', n_jobs=4, cv=skf.split(X,y), verbose=3, random_state=1001 )

    # # Here we go
    # start_time = timer(None) # timing starts from this point for "start_time" variable
    # random_search.fit(X, y)
    # timer(start_time) # timing ends here for "start_time" variable

    # print('\n All results:')
    # print(random_search.cv_results_)
    # print('\n Best estimator:')
    # print(random_search.best_estimator_)
    # print('\n Best normalized gini score for %d-fold search with %d parameter combinations:' % (folds, param_comb))
    # print(random_search.best_score_ * 2 - 1)
    # print('\n Best ROC_AUC score:')
    # print(random_search.best_score_)
    # print('\n Best hyperparameters:')
    # print(random_search.best_params_)


    tuned = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.6, eval_metric='logloss',
              gamma=0.5, gpu_id=-1, importance_type='gain',
              interaction_constraints='', learning_rate=0.1, max_delta_step=0,
              max_depth=8, min_child_weight=1, missing=None,
              monotone_constraints='()', n_estimators=140, n_jobs=4, nthread=4,
              num_parallel_tree=1, random_state=0, reg_alpha=0.01, reg_lambda=1,
              scale_pos_weight=1, subsample=0.8, tree_method='exact',
              validate_parameters=1, verbosity=None)
    fs = []
    roc = []
    
    for train, test in skf.split(X,y):
        tuned.fit(X.iloc[train], y.iloc[train])
        pred = tuned.predict(X.iloc[test])
        fs.append(f1_score(y.iloc[test], pred))
        roc.append(roc_auc_score(y.iloc[test], pred))
    print(f'Max F1: {max(fs)}')
    print(f'Mean F1: {np.mean(fs)}')
    print(f'Max ROC AUC: {max(roc)}')
    print(f'Mean ROC AUC: {np.mean(roc)}')