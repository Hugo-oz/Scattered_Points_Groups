from sklearn.cluster import KMeans


def find_clusters(points, clusters_num):
    # Define the number of clusters
    kmeans = KMeans(n_clusters=clusters_num)

    # Fit the model to the points
    kmeans.fit(points)

    # Get the cluster labels assigned to each point
    cluster_labels = kmeans.labels_

    # Create a dictionary to store the clusters
    clusters = {}
    for i, label in enumerate(cluster_labels):
        # Add the point to the corresponding cluster
        if label in clusters:
            clusters[label].append(points[i])
        else:
            clusters[label] = [points[i]]
    return clusters