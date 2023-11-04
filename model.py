import pandas as pd
from sklearn.cluster import KMeans
from subprocess import run


data = pd.read_csv('wc.csv')


selected_columns = ['Age', 'Rating']

kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(data[selected_columns])

cluster_counts = data['cluster'].value_counts()

cluster_counts.to_csv('k.txt', header=False)

run(["python", "final.sh", 'wc.csv'])