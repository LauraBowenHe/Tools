### This script records some useful pandas skills I have met or used, record and share :)
### This will update constantly

#---------------- handle with nan in column --------------------------------
### replace outlier value as nan
df[col].replace(365243, np.nan, inplace= True)

### drop column with nan appear greater than 60%
feats_test_drop = []
for col in df.columns:
    if df[col].isnull().sum() * 1. / df[col].shape[0] > 0.6:
        feats_test_drop.append(col)
df = df.drop(feats_test_drop, axis=1)

### fill nan with mode in a column
print("fill missing data with mode...")
for col in df.columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
 
#---------------- check zero variance variable --------------------------------
### zero variance variable is imprevious to tree models, but not to linear models
feats_var_zero = []
df_var = df.var(axis=0)
for col in df.columns:
    if df_var[col] > 0:
        feats_var_zero.append(col)
df.drop(feats_var_zero, axis=1)

#---------------------- lambda function ---------------------------------------
df['z_dist'] = df.apply(lambda x:Levenshtein.ratio(x['question1'], x['question2']), axis=1)

#------------------- get random samples from dataframe ------------------------
### frac specifys the fraction of rows to return in the random sample
df.sample(frac=1)

#------------------- parquet for faster save than csv  ------------------------
### (pip install pyarrow)
df = pd.read_parquet('../data/spn_nlp_feats.parquet.gzip', engine='pyarrow')

#------------------- modify column by certain condition -----------------------
df.loc[((df[col]==1) & (df[col1]==1)), 'prob'] = 1


