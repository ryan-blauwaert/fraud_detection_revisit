import pandas as pd 
import numpy as np 
from email_country_analysis import country_analysis, distinct_tld_analysis, combined_tld_analysis, email_provider_analysis
from load_and_clean import load_and_drop
# from email_provider import email_provider
# from top_level_domain import combined_tld, seperate_tld

# def load_df():
#     df = load_and_drop(False)
#     df['email_provider'] = df['email_domain'].apply(lambda x: email_provider(x))
#     df['distinct_top_level_domain'] = df['email_domain'].apply(lambda x: seperate_tld(x))
#     df['combined_tld'] = df['email_domain'].apply(lambda x: combined_tld(x))
#     df['country'].loc[pd.isnull(df['country'])] = 'NO_COUNTRY'
#     return df

def dummies_bc(df, category = 'provider', distinct_dummy_thresh = 1000, low_considered_min=15, med_considered_min=10,  high_considered_min=5, lower_thresh=25, upper_thresh=75):
    if category == 'provider':
        result = email_provider_analysis(df)
        starting_str = 'email_provider'
        apply_col = 'email_provider'
    elif category == 'combined_tld':
        result = combined_tld_analysis(df)
        starting_str = 'combined_tld'
        apply_col = 'combined_tld'

    elif category == 'distinct_tld':
        result = distinct_tld_analysis(df)
        starting_str = 'distinct_tld'
        apply_col = 'distinct_top_level_domain'

    elif category == 'country':
        result = country_analysis(df)
        starting_str = 'country'
        apply_col = 'country'

    
    distinct_dummies = list(result[result['instances'] >= distinct_dummy_thresh]['variable'].unique())
    result = result[result['instances'] < distinct_dummy_thresh]
    for var in distinct_dummies:
        
        dummy_col = f'{starting_str}_{var}'
        if category == 'distinct_tld':
            df[dummy_col] = df[apply_col].apply(lambda x: 1 if var in x else 0)
        else:
            df[dummy_col] = df[apply_col].apply(lambda x: 1 if var == x else 0)
    
    # grouped_dummies = list(result[result['instances'] >= considered_min]['variable'].unique())

    low_risk = []
    medium_risk = []
    high_risk = []
    for idx, row in result.iterrows():
            if row['percent_fraud'] <= lower_thresh and row['instances'] >= low_considered_min:
                low_risk.append(row['variable'])
            elif row['percent_fraud'] <= upper_thresh and row['instances'] >= med_considered_min:
                medium_risk.append(row['variable'])
            elif row['percent_fraud'] > upper_thresh and row['instances'] >= high_considered_min:
                high_risk.append(row['variable'])
            else:
                continue 

    risk_lsts = [low_risk, medium_risk, high_risk]
    dummy_cols = [f'{starting_str}_low_risk', f'{starting_str}_medium_risk', f'{starting_str}_high_risk']
    for (risk_lst, dummy_col) in zip(risk_lsts, dummy_cols):
        if category == 'distinct_tld':
            df[dummy_col] = df[apply_col].apply(lambda tlds: distinct_tld_apply(tlds, risk_lst))
        else:
            df[dummy_col] = df[apply_col].apply(lambda x: 1 if x in risk_lst else 0)
    return df

    
                    





        
def distinct_tld_apply(tlds, risk_lst):
    for tld in tlds:
        if tld in risk_lst:
            return 1
        else:
            continue
    return 0 




    


if __name__=="__main__":
    df = load_and_drop(False)
    df = dummies_bc(df, category='distinct_tld', distinct_dummy_thresh = 300)

    print(df.info())