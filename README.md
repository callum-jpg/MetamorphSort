## For sorting stage position files from Metamorph

This script intends to sort a range of stage position images into a desired folder. This is a pre-requisite to the CellProfiler analysis pipeline which I use, tthat uses REGEX to group data based on the parent folder.

I found this method easier and more deliberate (with ever changing experimental conditions) than trying to find a unifying REGEX to extract grouping data from the filename.

Moreover, the designated destination folder for ranges of stage images becomes an identifier for each condition in later analysis.
