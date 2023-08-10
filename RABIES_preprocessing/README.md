**Reproducing preprocessing:**
Every preprocessing script found within preprocess_call/ is structured similarly to the following:

```sh
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
```

Instructions for reproducing preprocessing:
1. Download the dataset from the online repository linked in the supplementary table listing datasets and their corresponding QC outcomes.
2. Find the .sh script titled 'preprocess_{dataset_name}.sh' for the corresponding dataset. Download a Singularity image for the appropriate RABIES version (version 0.4.7 for datasets included in part 2, 0.3.3 for other datasets) (see instructions https://rabies.readthedocs.io/en/stable/installation.html). Provide the script with appropriate paths for the Singularity image (the .sif file), the input BIDS folder (the /nii_inputs:ro path), and the desired output folder (the /rabies_out path).
2.5 For rat preprocessing, the Fischer 344 atlas (https://www.nearlab.xyz/fischer344atlas) must be downloaded and provided as input atlas. The script should be modified according to provide the appropriate path to the atlas folder and each specific associated file (see .sh scripts).
3. Execute the .sh script with appropriate computational resources. If memory is overloaded, consider modulate the --local_threads option (https://rabies.readthedocs.io/en/stable/running_the_software.html)
4. Preprocessing is non-deterministic, thus the quality control results may change slightly. For further steps, the quality control of registration must be carried out again by inspecting the outputs in the newly-generated preprocess_QC_report folder. 
