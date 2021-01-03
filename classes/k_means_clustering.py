import random

from classes.information_helper import *


class KMeans:
    def __init__(self, matrix, k, iterations, output_writer):
        self.matrix = matrix
        self.k = k
        self.iterations = iterations
        self.output_writer = output_writer

    def __map_examples_to_clusters(self, centroids: []) -> [[int]]:
        result: [] = [[] for i in range(self.k)]
        for x in self.matrix:
            idx = find_nearest_cluster_index(x, centroids)
            result[idx].append(x)
        return result

    def __choose_initial_centroids(self) -> []:
        centroids: [] = random.sample(self.matrix, self.k)
        return centroids

    def __calculate_new_centroids(self, result: []) -> []:
        centroids: [] = []
        for cluster in result:
            new_centroid: [] = [0 for i in range(DATA_WIDTH)]
            for data in cluster:
                for i in range(DATA_WIDTH):
                    new_centroid[i] += data[i]
            if len(cluster) != 0:
                for i in range(DATA_WIDTH):
                    new_centroid[i] /= len(cluster)
            centroids.append(new_centroid)
        return centroids

    def cluster(self) -> [[int]]:
        clusters = []
        centroids = self.__choose_initial_centroids()
        distortions = []  # distortion[i][j] is the distortion of the j'th cluster at i'th iteration
        labels_frequency_in_clusters = []  # labels_frequency_in_clusters[i][j][k] is the frequency of the k'th label of j'th cluster at i'th iteration

        for i in range(self.iterations):
            print(f"running {i + 1}'{ORDER_SUFFIXES[i] if (i <= 2) else ORDER_SUFFIXES[3]} iteration ")
            clusters = self.__map_examples_to_clusters(centroids)

            distortions.append(find_distortions(clusters, centroids))
            labels_frequency_in_clusters.append(build_label_frequency_in_clusters(clusters))

            self.output_writer.save_centroids_to_images(centroids)
            centroids = self.__calculate_new_centroids(clusters)

        self.output_writer.save_centroids_to_images(centroids)
        self.output_writer.save_samples_from_clusters(clusters)

        return clusters, centroids, distortions, labels_frequency_in_clusters
