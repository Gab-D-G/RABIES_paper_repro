#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
singularity run -B /scratch/m/mchakrav/desgab/rats/ds003646_inputs:/nii_inputs:ro \
-B /scratch/m/mchakrav/desgab/rats/rabies_ds003646_20211026:/rabies_out \
-B /home/m/mchakrav/desgab/atlases:/atlases:ro \
/home/m/mchakrav/desgab/singularity_images/rabies-0.3.3.sif -p MultiProc preprocess /nii_inputs /rabies_out \
--anat_template /atlases/Fischer344_nii_v4/Fischer344_template.nii --brain_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii \
--WM_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii --CSF_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii --vascular_mask /atlases/Fischer344_nii_v4/Fischer344_template_mask.nii \
--labels /atlases/Fischer344_nii_v4/Fischer344_template_labels.nii --bold_only

