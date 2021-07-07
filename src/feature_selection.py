import pandas as pd 
import numpy as np 
from xgboost import XGBClassifier
from load_data import load_data
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, brier_score_loss
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt 
from itertools import combinations 


def feature_importances(model, X, y):
    model.fit(X,y)
    result = {}
    for col, importance in zip(X.columns, model.feature_importances_):
        print(f'{col}: {importance}')
        print('\n')


def column_combinations(base_list, considered_columns, r=[1]): # all possible combinations of columns (that we are considering)
    """Creates a list of lists. list contain combinations of column names

    Args:
        base_list (list): columns to always be included
        considered_columns (list): columns to be fluctuated through
        r (list, optional): Number of column combinations. see itertools documentation. it is 'r' in the combinations function. Defaults to [1].

    Returns:
        list of lists: columns to be tested 
    """    
    column_list = []
    column_list.append(base_list)

    for num in r: # gets column combination of sizes included in list 'r'
        subset = list(combinations(considered_columns, num))
        for cols in subset:
            temp = base_list.copy() 
            for col in cols: # adds columns from each considered column combination to copy of base_list
                temp.append(col)
            column_list.append(temp) # adds copy + combination to column_list

    return column_list


def cv(model, X, y, folds=10):
    skf = StratifiedKFold(n_splits=folds, shuffle = True)
    roc = []
    brier = []
    f1 = []
    for train, test in skf.split(X,y):
        model.fit(X.iloc[train], y.iloc[train])
        pred = model.predict(X.iloc[test])
        roc.append(roc_auc_score(y.iloc[test], pred))
        brier.append(brier_score_loss(y.iloc[test], pred))
        f1.append(f1_score(y.iloc[test], pred))
    return np.mean(roc), np.mean(brier), np.mean(f1)


def test_combinations(model, X, y, base_list, considered_columns, r=[1], folds=10):


    result = pd.DataFrame(columns=['columns', 'brier', 'roc_auc', 'f1']) 

    col_lst = column_combinations(base_list, considered_columns, r)

    count = 0

    for idx, cols in enumerate(col_lst): # iterate through column list
        X_subset = X[cols] # reduces X to just columns that ought to be considered
        X_cols = list(X_subset.columns)


        roc_auc, brier, f1 = cv(model, X_subset, y) # get scores using cv function

        for col in base_list: # removes columns from base list from X_cols to remove extra info from DataFrame
            X_cols.remove(col)  


        result.loc[idx] = [X_cols, brier, roc_auc, f1] #inserting results into DataFrame


    return result 


if __name__=="__main__":
    # body_length: 0.02472328580915928
    # channels: 0.02499024197459221
    # matching_country_venue_country: 0.02851231023669243
    # fb_published: 0.031903840601444244
    # has_analytics: 0.022629790008068085
    # has_header: 0.0494292713701725
    # has_logo: 0.040364790707826614
    # name_length: 0.029961103573441505
    # sale_duration: 0.061685942113399506
    # user_age: 0.04255932196974754
    # user_type: 0.06566121429204941
    # len_description: 0.02511097677052021
    # num_previous_payouts: 0.3263902962207794
    # has_org_desc: 0.022295625880360603
    # user_created_to_event_start: 0.11174279451370239
    # has_payee_name: 0.09203917533159256

    X, y = load_data(True,True)

    xgb = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                colsample_bynode=1, colsample_bytree=0.6, eval_metric='logloss',
                gamma=0.5, gpu_id=-1, importance_type='gain',
                interaction_constraints='', learning_rate=0.1, max_delta_step=0,
                max_depth=8, min_child_weight=1, missing=None,
                monotone_constraints='()', n_estimators=140, n_jobs=4, nthread=4,
                num_parallel_tree=1, random_state=0, reg_alpha=0.01, reg_lambda=1,
                scale_pos_weight=1, subsample=0.8, tree_method='exact',
                validate_parameters=1, verbosity=None)


    # print(feature_importances(xgb, X, y))
    base_list = ['user_type', 
                 'num_previous_payouts', 
                 'user_created_to_event_start', 
                 'has_payee_name',
                 'channels',
                 'has_header', 
                 'has_logo', 
                 'name_length', 
                 'sale_duration', 
                 'user_age']
    considered_list = ['body_length', 
                       'matching_country_venue_country', 
                       'fb_published', 
                       'has_analytics', 
                       'len_description', # should most likely be removed (above could probably be removed as well)
                       'has_org_desc'] # should most likely be removed

    for col in base_list:
        if col in X.columns:
            print(col)
    result = test_combinations(xgb, X, y, base_list, considered_list, r=[1,2,3,4,5,6])
    print(result.head())
    result.to_csv('../data/feature_selection.csv')