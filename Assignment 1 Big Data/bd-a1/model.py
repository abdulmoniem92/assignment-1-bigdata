import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("amazon.csv")

df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=True)
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')

df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

columns = ['discount_percentage', 'rating', 'rating_count'] 
df[columns] = pd.to_numeric(df[columns], errors='coerce')

k = 3  
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(df[columns])

cluster_labels = kmeans.labels_

cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

cluster_counts_filename = "k.txt"
cluster_counts.to_csv(cluster_counts_filename, index=False, header=False)