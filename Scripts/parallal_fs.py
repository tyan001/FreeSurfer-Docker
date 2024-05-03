from pathlib import Path
import multiprocessing as mp
import os
import argparse

parser = argparse.ArgumentParser(description='Process MRI data using FreeSurfer.')
parser.add_argument('-subjects', type=str, help='Path to the subjects directory.')
parser.add_argument('-output', type=str, help='Path to the output directory for FreeSurfer results.')
parser.add_argument('-fs_cmd', type=str, help='Path to the FreeSurfer bin directory or FreeSurfer command. i.e /path/to/bin/recon-all or recon-all', default='recon-all')
#parser.add_argument('--extension', type=str, default='.nii', help='File extension to process (default: .nii)')
parser.add_argument('--cores', type=int, default=mp.cpu_count(), help='Number of cores to use for parallel processing (default: all available cores)')

args = parser.parse_args()

def process_subject(subjects_path):
    subject = subjects_path.stem
    print(f'Processing subject: {subject}')
    os.system(f'{args.fs_cmd} -i {subjects_path} -subjid {subject} -sd {args.output} -all')

if __name__ == '__main__':
    
    subject_path = [f for f in Path(args.subjects).glob('*.nii')]
    
    pool = mp.Pool(processes=args.cores)
    pool.map(process_subject, subject_path)
    
    pool.close()
    pool.join()
    
    print("Processing completed.")