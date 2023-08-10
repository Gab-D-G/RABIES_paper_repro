#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
singularity run -B /scratch/m/mchakrav/desgab/rats/upenn_data/inputs:/nii_inputs:ro \
-B /scratch/m/mchakrav/desgab/rats/rabies_upenn_20211026:/rabies_out \
-B /home/m/mchakrav/desgab/atlases:/atlases:ro \
/home/m/mchakrav/desgab/singularity_images/rabies-0.3.3.sif -p MultiProc preprocess /nii_inputs /rabies_out \
--anat_template /atlases/Fischer344_nii_v4/Fischer344_template.nii --brain_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii \
--WM_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii --CSF_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii --vascular_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii \
--labels /atlases/Fischer344_nii_v4/Fischer344_template_labels.nii --anat_inho_cor no_reg --anat_autobox --bold_autobox --bold_inho_cor_otsu 3

