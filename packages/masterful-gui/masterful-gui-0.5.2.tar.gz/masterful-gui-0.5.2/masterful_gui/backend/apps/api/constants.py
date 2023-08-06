"""Define application wide costants for the API server."""

import os

_USER = f'{os.path.expanduser("~")}'

# The location where the scanner should look for serialzed training runs.
TRAINING_RUN_SCAN_DIR = f'{_USER}/.masterful/gui/exports'

# The extension of a serialized TrainingRun proto file. The extension actually
# makes no difference, this is just to facilitate identifying the right files
# to read.
# WARNING: This matches the configuration of gui.exporter module in
# masterful package. You must change them both or you'll break the GUI.
TRAINING_RUN_EXT = "trp"

# The location where the GUI can export artifacts needed for running the app.
# One example is generating PNG images from binary data received from Masterful.
ARTIFACTS_DIR = f'{_USER}/.masterful/gui/data'

MODEL_GRAPH_IMAGE_NAME = 'model_graph_image'

# Dir where model graph image is stored. Nested under MEDIA_ROOT/<run_name>/
MODEL_IMG_DIR = 'model'

# Dir where dataset sample images are stored.
# Nested under MEDIA_ROOT/<run_name>/
DATASET_IMG_DIR = 'dataset'

BINARY_SAMPLE_RUN_NAME = 'Sample run 1'
BINARY_SAMPLE_RUN_FILE_NAME = 'sample_run_bc'
CLASSIFICATION_SAMPLE_RUN_NAME = 'Sample run 2'
CLASSIFICATION_SAMPLE_RUN_FILE_NAME = 'sample_run_c'