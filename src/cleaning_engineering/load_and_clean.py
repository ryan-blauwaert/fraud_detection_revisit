
import pandas as pd 
import numpy as np 
# from email_provider import create_email_provider_columns
# from top_level_domain import create_tld_columns
# from country_columns import create_country_columns
from dummies_by_criteria import dummies_bc

def load_and_drop(apply_dummies=True):
    data = pd.read_json('../../data/data.json')
    data.drop(columns=['approx_payout_date', 'gts', 'num_order', 'num_payouts', 'sale_duration2'], inplace=True)
    data['is_fraud'] = data['acct_type'].str.contains('fraud')
    for col in data.columns:
        data[col].loc[data[col]==''] = np.nan
    data.drop(columns='acct_type', inplace=True)

    data['email_provider'] = data['email_domain'].apply(lambda x: email_provider(x))
    data['distinct_top_level_domain'] = data['email_domain'].apply(lambda x: seperate_tld(x))
    data['combined_tld'] = data['email_domain'].apply(lambda x: combined_tld(x))
    data['country'].loc[pd.isnull(data['country'])] = 'NO_COUNTRY'
    data['matching_country_venue_country'] = data.apply(lambda x: matching_country_venue_country(x), axis=1)

    if apply_dummies:
        data = dummies_bc(data, category='provider', distinct_dummy_thresh=200, considered_min=5, lower_thresh=20, upper_thresh=80)
        data = dummies_bc(data, category='combined_tld', distinct_dummy_thresh=200, considered_min=5, lower_thresh=20, upper_thresh=80)
        data = dummies_bc(data, category='distinct_tld', distinct_dummy_thresh=200, considered_min=5, lower_thresh=20, upper_thresh=80)
        data = dummies_bc(data, category='country', distinct_dummy_thresh=200, considered_min=5, lower_thresh=20, upper_thresh=80)

        # data = create_country_columns(data)
    return data


def email_provider(x):
    url = None # variable to store the top level domain
    for idx, char in enumerate(x):
        if char =='.':
            url = x[:idx]
            break 
    return url.lower()
            
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

def matching_country_venue_country(x):
    co = x['country']
    vco = x['venue_country']
    if co == vco:
        return 1
    else:
        return 0

if __name__=="__main__":
    data = load_and_drop(True)
    data.to_csv('../../data/dummy_testing.csv')
    # vc = data['email_provider'].value_counts()
    # data



    #  0   body_length                     14337 non-null  float64
    #  1   channels                        14337 non-null  float64
    #  2   country                         13940 non-null  object 
    #  3   currency                        14337 non-null  object 
    #  4   delivery_method                 14321 non-null  float64
    #  5   description                     13508 non-null  object 
    #  6   email_domain                    14337 non-null  object 
    #  7   event_created                   14337 non-null  float64
    #  8   event_end                       14337 non-null  float64
    #  9   event_published                 14238 non-null  float64
    #  10  event_start                     14337 non-null  float64
    #  11  fb_published                    14337 non-null  float64
    #  12  has_analytics                   14337 non-null  float64
    #  13  has_header                      8928 non-null   float64
    #  14  has_logo                        14337 non-null  float64
    #  15  listed                          14337 non-null  object 
    #  16  name                            14252 non-null  object 
    #  17  name_length                     14337 non-null  float64
    #  18  object_id                       14337 non-null  float64
    #  19  org_desc                        8172 non-null   object 
    #  20  org_facebook                    14278 non-null  float64
    #  21  org_name                        12875 non-null  object 
    #  22  org_twitter                     14278 non-null  float64
    #  23  payee_name                      3177 non-null   object 
    #  24  payout_type                     13844 non-null  object 
    #  25  previous_payouts                14337 non-null  object 
    #  26  sale_duration                   14182 non-null  float64
    #  27  show_map                        14337 non-null  float64
    #  28  ticket_types                    14337 non-null  object 
    #  29  user_age                        14337 non-null  float64
    #  30  user_created                    14337 non-null  float64
    #  31  user_type                       14337 non-null  float64
    #  32  venue_address                   12166 non-null  object 
    #  33  venue_country                   12385 non-null  object 
    #  34  venue_latitude                  13261 non-null  float64
    #  35  venue_longitude                 13261 non-null  float64
    #  36  venue_name                      11280 non-null  object 
    #  37  venue_state                     10636 non-null  object 
    #  38  is_fraud                        14337 non-null  float64
    #  39  email_provider                  14337 non-null  object 
    #  40  gmail_email                     14337 non-null  int64  
    #  41  yahoo_email                     14337 non-null  int64  
    #  42  hotmail_email                   14337 non-null  int64  
    #  43  aol_email                       14337 non-null  int64  
    #  44  live_email                      14337 non-null  int64  
    #  45  me_email                        14337 non-null  int64  
    #  46  ymail_email                     14337 non-null  int64  
    #  47  comcast_email                   14337 non-null  int64  
    #  48  believed_safe_email             14337 non-null  int64  
    #  49  medium_risk_email               14337 non-null  int64  
    #  50  high_risk_email                 14337 non-null  int64  
    #  51  distinct_top_level_domain       14337 non-null  object 
    #  52  combined_tld                    14337 non-null  object 
    #  53  dot_com                         14337 non-null  int64  
    #  54  dot_org                         14337 non-null  int64  
    #  55  dot_uk                          14337 non-null  int64  
    #  56  dot_co                          14337 non-null  int64  
    #  57  dot_au                          14337 non-null  int64  
    #  58  dot_net                         14337 non-null  int64  
    #  59  dot_ca                          14337 non-null  int64  
    #  60  dot_edu                         14337 non-null  int64  
    #  61  safe_tld                        14337 non-null  int64  
    #  62  high_risk_tld                   14337 non-null  int64  
    #  63  US_country                      14337 non-null  int64  
    #  64  GB_country                      14337 non-null  int64  
    #  65  CA_country                      14337 non-null  int64  
    #  66  AU_country                      14337 non-null  int64  
    #  67  MA_country                      14337 non-null  int64  
    #  68  DE_country                      14337 non-null  int64  
    #  69  NZ_country                      14337 non-null  int64  
    #  70  No_country                      14337 non-null  int64  
    #  71  IE_country                      14337 non-null  int64  
    #  72  ES_country                      14337 non-null  int64  
    #  73  VN_country                      14337 non-null  int64  
    #  74  A1_country                      14337 non-null  int64  
    #  75  PK_country                      14337 non-null  int64  
    #  76  matching_country_venue_country  14337 non-null  int64 