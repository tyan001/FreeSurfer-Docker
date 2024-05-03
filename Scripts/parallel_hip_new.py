from pathlib import Path
import multiprocessing as mp
import os
import argparse

# Documentation of FreeSurfer Hippocampus & amygdala script https://surfer.nmr.mgh.harvard.edu/fswiki/HippocampalSubfieldsAndNucleiOfAmygdala
# Example: segment_subregions hippo_amygdala --cross 002_S_0295 --sd output
#        : segment_subregions [STRUCTURE] [--cross/--long-base] [SUBJ] --sd [$SUBJECT_DIR] <- Directory of FS output
subjs_dir = os.environ.get("SUBJECTS_DIR")
parser = argparse.ArgumentParser(description='Segmentation & amygdala segmentation process')
parser.add_argument('-sd', default=subjs_dir, type=str, help='Path to the subjects directory.')
parser.add_argument('-analysis', default="cross",type=str, help='Type of analysis cross-sectional or long base. cross or long-base')
parser.add_argument('-struct', type=str, default="hippo-amygdala",help='Structure to segmentation. i.e thalamus, hippo-amygdala, brainstem. (default: hippo_amygdala)')
parser.add_argument('--cores', type=int, default=1, help='Number of cores to use for parallel processing (default: 1)')

args = parser.parse_args()

def process_subject(subjects_path):
    subject = subjects_path.stem
    #print(f'segment_subregions {args.struct} --{args.analysis} {subject} --sd {args.sd}')
    os.system(f'segment_subregions {args.struct} --{args.analysis} {subject} --sd {args.sd}')

if __name__ == '__main__':
    
    subject_path = [f for f in Path(args.sd).glob('*') if f.is_dir()]
    
    pool = mp.Pool(processes=args.cores)
    pool.map(process_subject, subject_path)
    
    pool.close()
    pool.join()
    
    print("Processing completed.")