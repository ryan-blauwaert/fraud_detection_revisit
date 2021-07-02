import pandas as pd 
import numpy as np 
from collections import Counter


def email_provider_analysis(data):
    email_providers = list(data['email_provider'].unique())
    result = pd.DataFrame(columns=['variable', 'instances', 'pos_instances', 'neg_instances', 'percent_fraud'], index=list(range(len(email_providers))))
    for idx, email in enumerate(email_providers):
        subset = data[data['email_provider']==email]
        result.iloc[idx] = [email, len(subset), subset['is_fraud'].sum(), len(subset) - subset['is_fraud'].sum(), 100 * subset['is_fraud'].sum() / len(subset)]
    return result

def combined_tld_analysis(data):
    tld_lst = list(data['combined_tld'].unique())
    result = pd.DataFrame(columns=['variable', 'instances', 'pos_instances', 'neg_instances', 'percent_fraud'], index=list(range(len(tld_lst))))
    for idx, tld in enumerate(tld_lst):
        subset = data[data['combined_tld']==tld]
        result.iloc[idx] = [tld, len(subset), subset['is_fraud'].sum(), len(subset) - subset['is_fraud'].sum(), 100 * subset['is_fraud'].sum() / len(subset)]
    return result

def distinct_tld_analysis(data):
    instances = {}
    for idx, row in data.iterrows():
        if row['is_fraud'] == 1:
            char = 'P'
        else:
            char = 'N'
        for tld in row['distinct_top_level_domain']:
            if tld in instances:
                instances[tld] += char
            else:
                instances[tld] = char
                
    result = pd.DataFrame(columns=['variable', 'instances', 'pos_instances', 'neg_instances', 'percent_fraud'], index=list(range(len(instances))))
    for idx, (key, val) in enumerate(instances.items()):
        pos = Counter(val)['P']
        neg = Counter(val)['N']
        result.iloc[idx] = [key, pos + neg, pos, neg, 100 * pos / (pos+neg)]
    return result 
    
def country_analysis(data):
    countries = data['country'].unique()
    result = pd.DataFrame(columns=['variable', 'instances', 'pos_instances', 'neg_instances', 'percent_fraud'], index=list(range(len(countries))))
    for idx, country in enumerate(countries):
        subset = data[data['country']==country]
        result.iloc[idx] = [country, len(subset), subset['is_fraud'].sum(), len(subset) - subset['is_fraud'].sum(), 100 * subset['is_fraud'].sum() / len(subset)]
    return result 

if __name__=="__main__":
    # print(country_analysis(data).sort_values('instances'))
    pass 