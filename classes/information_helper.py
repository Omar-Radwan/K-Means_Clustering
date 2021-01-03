import math

import matplotlib.pyplot as plt
from classes.constants import *


def calculate_distance(x: [int], y: [int]) -> int:
    result: int = 0
    for i in range(COLOR_WIDTH):
        p1, q1, r1 = x[i], x[i + COLOR_WIDTH], x[i + 2 * COLOR_WIDTH]
        p2, q2, r2 = y[i], y[i + COLOR_WIDTH], y[i + 2 * COLOR_WIDTH]
        s1, s2, s3 = p1 - p2, q1 - q2, r1 - r2
        result += math.sqrt(s1 * s1 + s2 * s2 + s3 * s3)
    return result


def find_nearest_cluster_index(x: [], centroids: []) -> int:
    min_idx, min_diff = -1, int(2e9)
    cur_idx: int = 0
    for y in centroids:
        cur_diff = calculate_distance(x, y)
        if cur_diff < min_diff:
            min_idx, min_diff = cur_idx, cur_diff
        cur_idx += 1
    return min_idx


def build_label_frequency_in_clusters(output: []) -> [[]]:
    k = len(output)
    cluster_label_count = [[0 for j in range(LABEL_SIZE)] for i in range(k)]
    for cluster_index in range(len(output)):
        for example in output[cluster_index]:
            correct_label = example[LABEL_INDEX]
            cluster_label_count[cluster_index][correct_label] += 1
    return cluster_label_count


def find_distortions(clusters: [], centroids: []):
    k = len(centroids)
    distortions = [0 for i in range(k)]
    for centroid_index in range(k):
        for example in clusters[centroid_index]:
            distance = calculate_distance(centroids[centroid_index], example)
            distortions[centroid_index] += (int(distance) * int(distance))
    return distortions


class InformationHelper:
    def __init__(self, k, iterations):
        self.__k = k
        self.__iterations = iterations

    def build_distortion_graph(self, distortions):
        x = [i for i in range(1, self.__iterations + 1)]
        y = [sum(distortions[i]) for i in range(self.__iterations)]
        plt.plot(x, y)
        plt.xlabel(X_LABEL)
        plt.ylabel(Y_LABEL)
        plt.title(GRAPH_TITLE)

    def build_maximum_label_tuples(self, label_frequency, clusters):
        max_label_tuples = [(-1, -1, -1) for i in range(self.__k)]
        total_percentage = 0
        for cluster_index in range(self.__k):
            max_tuple = (0, -1)
            for label_index in range(LABEL_SIZE):
                max_tuple = max((label_frequency[cluster_index][label_index], label_index), max_tuple)

            cluster_size = len(clusters[cluster_index])

            percentage = f'{(max_tuple[0] / cluster_size * 100)}%'
            max_tuple = (max_tuple[0], cluster_size, max_tuple[1], LABEL_INDEX_TO_NAME[max_tuple[1]],
                         percentage)
            total_percentage += max_tuple[0] / cluster_size
            max_label_tuples[cluster_index] = max_tuple

        total_percentage = (total_percentage / self.__k) * 100
        total_percentage_string = f'{total_percentage}%'
        return max_label_tuples, total_percentage_string
