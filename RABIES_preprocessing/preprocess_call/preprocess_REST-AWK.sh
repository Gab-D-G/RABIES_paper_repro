#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
singularity run -B /scratch/m/mchakrav/desgab/data/bids_grandjean_rest_awk_subset:/nii_inputs:ro \
-B /scratch/m/mchakrav/desgab/new_rest_awk_analysis/rabies_bids_grandjean_rest_awk_subset_20211026:/rabies_out \
-B /home/m/mchakrav/desgab/atlases:/atlases:ro \
/home/m/mchakrav/desgab/singularity_images/rabies-0.3.3.sif -p MultiProc preprocess /nii_inputs /rabies_out \
--anatomical_resampling 0.15x0.15x0.15 --commonspace_resampling 0.2x0.2x0.2 \
--labels /atlases/hierarchical_downsample/DSURQE_downsample.nii.gz
