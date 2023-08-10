import pathlib
import sys
import glob
import pandas as pd
cleaned_path = sys.argv[1]
out_path = sys.argv[2]
outliers = sys.argv[3]
file_list = glob.glob(cleaned_path)

outlier_list = outliers.split(',')

# specify the missing preproc scans
failed_list=['sub-jgrAesAWc21L_ses-1_task-rest_acq-EPI_run-1_bold', 'sub-212_ses-1_task-rest_acq-EPI_bold']

exclusion_list = failed_list+outlier_list

name_list=[]
for f in file_list:
    include=True
    print(f)
    name = pathlib.Path(f).name.rsplit("_bold_")[0]
    print(name)
    for failed in exclusion_list:
        if name in failed:
            include=False
    if include:
        name_list.append(name+'_bold.nii.gz')
if len(name_list)<10:
    print('Dataset had under 10 scans left, no analysis is conducted.')
    name_list=[]

pd.DataFrame(name_list).to_csv(out_path, index=None, header=False)
