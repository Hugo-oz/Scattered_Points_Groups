from main import find_clusters
from utils import generate_random_points, clusters_plot

# Define the number of points
num_points = 10000

# Define the points X and Y coordinates limits
grid_length = [20, 20]

# Define the number of clusters
num_clusters = 10

# Generate random points
points = generate_random_points(num_points, grid_length)

# Finds num_clusters clusters. num_clusters = Number of clusters
clusters = find_clusters(points, num_clusters)

# Plot the clusters found
clusters_plot(clusters, num_clusters)