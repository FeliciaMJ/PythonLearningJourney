import os
import sys
import time
import numpy as np
import tensorflow as tf
from sklearn import metrics
from nlp_task.text_classification.cnn_model import TCNNConfig, TextCNN
from nlp_task.text_classification