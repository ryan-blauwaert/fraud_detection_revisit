import pandas as pd 
import numpy as np 
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV,StratifiedKFold
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier
from load_data import load_data



def grid_search():
    estimator = XGBClassifier(eval_metric='logloss') #objective='binary:logistic'
    params = {
        'min_child_weight': [1, 10],
        'gamma': [0.5, 5],
        'subsample': [0.6, 1.0],
        'colsample_bytree': [0.6, 1.0],
        'max_depth': [3, 5]
        }
    grid_search = GridSearchCV(
        estimator=estimator,
        param_grid=params,
        scoring='roc_auc',
        cv=5,
        n_jobs=-1,
        verbose=1
    )
    X, y = load_data(True, True)
    grid_search.fit(X,y)
    print(grid_search.best_estimator_)
    print(grid_search.best_score_)

if __name__=="__main__":
    # df = load_data()
    # print(df['len_description'].value_counts())
    # print(df.info())
    # print(df.head())

    # grid_search()

    X, y = load_data(True,True)
    print(X.info())
    print(y)






        # params = {
        # 'min_child_weight': [1, 5, 10],
        # 'gamma': [0.5, 1, 1.5, 2, 5],
        # 'subsample': [0.6, 0.8, 1.0],
        # 'colsample_bytree': [0.6, 0.8, 1.0],
        # 'max_depth': [3, 4, 5]
        # }