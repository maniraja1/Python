import pandas as pd

"""
When making a copy of a dataframe always remember to copy 
"""


"""
Canoncialize a dataset
"""
def canonicalize_tibble(X):
    var_names = sorted(X.columns)
    Y = X[var_names].copy()
    Y.sort_values(by=var_names, inplace=True)
    Y.reset_index(drop=True, inplace=True)
    return Y


"""
Compare tibbles
"""
def tibbles_are_equivalent (A, B):
    A_canonical = canonicalize_tibble(A)
    B_canonical = canonicalize_tibble(B)
    equal = (A_canonical == B_canonical)
    return equal.all().all()

# Data frame from file
movies = pd.read_table(get_data_path('movie-name-score.txt'), sep=',', header=None, names=['id', 'name', 'score'])
cast = pd.read_table(get_data_path('movie-cast.txt'), sep=',', header=None, names=['movie_id', 'cast_id', 'cast_name'])


# Create a data frame from aggregation
temp = pd.DataFrame(cast.groupby(['movie_id']).size())
good_teamwork = good_teamwork.groupby(['cast_name_x', 'cast_name_y']).agg({'movie_id': 'size', 'score': 'mean'}).reset_index()


#Group and having
single_cast = pd.DataFrame(cast.groupby('cast_id').size().loc[lambda x: x==1].sort_values())

#group by with where clause
df_hb = round(df_analysis[df_analysis['hba1c_change']!=0].groupby('treatment_type')['hba1c_change'].mean(),4)

# Rename single column
temp.rename(columns = {0: "cast_count"},
          inplace = True)
solution_df.columns = ["Sender", "Receiver","Frequency"]

# Join Example
cast_size = pd.merge(movies[['id','name']], temp, left_on='id', right_on='movie_id', how='inner').drop('id',1).sort_values('cast_count', ascending=False)
cast_score=pd.DataFrame(pd.merge(movies[['id','score']],cast[['movie_id','cast_name']],left_on='id', right_on='movie_id').drop(['id','movie_id'],1).groupby('cast_name',as_index=False).mean().round(2))

#Reset Index
cast_size.reset_index(drop=True, inplace=True)

#Filter
one_hit_wonders = one_hit_wonders[one_hit_wonders['score']==100]
good_teamwork=good_teamwork.query('score>25')
temp[['home_team','points']].loc[temp['winner'] == 'Draw']

#multiple condition
temp = winners_df.loc[(winners_df['tournament'] == 'FIFA World Cup') & (winners_df['year'] == 1998)]

#Filter contains and case insensitive
Network_sub=Network.loc[Network['Entity B'].str.contains('trump',case=False)]

#filter exact match case insensitive
display(Network.loc[Network['Entity B'].str.upper()=='IVANKA TRUMP'])

#filter based on values in a list
Network_strong=Network_sub.loc[(Network_sub['Entity A'].isin(x))&(Network_sub['Entity B Type']=='Organization')]


#SQL Query
disk_engine=''
query = '''select a.cast_name as cast_member_1, b.cast_name as cast_member_2, count(*) as num_movies, round(avg(score), 2) as avg_score
           from cast a inner join cast b on (a.movie_id = b.movie_id and a.cast_name < b.cast_name) 
           inner join movies c on b.movie_id = c.id
           group by a.cast_name, b.cast_name
           having num_movies >=3 and avg_score >=50
           order by cast_member_1, cast_member_2
        '''
good_teamwork2 = pd.read_sql_query(query, disk_engine)

conn = db.connect('file:' + get_path('ca-roads/network.db') + '?mode=ro', uri=True)
pd.read_sql_query("SELECT * FROM Intersections LIMIT 7", conn)

#Adding a new columns
game_df['winner']='Draw'
game_df.loc[game_df['home_score']>game_df['away_score'], 'winner']=game_df['home_team']
game_df.loc[game_df['home_score']<game_df['away_score'], 'winner']=game_df['away_team']

#deleting rows based on condition
temp.drop(temp[temp['home_winner'] < 50].index, inplace = True)

#delete rows after first 5 rows
temp = temp.iloc[:5]

#Convert string to date
winners_df['year'] = pd.DataFrame(pd.DatetimeIndex(winners_df['date'].astype('datetime64[ns]')).year)
display(pd.DataFrame(pd.DatetimeIndex(winners_df['date'].astype('datetime64[ns]'))))
df0['Timestamp'] = pd.to_datetime(df0['Last Update'])

#update column based on condition
winners_df['home_winner']=0
winners_df.loc[winners_df['winner']==winners_df['home_team'], 'home_winner']=1
data_clean['year'] = pd.DatetimeIndex(data_clean['onsale_dt']).year

# union
temp5=pd.concat([temp2, temp3, temp4])

#pandas create a dict
for i,j in temp.iterrows():
        x[j['Entity A']].update({j['Entity B']:j['Connection_Strength']})


# To get a single cell
ATL_ID=airport_codes[airport_codes['Description'].str.contains("Hartsfield")]
ATL_ID=ATL_ID.iloc[0,0]


#Add index as a column
origin_indices['ORIGIN_INDEX'] = airport_codes.index

#Max value in a column
column = df["col2"].max()

#rows in series
temp=segments['ORIGIN_INDEX'].unique()
print(len(temp))

#rows in a data frame
x=len(airport_codes.index)

#Pandas standardize dates
df['year1']=pd.to_datetime(df['yearID'], errors='coerce')

#Pandas round column to the nearest 10
select_col = [x for x in df2.columns if x not in ['playerID','yearID']]
df2[select_col] = df2[select_col].round(-1).astype(int)

#Pandas get all columns with number
x=df.select_dtypes(np.number)

#Pandas build aggregate dict
x=df.select_dtypes(np.number)
for i in x:
    n[i]='min'

# FInd rows with isna
data.isna().sum()

#copy data frame first row only (deep copy)
data_copy = data[0:1].copy()

data = data[1:]
print (data.shape)

#Drop columns
data.drop([cola,colb], axis=1, inplace=True)

#Select some columns, based on regex filter on  column name
# You can also do the same search by rows index by passing axis=0
x=data.filter(regex='_Part_')
DataFrame.filter(self, items=None, like=None, regex=None, axis=None)


#drop na

#Drop na single columns
df.dropna(subset=['colname'])
df = df[df['EPS'].notna()]

#Create dataframe from list
#Method1
lst = [['tom', 25], ['krish', 30],
       ['nick', 26], ['juli', 22]]
df = pd.DataFrame(lst, columns=['Name', 'Age'])

#Method2
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst, index =['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                                              columns =['Names'])
#Method3
# A temporary dataset to help with testcases and debugging

temp = pd.DataFrame(columns = ['userId','movieId','rating','timestamp'])
temp.loc[len(temp)] = [22,4,3.0,123]
temp.loc[len(temp)] = [22,5,3.0,123]

# when you join 2 data frames the resultant data frame may have a different sorting than the original dataframe
# If the test's relies on origin aordering follow the below technique
# basically instead of join you may have to rely on apply
data_clean['year'] = data_clean['onsale_dt'].map(lambda x: x[0:4])
years = np.arange(2004, 2017)
years = [str(year) for year in years]
inflation = np.array([0.033, 0.034, 0.025, 0.041, 0.001, 0.027, 0.015, 0.030, 0.017, 0.015, 0.008, 0.007, 0.021])
display(years)
display(inflation)
inflation_table = {}
for i in range(len(years)):
    inflation_table[years[i]] = 1 + inflation[i]

data_clean['per_ticket_price'] = data_clean.apply(lambda x: round(float(inflation_table[str(x['year'])]) * float(x['trans_face_val_amt']) / float(x['tickets_purchased_qty']), 2), axis=1)
data_clean = data_clean.reset_index()
data_clean.drop(columns = ['index'], inplace = True)

# Casting
def cast(df, key, value, join_how='outer'):
    """Casts the input data frame into a tibble,
    given the key column and value column.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns and value in df.columns
    assert join_how in ['outer', 'inner']

    fixed_vars = df.columns.difference([key, value])
    tibble = pd.DataFrame(columns=fixed_vars)  # empty frame

    ### BEGIN SOLUTION
    new_vars = df[key].unique()
    for v in new_vars:
        df_v = df[df[key] == v]
        del df_v[key]
        df_v = df_v.rename(columns={value: v})
        tibble = tibble.merge(df_v,
                              on=list(fixed_vars),
                              how=join_how)

    return tibble

#Melting
def melt(df, col_vals, key, value):
    assert type(df) is pd.DataFrame
    fixed_vars = df.columns.difference(col_vals)
    print(fixed_vars)
    x=pd.melt(df, id_vars =fixed_vars, value_vars =col_vals,
              var_name =key, value_name =value)
    #display(x)
    return x

#fill na with a specific value
df.fillna(0)
df_labresults_wide.fillna(0, inplace=True)

#pandas selecting rows and columns
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

#first non zero column
display(set((tibble.iloc[:,1:] > 0).idxmax(axis=1, skipna=True)))

#Apply lambda
# Remember  to provide axis=1
temp["L"]=temp.apply(lambda z: sqrt(pow(z['BX']-z['AX'],2)+pow(z['BY']-z['AY'],2)),axis=1)

#Split columns
df_labresults_sep[['test_value','date_taken']]=df_labresults_sep['result_date_taken'].str.split("(", expand=True)

#drop duplicated rows
temp.drop_duplicates(subset=primary_cols, inplace=True)

#Get Hour from Time
Accidents['Hour'] = pd.to_datetime(Accidents['Time']).dt.hour.astype(str)

#column addition with custom lambda
def label_treatment (row):
    treatments=[]
    if row['metformin'] == 'YES' :
        treatments.append('Metformin')
    if row['glipizide'] == 'YES' :
        treatments.append('Glipizide')
    if row['insulin'] == 'YES' :
        treatments.append('Insulin')
    if len(treatments) == 0:
        return 'No Treatment'
    return '-'.join(treatments)

df_treatments['treatment_type'] = df_treatments.apply (lambda row: label_treatment (row),axis=1)

#Pandas top 1 from group by
temp=temp[['Year', 'Month', 'Day_of_Week']].groupby(['Year', 'Month', 'Day_of_Week'], as_index=False).size().sort_values('size', ascending=False)
temp=temp.groupby(['Year','Month']).head(1)

# Rolling window
def daily_windowed_avg(df, days):
    df_avg = df.sort_values(by="Timestamp") \
               .set_index("Timestamp") \
               .groupby("ST") \
               .rolling(days) \
               .mean() \
               .reset_index() \
               .rename(columns={"Confirmed": "Avg"}) \
               .dropna()
    return df_avg.merge(df, on=["ST", "Timestamp"])

#pivot table
travel_matrix = pd.pivot_table(gnd_travel_ids,
                               index="Starting_City",
                               columns="Ending_City",
                               values="Average_Travel_Time")
travel_matrix.fillna(0, inplace=True)

x="12xx"
print("".join(i) for i in x if str(x).isnumeric())

#Create dataframe from dict
total_revenue_by_genre = pd.DataFrame.from_dict(revenue_by_genre, orient='index').rename(columns = {0: 'total_revenue'})
total_revenue_by_genre['genre'] = total_revenue_by_genre.index

#Data Type conversion
Drugs['Units'] = pd.to_numeric(Drugs['Units'].str.replace(',',''), errors='coerce')
Drugs['Admin Date'] = pd.to_datetime(Drugs['Admin Date'], infer_datetime_format=True)
Drugs['Month'] = Drugs['Admin Date'].dt.month

#Interesting Group by use case
# Group by ID and find unique rows and update column based on number of rows
who_switched = Drugs.groupby(['ID'])['Med'].unique().to_frame(name='Unique Med')
who_switched['Med A->B?'] = who_switched.apply(lambda x: 1 if len(x['Unique Med'])==2 else 0,axis=1)
who_switched['Newly_started'] = who_switched.apply(lambda x: 1 if x['Unique Med'].tolist()==['Med B'] else 0,axis=1)

#html to dataframe
#https://stackoverflow.com/questions/50633050/scrape-tables-into-dataframe-with-beautifulsoup/50633450

#pandas regex search
search_str = r"|".join(target_jobs)
temp = df['JOB TITLE'].str.contains(search_str)

#pandas series replace
s.str.replace(f'.*\s*{target}\s*.*', target, regex=True)