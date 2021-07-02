import pandas as pd
import numpy as np


def featurize_row(streaming_row):

    df = pd.DataFrame.from_dict(streaming_row, orient='index').T
    boolean_cols = ['has_header', 'has_analytics', 'has_logo']
    for col in boolean_cols:
        df[col].fillna(0, inplace=True)
    df['len_description'] = df['description']
    df['num_previous_payouts'] = df['previous_payouts'].apply(lambda x: len(x))
    df['has_org_desc'] = df['org_desc'].isnull() == False
    df['has_payee_name'] = df['payee_name'].isnull() == False
    df['user_created_to_event_start'] = df['event_start'] - df['user_created']




if __name__ == '__main__':
    pass
