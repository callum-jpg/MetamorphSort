#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil # for copying files to new directory

# test sorting
# Choose range of stage position and the desired save folder (k:v)
stage_to_folder = {range(1, 11) : "Positions 1:10",
                   range(11, 21): "Positions 11:20"
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



