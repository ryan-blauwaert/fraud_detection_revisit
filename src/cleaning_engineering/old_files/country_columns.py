import numpy as np
import pandas as pd



def create_country_columns(df):


    df['US_country'] = df['country'].apply(lambda x: US_or_not(x))

    df['GB_country'] = df['country'].apply(lambda x: GB_or_not(x))

    df['CA_country'] = df['country'].apply(lambda x: CA_or_not(x))

    df['AU_country'] = df['country'].apply(lambda x: AU_or_not(x))

    df['MA_country'] = df['country'].apply(lambda x: MA_or_not(x))

    df['DE_country'] = df['country'].apply(lambda x: DE_or_not(x))

    df['NZ_country'] = df['country'].apply(lambda x: NZ_or_not(x))

    df['No_country'] = df['country'].apply(lambda x: None_or_not(x))

    df['IE_country'] = df['country'].apply(lambda x: IE_or_not(x))

    df['ES_country'] = df['country'].apply(lambda x: ES_or_not(x))

    df['VN_country'] = df['country'].apply(lambda x: VN_or_not(x))

    df['A1_country'] = df['country'].apply(lambda x: A1_or_not(x))

    df['PK_country'] = df['country'].apply(lambda x: PK_or_not(x))

    df['matching_country_venue_country'] = df.apply(lambda x: matching_country_venue_country(x), axis=1)

    return df 

    
##################################################




def US_or_not(x): # 1 for us 0 for not us
    if x == 'US':
        return 1
    else:
        return 0

def GB_or_not(x): 
    if x == 'GB':
        return 1
    else:
        return 0

def CA_or_not(x): 
    if x == 'CA':
        return 1
    else:
        return 0

def AU_or_not(x):
    if x == 'AU':
        return 1
    else:
        return 0

def MA_or_not(x): 
    if x == 'MA':
        return 1
    else:
        return 0

def DE_or_not(x):
    if x == 'DE':
        return 1
    else:
        return 0

def NZ_or_not(x): 
    if x == 'NZ':
        return 1
    else:
        return 0

def None_or_not(x):
    if pd.isnull(x):
        return 1
    else:
        return 0


def IE_or_not(x): 
    if x == 'IE':
        return 1
    else:
        return 0

def ES_or_not(x): 
    if x == 'ES':
        return 1
    else:
        return 0

def VN_or_not(x): 
    if x == 'VN':
        return 1
    else:
        return 0

def A1_or_not(x): 
    if x == 'A1':
        return 1
    else:
        return 0

def PK_or_not(x): 
    if x == 'PK':
        return 1
    else:
        return 0

def matching_country_venue_country(x):
    co = x['country']
    vco = x['venue_country']
    if co == vco:
        return 1
    else:
        return 0