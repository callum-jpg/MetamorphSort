#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% Make some empty files for testing
num_files = range(1, 21)

for i in num_files:
    with open("_s{}.tiff".format(i), "w") as output:
        output.write("")
