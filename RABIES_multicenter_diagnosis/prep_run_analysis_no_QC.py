dataset_dict={}
dataset='7_Cryo_aw_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_Cryo_med_f1'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_Cryo_med_f2'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_Cryo_med_f3'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=5
dataset_dict[dataset]['group_spec']='*'

dataset='7_RT_halo_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_RT_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='7_RT_med_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='47_RT_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_Cryo_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_Cryo_med_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_RT_iso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_RT_mediso_f1'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='94_RT_mediso_f2'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='117_Cryo_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset='117_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['group_spec']='*'

dataset_dict['bids_grandjean_rest_awk_bold_only_subset_mediso']={}
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_mediso']['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/rabies_bids_grandjean_rest_awk_bold_only_subset_20221024'
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_mediso']['local_threads']=20
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_mediso']['group_spec']='*MEDISO*'


dataset_dict['bids_grandjean_rest_awk_bold_only_subset_awake']={}
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_awake']['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/rabies_bids_grandjean_rest_awk_bold_only_subset_20221024'
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_awake']['local_threads']=20
dataset_dict['bids_grandjean_rest_awk_bold_only_subset_awake']['group_spec']='*AWc*'


for dataset in list(dataset_dict.keys()):
    diagnosis_out=f'/scratch/m/mchakrav/desgab/multicenter_diagnosis/{dataset}'
    rabies_out = dataset_dict[dataset]['rabies_out']
    local_threads = dataset_dict[dataset]['local_threads']
    group_spec = dataset_dict[dataset]['group_spec']

    scan_QC_str = "--scan_QC_thresholds '{}'"

    run_analysis_call=f'''#!/bin/bash
#SBATCH --time=4:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab

conf_dir=mot6_FD
analysis_out=mot6_FD_no_QC

mkdir -p {diagnosis_out}/$analysis_out
rm {diagnosis_out}/$analysis_out/rabies_analysis.pkl
rm -r {diagnosis_out}/$analysis_out/analysis_datasink
rm -r {diagnosis_out}/$analysis_out/data_diagnosis_datasink

singularity exec -B /scratch/m/mchakrav/desgab/multicenter_diagnosis/:/work_dir \
-B {diagnosis_out}/$conf_dir:/diagnosis_out \
-B {diagnosis_out}/$analysis_out:/new_diagnosis_out \
/home/m/mchakrav/desgab/singularity_images/rabies-0.5.0-dev.sif python /work_dir/prepare_scanlist.py \
/diagnosis_out/confound_correction_datasink/cleaned_timeseries/{group_spec}/{group_spec}cleaned.nii.gz /new_diagnosis_out/scanlist.txt none

singularity run -B {rabies_out}:/rabies_out \
-B {diagnosis_out}/$conf_dir:/diagnosis_out \
-B {diagnosis_out}/$analysis_out:/new_diagnosis_out \
-B /home/m/mchakrav/desgab/atlases:/atlases:ro \
/home/m/mchakrav/desgab/singularity_images/rabies-0.5.0-dev.sif -p MultiProc --figure_format svg --local_threads {local_threads} analysis /diagnosis_out /new_diagnosis_out/ \
--data_diagnosis --scan_list /new_diagnosis_out/scanlist.txt \
--seed_list /atlases/SBC_seeds_DSURQE/AC_seed_EPI_template.nii.gz /atlases/SBC_seeds_DSURQE/S1_seed_EPI_template.nii.gz \
--seed_prior_list /atlases/SBC_seeds_DSURQE/AC_consensus_EPI_template.nii.gz /atlases/SBC_seeds_DSURQE/S1_consensus_EPI_template.nii.gz \
--DR_ICA --prior_maps /home/rabies/.local/share/rabies/melodic_IC_resampled.nii.gz --prior_bold_idx 5 19 {scan_QC_str}

    '''

    text_file = open(f"{dataset}/run_analysis_no_QC.sh", "wt")
    n = text_file.write(run_analysis_call)
    text_file.close()
