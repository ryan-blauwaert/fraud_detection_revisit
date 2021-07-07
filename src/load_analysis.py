import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

def load_analysis(category='provider', drop_extras=True,  split_labels=True, scale=True, exclude=[]):
    if category=='provider':
        data = pd.read_csv('../data/analysis_csvs/email_provider.csv')
    elif category=='distinct_tld':
        data = pd.read_csv('../data/analysis_csvs/distinct_tld.csv')
    elif category=='combined_tld':
        data = pd.read_csv('../data/analysis_csvs/combined_tld.csv')
    else:
        data = pd.read_csv('../data/analysis_csvs/country.csv')



    data.drop(columns=['Unnamed: 0'],inplace=True)

    if exclude != []:
        for var in exclude:
            data = data[data['variable'] != var]

    if drop_extras:
        data = data[['variable', 'instances', 'percent_fraud']]
        if split_labels:
            labels = data[['variable']]
            X = data[['instances', 'percent_fraud']]
            if scale:
                MMS = MinMaxScaler()
                X = MMS.fit_transform(X)
            return X, labels


    return data




if __name__=="__main__":
    # data = load_and_drop(False)
    # result = country_analysis(data)
    # print(result.info())
    # print(result.head())
    # result.to_csv('../../data/analysis_csvs/country.csv')
    print()
    X, y = load_analysis(category='country')
    print(X)
    print(y)
    
