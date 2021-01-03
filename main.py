from classes.information_helper import InformationHelper
from classes.constants import *
from classes.input_parser import InputParser
from classes.k_means_clustering import KMeans
from classes.output_writer import OutputWriter

matrix, data = [], []


def run_trial(k, iterations):
    output_writer = OutputWriter(data, k, iterations)
    information_helper = InformationHelper(k, iterations)
    k_means = KMeans(matrix, k, iterations, output_writer)
    clusters, centroids, distortions, labels_frequency_in_clusters_all_iterations = k_means.cluster()

    information_helper.build_distortion_graph(distortions)
    output_writer.save_distortion_graph()

    max_label_tuples, total_percentage_string = information_helper.build_maximum_label_tuples(
        labels_frequency_in_clusters_all_iterations[-1],
        clusters)

    output_writer.save_in_excel_sheet(max_label_tuples, total_percentage_string)


if __name__ == '__main__':
    k = int(input("Enter the value of k: "))
    iterations = int(input("Enter the number of iterations: "))
    print(f"unpacking data from {NUMBER_OF_BATCHES} batches that contain a total of {NUMBER_OF_BATCHES * SIZE_FROM_BATCH} images ...")
    input_parser = InputParser(NUMBER_OF_BATCHES, SIZE_FROM_BATCH)
    matrix, data = input_parser.load_data()
    print("data unpacked")
    print("running K-Means")
    run_trial(k, iterations)
    print("done")