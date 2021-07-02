import numpy as np
import pandas as pd


def create_email_provider_columns(df):
    df['email_provider'] = df['email_domain'].apply(lambda x: email_provider(x))

    df['gmail_email'] = df['email_provider'].apply(lambda x: gmail_email(x))

    df['yahoo_email'] = df['email_provider'].apply(lambda x: yahoo_email(x))

    df['hotmail_email'] = df['email_provider'].apply(lambda x: hotmail_email(x))

    df['aol_email'] = df['email_provider'].apply(lambda x: aol_email(x))

    df['live_email'] = df['email_provider'].apply(lambda x: live_email(x))

    df['me_email'] = df['email_provider'].apply(lambda x: me_email(x))

    df['ymail_email'] = df['email_provider'].apply(lambda x: ymail_email(x))

    df['comcast_email'] = df['email_provider'].apply(lambda x: comcast_email(x))

    df['believed_safe_email'] = df['email_provider'].apply(lambda x: believed_safe_email(x))

    df['medium_risk_email'] = df['email_provider'].apply(lambda x: medium_risk(x))

    df['high_risk_email'] = df['email_provider'].apply(lambda x: high_risk(x))


    return df 



def email_provider(x):
    url = None # variable to store the top level domain
    for idx, char in enumerate(x):
        if char =='.':
            url = x[:idx]
            break 
    return url.lower()
            
####################################################################3


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


def live_email(x):
    if x == 'live':
        return 1
    else:
        return 0

def me_email(x):
    if x == 'me':
        return 1
    else:
        return 0

def ymail_email(x):
    if x == 'ymail':
        return 1
    else:
        return 0

def comcast_email(x):
    if x == 'comcast':
        return 1
    else:
        return 0


def believed_safe_email(x):
    if x in ['generalassemb',
                'kineticevents',
                'improvboston',
                'sippingnpainting',
                'claytonislandtours',
                'racetonowhere',
                'greatworldadventures',
                'shaw',
                'sbcglobal',
                'mac',
                'guardian',
                'joonbug',
                'jhilburn',
                'busboysandpoets',
                'doctor',
                'dsicomedy',
                'o-cinema',
                'senecalakewine',
                'themagnetictheatre',
                'womenlikeus',
                'wholefoods',
                'verizon',
                'webookbands',
                'jumpnasiumparty',
                'pricecutteronline',
                'discodonniepresents',
                'tribecafilmfestival',
                'americanphotosafari']:
        return 1
    else:
        return 0

def high_risk(x):
    if x in ['lidf',
            'rocketmail',
            'ultimatewine',
            'diversity-church',
            'yopmail',
            'mohmal',
            'thinktankconsultancy',
            'maroclancers',
            'inbox',
            'execs',
            'ashfordradtech',
            'consultant',
            '9and1']:
        return 1
    else:
        return 0 

def medium_risk(x):
    if x in ['outlook', 'mail', 'cox', 'att', 'cs', 'post', 'gmx']:
        return 1
    else:
        return 0 

