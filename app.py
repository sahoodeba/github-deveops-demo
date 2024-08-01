import pandas as pd

#Step 1: Read data from a CSV file
df=pd.read_csv('C:/Users/DEBASHISH/Downloads/Data Analysis/Diwali Sales Data.csv',encoding='unicode_escape')
print(df);

# Print the few rows of the data
a=df.head()
print(a);

# Step 2: Perform some basic data manipulation
shape=df.shape
print(shape);

info=df.info()
print(info)

drop_col=df.drop(['Status','unnamed1'],axis=1,inplace=True);
print(drop_col);

info1=df.info()
print(info1);

null_check=df.isnull()
print(null_check)

null_check1=df.isnull().sum()
print(null_check1)


drop_null=df.dropna(inplace=True);

null_check2=df.isnull().sum();
print(null_check2)

duplicate_check=df.duplicated()
print(duplicate_check);

drop_Duplicate=df.drop_duplicates(inplace=True)

print(df)

info4=df.info()
print(info4)

data_type=df['Amount'].astype('int')
# print(data_type)
info5=df.info()
print(info5);

print(df)

rename_col=df.rename(columns={'Zone':'Zones'},inplace=True)
print(df);

Upper=df['Zones'].str.upper()
print(Upper)

export_clean_Data=df.to_csv('Diwali_Sales1.csv',index=True)