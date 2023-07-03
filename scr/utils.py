import matplotlib.pyplot as plt
import random

def generate_random_points(num_points, grid_length):
    # Create an array to store the points
    points = []
    # Loop num_points times to generate X and Y random coordinates points
    for _ in range(num_points):
        x = random.uniform(0, grid_length[0])
        y = random.uniform(0, grid_length[1])
        points.append([x, y])
    return points

def clusters_plot(clusters, num_clusters):
# Create an array to store the clusters
    cluster_points = []
    for _ in range(num_clusters):
        cluster_points.append([])
    # Iterates over the clusters in order to create a scatter plot for each cluster
    for cluster_id, cluster_points_list in clusters.items():
        for point in cluster_points_list:
            cluster_points[cluster_id].append(point)

    # Generate random colors for each cluster
    colors = []
    for _ in range(num_clusters):
        color = (random.random(), random.random(), random.random())
        colors.append(color)

    # Plot each point and add a color according to his label
    for cluster_id, points in enumerate(cluster_points):
        x_values = [point[0] for point in points]
        y_values = [point[1] for point in points]
        plt.scatter(x_values, y_values, color=colors[cluster_id])

    # Add labels to the plot
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Clusters')
    plt.show()