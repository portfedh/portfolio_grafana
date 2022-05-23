from scripts import irr_calculations as irr

# Create Consolidated Contributions File
########################################
cont_file = irr.irr_contributions_df(
    'inputs/contributions_CLG_CETES.csv',
    'inputs/contributions_CLG_GBM.csv')
cont_file.to_csv("outputs/irr_contributions_CLG_AllAccounts.csv",
                 index=True, index_label='Date')

# Create Consolidated Monthly Account Balance
#############################################
