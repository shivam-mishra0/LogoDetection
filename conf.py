# config.py

import torch
BATCH_SIZE = 1
RESIZE_TO = 360
NUM_EPOCHS = 100

DEVICE = torch.device(
    'cuda') if torch.cuda.is_available() else torch.device('cpu')

# training images and XML files directory

TRAIN_DIR = "/home/shivam/Downloads/FasterRCNN/Datasets/train"
VALID_DIR = "/home/shivam/Downloads/FasterRCNN/Datasets/valid"

CLASSES = [
    'background',
    'puma',
    'addidas',
    'nike',
    'UnderArmour'
]

NUM_CLASSES = 5

# whether to visualize images after crearing the data loaders

VISUALIZE_TRANSFORMED_IMAGES = False

OUT_DIR = "/home/shivam/Downloads/FasterRCNN/output"
SAVE_PLOTS_EPOCH = 2
SAVE_MODEL_EPOCH = 2
