from load_data import load_data
from load_analysis import load_analysis
from sklearn.cluster import KMeans
from collections import defaultdict
from feature_selection import cv 
from xgboost import XGBClassifier
import pandas as pd 

def create_cluster_dummies(model, X, y, stop, analysis_type='provider'):
    if analysis_type == 'provider':
        apply_col = 'email_provider'
    elif analysis_type == 'distinct_tld':
        apply_col = 'distinct_top_level_domain'
    elif analysis_type == 'combined_tld':
        apply_col = 'combined_tld'
    elif analysis_type == 'country':
        apply_col = 'country'

    analysis_matrix, labels = load_analysis(category=analysis_type)

    result = pd.DataFrame(columns=['K', 'roc', 'brier', 'f1'], index = list(range(stop-1)))

    for idx, num in enumerate(range(2, stop+1)):
        print(num)
        X, y = prep_primary_data(analysis_type=analysis_type)
        km = KMeans(num)
        km.fit(analysis_matrix)
        dic = defaultdict(list)
        for cluster, label in zip(km.labels_, labels.values):
            dic[cluster].append(label[0])
        for clstr_grp in range(len(dic)):
            if analysis_type == 'distinct_tld':
                X[f'{analysis_type}_clstr_{clstr_grp}'] = X[apply_col].apply(lambda x: distinct_tld_apply(x, dic[clstr_grp]))
            else:
                X[f'{apply_col}_clstr_{clstr_grp}'] = X[apply_col].apply(lambda x: 1 if x in dic[clstr_grp] else 0)
        X.drop(columns=apply_col,inplace=True)
        roc, brier, f1 = cv(model,X,y)
        result.iloc[idx] = [num, roc, brier, f1]
    return result 


def distinct_tld_apply(x, lst):
    for tld in x:
        if tld in lst:
            return 1
    return 0 

def prep_primary_data(analysis_type = 'provider'):
    X, y = load_data(False, True)
    X.drop(columns=['currency','len_description', 'has_org_desc'], inplace=True)
    if analysis_type == 'provider':
        X.drop(columns=['distinct_top_level_domain', 'combined_tld','country'], inplace=True)
    elif analysis_type == 'distinct_tld':
        X.drop(columns=['combined_tld', 'email_provider', 'country'], inplace=True)
    elif analysis_type == 'combined_tld':
        X.drop(columns=['distinct_top_level_domain', 'email_provider', 'country'], inplace=True)
    elif analysis_type == 'country':
        X.drop(columns=['distinct_top_level_domain', 'email_provider', 'combined_tld'], inplace=True)
    
    return X, y 



if __name__=="__main__":
    xgb = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                colsample_bynode=1, colsample_bytree=0.6, eval_metric='logloss',
                gamma=0.5, gpu_id=-1, importance_type='gain',
                interaction_constraints='', learning_rate=0.1, max_delta_step=0,
                max_depth=8, min_child_weight=1, missing=None,
                monotone_constraints='()', n_estimators=140, n_jobs=4, nthread=4,
                num_parallel_tree=1, random_state=0, reg_alpha=0.01, reg_lambda=1,
                scale_pos_weight=1, subsample=0.8, tree_method='exact',
                validate_parameters=1, verbosity=None)

    X, y = prep_primary_data('distinct_tld')
    # print(X.info())
    # provider, provider_labels = load_analysis(category='provider')

    # km = KMeans(5)
    # km.fit(provider)
    # dic = defaultdict(list)
    # for cluster, label in zip(km.labels_, provider_labels.values):
    #     dic[cluster].append(label[0])
    # for clstr_grp in range(len(dic)):
    #     X[f'provider_clstr_{clstr_grp}'] = X['email_provider'].apply(lambda x: 1 if x in dic[clstr_grp] else 0)
    # X.drop(columns='email_provider', inplace=True)
    # print(cv(xgb, X, y))

    result = create_cluster_dummies(xgb, X, y, 40, 'distinct_tld')
    print(result.head())
    result.to_csv('../data/cluster_csvs/distinct_tld_cluster_results.csv')
    # for num in range(2, 5+1):
    #     print(num)
    # print(list(range(2,5+1)))