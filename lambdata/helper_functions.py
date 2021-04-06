def null_count(df):
    """Counts and adds the nulls in a dataframe df"""
    null_sum = df.isna().sum().sum()
    return null_sum

def split_dates(date_series):
    """Takes a series of date of format MM/DD/YYYY into multiple columns, dataframe(df['MM'],df['DD'],df['YYYY'])"""
    df = pd.DataFrame({'date' : date_series})

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['year'] = df['date'].dt.year

    df.drop('date', axis = 1, inplace = True)

    return df
