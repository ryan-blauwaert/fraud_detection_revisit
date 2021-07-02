import pandas as pd 
import numpy as np 

def apply_column_engineering(data):
    data['email_provider'] = data['email_domain'].apply(lambda x: email_provider(x))
    data['distinct_top_level_domain'] = data['email_domain'].apply(lambda x: seperate_tld(x))
    data['country'].loc[pd.isnull(data['country'])] = 'NO_COUNTRY'
    data['matching_country_venue_country'] = data.apply(lambda x: matching_country_venue_country(x), axis=1)
    data['provider_gmail'] = data['email_provider'].apply(lambda x: gmail_email(x))
    data['provider_yahoo'] = data['email_provider'].apply(lambda x: yahoo_email(x))
    data['provider_hotmail'] = data['email_provider'].apply(lambda x: hotmail_email(x))
    data['provider_aol'] = data['email_provider'].apply(lambda x: aol_email(x))
    data['tld_com'] = data['distinct_top_level_domain'].apply(lambda x: dot_com(x))
    data['tld_org'] = data['distinct_top_level_domain'].apply(lambda x: dot_org(x))
    data['tld_uk'] = data['distinct_top_level_domain'].apply(lambda x: dot_uk(x))
    data['tld_co'] = data['distinct_top_level_domain'].apply(lambda x: dot_co(x))
    data['tld_au'] = data['distinct_top_level_domain'].apply(lambda x: dot_au(x))
    data['tld_net'] = data['distinct_top_level_domain'].apply(lambda x: dot_net(x))
    data['tld_ca'] = data['distinct_top_level_domain'].apply(lambda x: dot_ca(x))
    data['tld_edu'] = data['distinct_top_level_domain'].apply(lambda x: dot_edu(x))
    data['country_US'] = data['country'].apply(lambda x: US_or_not(x))
    data['country_GB'] = data['country'].apply(lambda x: GB_or_not(x))
    data['country_CA'] = data['country'].apply(lambda x: CA_or_not(x))
    data['country_AU'] = data['country'].apply(lambda x: AU_or_not(x))
    data['country_NONE'] = data['country'].apply(lambda x: null_country(x))
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

def gmail_email(x):
    if x == 'gmail':
        return 1
    else:
        return 0

def yahoo_email(x):
    if x == 'yahoo':
        return 1
    else:
        return 0

def hotmail_email(x):
    if x == 'hotmail':
        return 1
    else:
        return 0

def aol_email(x):
    if x == 'aol':
        return 1
    else:
        return 0

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

def null_country(x):
    if x == 'NO_COUNTRY':
        return 1
    else:
        return 0

if __name__=="__main__":
    pass