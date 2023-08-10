#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
singularity run -B /scratch/m/mchakrav/desgab/data/multicenter/inputs/7_Cryo_aw_f:/nii_inputs:ro \
-B /scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_aw_f_20221024:/rabies_out \
/home/m/mchakrav/desgab/singularity_images/rabies-0.4.7.sif \
-p MultiProc preprocess /nii_inputs /rabies_out \
--bold_only --commonspace_resampling 0.2x0.2x0.2 \
--commonspace_reg masking=true,brain_extraction=false,template_registration=SyN,fast_commonspace=false
