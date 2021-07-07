import pandas as pd 

def load_data(drop_sam_cols = True, X_y = False):
    df = pd.read_csv('../data/data_columns_added.csv')
    df = df[['body_length', 
             'channels', 
             'country',
             'currency',
             'email_provider',
             'distinct_top_level_domain',
             'combined_tld',
             'matching_country_venue_country',
             'fb_published', 
             'has_analytics', 
             'has_header', 
             'has_logo', 
             'name_length', 
             'sale_duration', 
             'user_age', 
             'user_type', 
             'len_description', 
             'num_previous_payouts', 
             'has_org_desc', 
             'user_created_to_event_start', 
             'has_payee_name', 
             'is_fraud']]
    if drop_sam_cols:
        df.drop(columns=['currency', 'email_provider', 'distinct_top_level_domain', 'combined_tld','country'], inplace=True)
    if X_y:
        y = df['is_fraud']
        X = df.drop(columns='is_fraud')
        return X, y 
    return df



if __name__=="__main__":   
    # df = pd.read_csv('../data/data_columns_added.csv')
    # df = df[['body_length', 
    #          'channels', 
    #          'country',
    #          'currency',
    #          'email_provider',
    #          'distinct_top_level_domain',
    #          'combined_tld',
    #          'matching_country_venue_country',
    #          'fb_published', 
    #          'has_analytics', 
    #          'has_header', 
    #          'has_logo', 
    #          'name_length', 
    #          'sale_duration', 
    #          'user_age', 
    #          'user_type', 
    #          'len_description', 
    #          'num_previous_payouts', 
    #          'has_org_desc', 
    #          'user_created_to_event_start', 
    #          'has_payee_name', 
    #          'is_fraud']]
    # print(df.info())
    # print(df.head())
    X, y = load_data(True, True)
    print(X.head())
    print(X.info())