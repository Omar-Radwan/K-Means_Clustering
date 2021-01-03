DATA_WIDTH = 3072
COLUMNS = 3076

BATCH_INDEX = 3072
TITLE_INDEX = 3073
LABEL_INDEX = 3074
INDEX_IN_BATCH_INDEX = 3075

COLOR_WIDTH = 1024

SIZE_FROM_BATCH = 100
MAX_K = 10
MAX_ITERATIONS = 4
NUMBER_OF_BATCHES = 5
ITERATIONS = 0
LABEL_INDEX_TO_NAME = ['airplane',
                       'automobile',
                       'bird',
                       'cat',
                       'deer',
                       'dog',
                       'frog',
                       'horse',
                       'ship',
                       'truck']
LABEL_SIZE = 10
DATA_KEY = b'data'
FILE_NAME_KEY = b'filenames'
LABEL_KEY = b'labels'

INPUT_PATH_PREFIX = './cifar-10-batches-py/data_batch_'

COL_TITLE = ['# examples belonging to max class',
             'Total # of examples in cluster',
             'max label index',
             'max label',
             'accuracy'
             ]

X_LABEL = 'Iterations'
Y_LABEL = 'Value of distortion'
GRAPH_TITLE = 'Distortion value as function of # of iterations'
SHEET_NAME = 'Sheet 1'
MAX_NUMBER_OF_SAMPLE_IMAGES = 20

IMAGE_ROWS = 32
IMAGE_COLUMNS = 32

EXAMPLES_BELONG_TO_MAX_CLASS_INDEX = 0
TOTAL_EXAMPLES_IN_CLUSTER_INDEX = 1
MAX_LABEL_INDEX_INDEX = 2
MAX_LABEL_INDEX = 3
ACCURACY_INDEX = 4
ORDER_SUFFIXES = ['st', 'nd', 'rd', 'th']