from constants import *
import pickle


class InputParser:

    def __init__(self, batches_count: int, size: int):
        self.data = []
        self.matrix = []
        self.batches_count = batches_count
        self.size = size

    def __unpickle(self, file):
        with open(file, 'rb') as fo:
            dict = pickle.load(fo, encoding='bytes')
        return dict

    def __load_data_patches(self):
        for i in range(self.batches_count):
            self.data.append(self.__unpickle(f'{INPUT_PATH_PREFIX}{i + 1}'))

    def __data_to_matrix(self):
        for batch_index in range(self.batches_count):
            for example_index in range(self.size):
                matrix_row = [0 for i in range(COLUMNS)]
                i = 0
                for rgb_value in self.data[batch_index][DATA_KEY][example_index]:
                    matrix_row[i] = (int(rgb_value))
                    i += 1
                matrix_row[BATCH_INDEX] = batch_index
                matrix_row[TITLE_INDEX] = (self.data[batch_index][FILE_NAME_KEY][example_index])
                matrix_row[LABEL_INDEX] = (self.data[batch_index][LABEL_KEY][example_index])
                matrix_row[INDEX_IN_BATCH_INDEX] = example_index
                self.matrix.append(matrix_row)

    def load_data(self) -> ([], []):
        self.__load_data_patches()
        self.__data_to_matrix()
        return self.matrix, self.data
