import pandas as pd
# import subprocess as call
def data_cleaning(df):
    df = df.drop_duplicates()

    df = df.dropna()
    return df

def data_transformation(df):
    df['rating'] = df['rating'].astype(str)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    return df

def data_reduction(df):
    relevant_columns = ['product_name', 'category']
    df_reduced = df[relevant_columns]

    df_filtered = df[df['rating'] > 5]

    return df

def data_discretization(df):
    #Convert a continuous variable into a categorical variable
    df['category'] = pd.qcut(df['rating'], q=4, labels=False)

    #Bin a numerical column into categories
    data = df["rating"]
    df = pd.DataFrame(data)

    rating_bins = [0, 4, 8, 10] 
    rating_labels = ['low', 'normal', 'high']
    df['rating_category'] = pd.cut(df['rating'], bins=rating_bins, labels=rating_labels)


    return df


df = pd.read_csv('res.csv')
df = data_cleaning(df)
df = data_transformation(df)
df = data_reduction(df)
df = data_discretization(df)

output_file = 'res_dpre.csv'
df.to_csv(output_file, index=False)