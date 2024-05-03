# Script was used to move the files into one folder.
from pathlib import Path
import os
file_path = Path("/raid/tyan/Freesurfer_Processing/HarP/output")
files = list(file_path.rglob("*IsRunningHP*"))
files.sort()

print(files)
print(len(files))

# for file in files:
#     os.remove(file)  