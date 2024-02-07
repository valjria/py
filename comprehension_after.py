import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list =  ["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list

print(soz)
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)





