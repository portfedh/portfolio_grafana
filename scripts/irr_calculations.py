import pandas as pd
from pyxirr import xirr


def irr_contributions_df(contributions_file1, contributions_file2):
    # Import data
    cont_cetes = pd.read_csv(contributions_file1)
    cont_GBM = pd.read_csv(contributions_file2)
    # Join dataframes
    result = pd.concat([cont_cetes, cont_GBM])
    # Substitute NA values with zeros
    result = result.fillna(0)
    # Add contributions of both accounts
    result['Tot_Contribuciones_MXN'] = (
        result['Contribuciones_Cetes_MXN'] + result['Contribuciones_GBM_MXN'])
    # Drop columns
    result.drop(
        ['Contribuciones_Cetes_MXN', 'Contribuciones_GBM_MXN'],
        axis=1, inplace=True)
    # Invert values from (+) to (-)
    result['Tot_Contribuciones_MXN'] = result['Tot_Contribuciones_MXN']*-1
    result['Tot_Contribuciones_MXN'] = result['Tot_Contribuciones_MXN'].astype('int')
    # Set 'Date' column as DateTime and set to index
    datetime_date = pd.to_datetime(result['Date'], dayfirst=True)
    datetime_index_trades = pd.DatetimeIndex(datetime_date.values)
    result = result.set_index(datetime_index_trades)
    result = result.rename_axis('Date', axis=1)
    result.drop('Date', axis=1, inplace=True)
    # Sort values by date in ascending order
    result.sort_index()
    # Return dataframe
    return result


def irr_monthly_balance_df(balance_df, balance_df2):
    # Merge two files
    balance_df = balance_df.merge(
        balance_df2, left_index=True, right_index=True)
    # Sum columns
    balance_df['Tot_Acct_Portafolio_MXN'] = (
        balance_df[balance_df.columns[0]] + balance_df[balance_df.columns[1]])
    # Save as Integer
    balance_df['Tot_Acct_Portafolio_MXN'] = balance_df['Tot_Acct_Portafolio_MXN'].astype('int')
    # Drop individual columns
    balance_df.drop(['Tot_Acct_Cetes_MXN', 'Tot_Acct_GBM_MXN'], axis=1, inplace=True)
    # Return dataframe
    return balance_df


def calculate_xirr(balance_df, balance_df2):
    # Get last value
    last = balance_df.copy(deep=True)
    last = last.iloc[-1:]
    # Rename column to match other DF
    last.rename(columns={'Tot_Acct_Portafolio_MXN': 'Tot_Contribuciones_MXN'}, inplace=True)
    # Concatenate dataframes
    irr_df = pd.concat([balance_df2, last])
    pdToList = irr_df.index.tolist()
    pdToList2 = list(irr_df['Tot_Contribuciones_MXN'])
    result = xirr(pdToList, pdToList2)
    return result
