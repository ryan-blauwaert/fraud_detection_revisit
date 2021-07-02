import numpy as np
import pandas as pd
from collections import Counter


def create_tld_columns(df):
    df['distinct_top_level_domain'] = df['email_domain'].apply(lambda x: seperate_tld(x))

    df['combined_tld'] = df['email_domain'].apply(lambda x: combined_tld(x))

    df['dot_com'] = df['distinct_top_level_domain'].apply(lambda x: dot_com(x))

    df['dot_org'] = df['distinct_top_level_domain'].apply(lambda x: dot_org(x))

    df['dot_uk'] = df['distinct_top_level_domain'].apply(lambda x: dot_uk(x))

    df['dot_co'] = df['distinct_top_level_domain'].apply(lambda x: dot_co(x))

    df['dot_au'] = df['distinct_top_level_domain'].apply(lambda x: dot_au(x))

    df['dot_net'] = df['distinct_top_level_domain'].apply(lambda x: dot_net(x))

    df['dot_ca'] = df['distinct_top_level_domain'].apply(lambda x: dot_ca(x))

    df['dot_edu'] = df['distinct_top_level_domain'].apply(lambda x: dot_edu(x))

    df['safe_tld'] = df['distinct_top_level_domain'].apply(lambda x: safe_tld(x))

    df['high_risk_tld'] = df['distinct_top_level_domain'].apply(lambda x: high_risk_tld(x))


    return df 



################################################3
def seperate_tld(x): # creates column that contains list of all the tld's for each row's email address
    tld_lst = []
    email = x.split('.')
    for elem in email[1:]:
        tld_lst.append(elem.lower())
    return tld_lst

def combined_tld(x):
    for idx, char in enumerate(x):
        if char == '.':
            return x[idx+1:].lower()

def dot_com(x):
    if 'com' in x:
        return 1
    else:
        return 0

def dot_org(x):
    if 'org' in x:
        return 1
    else:
        return 0


def dot_uk(x):
    if 'uk' in x:
        return 1
    else:
        return 0

def dot_co(x):
    if 'co' in x:
        return 1
    else:
        return 0

def dot_au(x):
    if 'au' in x:
        return 1
    else:
        return 0

def dot_net(x):
    if 'net' in x:
        return 1
    else:
        return 0

def dot_ca(x):
    if 'ca' in x:
        return 1
    else:
        return 0

def dot_edu(x):
    if 'edu' in x:
        return 1
    else:
        return 0

def safe_tld(x):
    result = 0
    safe_lst = ['on', 'cnc', 'ly', 'ie', 'coop', 'nl', 'gov', 'nz', 'ac', 'us']
    for elem in x:
        if elem in safe_lst:
            result = 1
            break 
    return result 

def high_risk_tld(x):
    result = 0
    high_risk_lst = ['fr', 'vn']

    for elem in x:
        if elem in high_risk_lst:
            result = 1
            break
    return result 

