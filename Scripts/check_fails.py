# Script was used to move the files into one folder.
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Error checking FS output by checking if there is a recon-all.error file in scripts folder')
parser.add_argument('-i', default="HarP/output", type=str, help='Path to the FS directory with all subjects')

args = parser.parse_args()

file_path = Path(args.i)
files = list(file_path.rglob("*recon-all.error*"))
files.sort()
print(len(files))

log_list = []
for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
        l = lines[-1].strip()
    
    with open("FS_log.txt", "a") as lf:
        print(f"{file.parent.parent.stem}: {l}", file=lf)

