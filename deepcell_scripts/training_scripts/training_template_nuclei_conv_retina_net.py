"""
training_template.py

Train a simple deep CNN on a dataset in a fully convolutional fashion.

Run command:
	python training_template_fully_conv.py

@author: David Van Valen
"""

from __future__ import print_function
from tensorflow.python.keras.optimizers import SGD, RMSprop, Adam

from deepcell import rate_scheduler, train_model_retina_net as train_model
from deepcell import resnet50_retinanet as the_model

import os
import datetime
import numpy as np
from scipy.misc import imsave

batch_size = 1
n_epoch = 200

dataset = "nuclei_conv_61x61"
expt = "retina_net"

direc_save = "/data/trained_networks/nuclei/"
direc_data = "/data/training_data_npz/nuclei/"

optimizer = Adam(lr=1e-5, clipnorm=0.001)
# optimizer = SGD(lr = 0.001, momentum = 0.9, nesterov = True)
lr_sched = rate_scheduler(lr = 1e-5, decay = 0.999)

file_name = os.path.join(direc_data, dataset + ".npz")
training_data = np.load(file_name)

for iterate in xrange(1):

	model = the_model(num_classes = 1, input_shape = (1,512,512))

	trained_model = train_model(model = model, dataset = dataset, optimizer = optimizer, 
		expt = expt, it = iterate, batch_size = batch_size, n_epoch = n_epoch,
		direc_save = direc_save, direc_data = direc_data, 
		lr_sched = lr_sched, rotation_range = 180, flip = True, shear = False)





