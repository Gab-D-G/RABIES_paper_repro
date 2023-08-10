#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
singularity run -B /scratch/m/mchakrav/desgab/data/multicenter/inputs/94_RT_mediso_f2:/nii_inputs:ro \
-B /scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_94_RT_mediso_f2_20221024:/rabies_out \
/home/m/mchakrav/desgab/singularity_images/rabies-0.4.7.sif \
-p MultiProc preprocess /nii_inputs /rabies_out \
--bold_only --commonspace_resampling 0.2x0.2x0.2 --bold_autobox \
--commonspace_reg masking=true,brain_extraction=true,template_registration=SyN,fast_commonspace=false
