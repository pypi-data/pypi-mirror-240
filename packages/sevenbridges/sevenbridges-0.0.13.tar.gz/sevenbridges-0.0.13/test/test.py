
#%%
import numpy as np

latitude_longitude_data = np.array([
    [40.09068,116.17355],
     [40.00395,116.20531],
     [39.91441,116.18424],
     [39.81513,116.17115],
     [39.742767,116.13605],
     [39.987312,116.28745],
     [39.98205,116.3974],
     [39.95405,116.34899],
     [39.878193,116.351974],
     [39.876183,116.39401],
     [39.855957,116.36781],
     [39.93712,116.46074],
     [39.929287,116.416885],
     [39.939552,116.48375],
     [39.929302,116.35103],
     [39.86347,116.27908],
     [39.718147,116.40616],
     [39.79449,116.50632],
     [39.885242,116.66416],
     [39.88649,116.40736],
     [39.899136,116.395386],
     [39.920994,116.44345],
     [40.127,116.655],
     [40.217,116.23],
     [39.937,116.106],
     [40.143,117.1],
     [40.328,116.628],
     [40.37,116.832],
     [40.453,115.972],
     [40.292,116.22],
     [40.365,115.988],
     [40.499,116.911],
     [40.1,117.12],
     [39.712,116.783],
     [39.52,116.3],
     [39.579998,116.0]
])

data_in_radians = np.radians(latitude_longitude_data)
n_clusters = 6

from sevenbridges.graphcreator import graph_generator
generator = graph_generator()
generator.kmeans(latitude_longitude_data, n_clusters)

# cluster_labels, cluster_centers = kmeans(data_in_radians, n_clusters)
# cluster_centers_degrees = np.degrees(cluster_centers)
# for i, center in enumerate(cluster_centers_degrees):
    # print(f'Cluster {i + 1} Center: Latitude {center[0]}, Longitude {center[1]}')
# print("Cluster Labels:", cluster_labels)