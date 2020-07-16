#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil # for copying files to new directory

# Choose range of stage position and the desired save folder (k:v)
stage_to_folder = {range(1, 51) : "nt-nt",
                   range(51, 101): "nt-olaparib",
                   range(101, 151):"nt-veliparib",
                   range(151, 201): "+dt-nt",
                   range(201, 251): "+dt-olaparib",
                   range(251, 301): "+dt-veliparib",
                   range(301, 351): "mms-nt",
                   range(351, 401): "mms-olaparib",
                   range(401, 451): "mms-veliparib"
                   }

image_dir = os.listdir()

# WORKS!
for i in image_dir:
    # Extract stage position, eg. s41.tiff = 41.
    regex = re.findall(r"\d+\.", i)
    for j in regex:
    # Remove the ., convert to in for in range check
        stage_pos = int(j[:-1])
        for k,v in stage_to_folder.items():
            if stage_pos in k:
                if not os.path.isdir(v):
                    os.mkdir(v)
                filename = os.path.join(os.getcwd(), i)
                save_filename = os.path.join(os.getcwd(), v, i)
                shutil.copy(filename, save_filename)


