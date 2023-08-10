**Preparation:** *note that all analyses were conducted in a linux environment, and we cannot guarantee direct reproducibility in other environments*
1. Create a folder where you will put all jupyter notebook and the following associated files (accessible from https://doi.org/10.17605/OSF.IO/GT7EX):
    * diagnosis_outputs (3.3Gb): analysis QC outputs generated from RABIES across datasets and confound correction strategies necessary for figure_2_repro, sup_figure_10_11_repro, sup_figure_9_repro
    * sample_size_repro_files (807Mb): Files required to run sample_size_effect_repro.ipynb. Contains dual regression outputs (DR_maps/) for the REST-AWK mediso dataset, together with associated BOLDsd (temporal_std/) and CRsd (CR_std/) brain maps and framewise displacement measures (FD_csv/) necessary to derive the group statistical report. Other files consist of overlapping template and mask files used for display.
    * conf_corr_overfitting_files.zip (691Mb): files associated to conf_corr_overfitting_repro.ipynb. Consist of the preprocessed timeseries for the subject 015 from the 7_Cryo_mediso_v, as well as associated files for confound correction and template, mask and ICA files overlapping with the subject.
2. Download anaconda (https://www.anaconda.com/) or miniconda (https://docs.conda.io/en/latest/miniconda.html) and create a new conda environment using the rabies_analysis_repro.yml environment file with `conda env create -f rabies_analysis_repro.yml`. By default the environment will be called rabies_analysis_repro, and can be activated with `conda activate rabies_analysis_repro`
3. Open jupyter lab interface by typing `jupyter lab`, then execute the jupyter notebooks

**Notebooks:**
* figure_2_repro.ipynb: reproduces figure 2
    * Change the path from `template_file='/home/gabriel/.local/share/rabies/EPI_template.nii.gz'` with this file https://zenodo.org/record/5118030/files/EPI_template.nii.gz, then the script should execute appropriately.
* sup_figure_9_repro.ipynb: reproduces supplementary figure 9
* sup_figure_10_11_repro.ipynb: generates all the figures found in the main figure 5, and the supplementary figures 10 & 11
    * Change the path from `template_file='/home/gabriel/.local/share/rabies/EPI_template.nii.gz'` with this file https://zenodo.org/record/5118030/files/EPI_template.nii.gz, then the script should execute appropriately.
* conf_corr_overfitting_repro.ipynb: reproduces sup. figure 6C
    * Change the path from `template_file='/home/gabriel/.local/share/rabies/EPI_template.nii.gz'` with this file https://zenodo.org/record/5118030/files/EPI_template.nii.gz, then the script should execute appropriately.
    * Move the files inside conf_corr_overfitting_files.zip in the same folder as the jupyter notebook to execute.
* sample_size_effect_repro.ipynb: reproduces sup. figure 8B
    * Move the files inside sample_size_repro_files.zip in the same folder as the jupyter notebook to execute.
* butterworth_filter_simulation.ipynb: reproduces sup. figure 2
