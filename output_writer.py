import os
from random import random

from pip._vendor.pep517.dirtools import mkdir_p
import numpy
from constants import *
import matplotlib.pyplot as plt
import xlwt
from xlwt import Workbook
from datetime import datetime


class OutputWriter:
    def __init__(self, data, k, iterations):
        self.__data = data
        self.__cnt = 0
        self.__k = k
        self.__iterations = iterations
        self.__output_dir_lvl_0 = f'./output/iterations= {self.__iterations}, K= {self.__k}'
        mkdir_p(self.__output_dir_lvl_0)
        run_id = len(os.listdir(self.__output_dir_lvl_0))
        self.__output_dir_lvl_0 += f'/run_id= {run_id}'
        mkdir_p(self.__output_dir_lvl_0)

    def __writeTupleToSheet(self, sheet, tuple, row: int):
        for col in range(len(tuple)):
            sheet.write(row, col, tuple[col])

    def __save_image(self, label: int, img):
        im_r = img[0:1024].reshape(32, 32)
        im_g = img[1024:2048].reshape(32, 32)
        im_b = img[2048:].reshape(32, 32)
        img = numpy.dstack((im_r, im_g, im_b))

        output_dir_lvl_1 = f'{self.__output_dir_lvl_0}/{label}'
        mkdir_p(output_dir_lvl_1)

        plt.imsave(f'{output_dir_lvl_1}/{"{:03d}".format(self.__cnt)}.png', img)
        self.__cnt += 1

    def save_samples_from_clusters(self, output: []):
        for cluster_index in range(len(output)):
            END = min(len(output[cluster_index]), MAX_NUMBER_OF_SAMPLE_IMAGES)
            for example_index in range(END):
                current_example = output[cluster_index][example_index]
                self.__save_image(cluster_index,
                                  self.__data[current_example[BATCH_INDEX]][DATA_KEY][
                                      current_example[INDEX_IN_BATCH_INDEX]])

    def save_in_excel_sheet(self, max_labels_tuples, total_percentage):
        work_book = Workbook()
        sheet1 = work_book.add_sheet(SHEET_NAME)
        title_tuple = (COL_TITLE[0], COL_TITLE[1], COL_TITLE[2], COL_TITLE[3], COL_TITLE[4])
        self.__writeTupleToSheet(sheet1, title_tuple, 0)
        for i in range(0, self.__k):
            self.__writeTupleToSheet(sheet1, max_labels_tuples[i], i + 1)
        sheet1.write(self.__k + 1, 4, total_percentage)
        sheet1.write(self.__k + 1, 0, "Total")
        work_book.save(f'{self.__output_dir_lvl_0}/sheet.xls')

    def save_centroids_to_images(self, centroids: []):
        for i in range(len(centroids)):
            dummy = []
            for j in range(DATA_WIDTH):
                dummy.append(int(centroids[i][j]))
            self.__save_image(i, numpy.array(dummy, dtype="uint8"))

    def save_distortion_graph(self):
        plt.savefig(f'{self.__output_dir_lvl_0}/graph.png')
        plt.show()
