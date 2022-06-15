#!/bin/env python

import os
import sys
from matplotlib import image
import numpy as np
import h5py

if len(sys.argv) > 1:
    img_file = sys.argv[1]
    img_file_name = os.path.basename(img_file)
    image = image.imread(img_file)
    data = np.asarray(image, dtype='<i2')
    tumorBorder=np.empty(shape=(1,42), dtype='<f8')
    mat = h5py.File('no_mat/' + img_file_name + '.mat', 'w')
    cjdata = mat.create_group("cjdata");
    cjdata.create_dataset("tumorBorder", (1,42), dtype='<f8', data=tumorBorder)
    cjdata.create_dataset("image", data=data)
    cjdata.create_dataset("label", data=[[0.]], dtype="<f8")