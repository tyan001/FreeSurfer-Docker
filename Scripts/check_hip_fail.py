from pathlib import Path
import multiprocessing as mp
import os

def process_subject(subject_paths):
    subject = subject_paths.stem
    print(f"segmentHA_T1.sh {subject} output")
    os.system(f'segmentHA_T1.sh {subject} output')

if __name__ == '__main__':
    
    file_paths = Path("output")
    subdirectories = [entry for entry in file_paths.iterdir() if entry.is_dir()]
    # len(files)
    # print(len(subdirectories))
    file_to_check = "lh.hippoSfVolumes-T1.v22.txt"
    missing_hipp = []
    for i, subdir in enumerate(subdirectories):
        files_in_sub = subdir/ "mri" /file_to_check
        if not files_in_sub.exists():
            missing_hipp.append(subdir)
            # print(f"{i} : {files_in_sub} not found in {subdir}")
            
    missing_hipp.sort()
    print(missing_hipp)
    
    # pool = mp.Pool(processes=mp.cpu_count())
    # pool.map(process_subject, missing_hipp)
    
    # pool.close()
    # pool.join()
    
    # print("Processing completed.")
