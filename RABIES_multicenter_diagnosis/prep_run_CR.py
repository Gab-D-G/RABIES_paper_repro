
dataset_dict={}

dataset='7_Cryo_aw_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_aw_f_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=260
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR1']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_24 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'


dataset='7_Cryo_med_f1'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_med_f1_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=266
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,400'
dataset_dict[dataset]['optimized_CR1']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'


dataset='7_Cryo_med_f2'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_med_f2_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=200
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,300'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'


dataset='7_Cryo_med_f3'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_med_f3_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=266
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR1']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --scale_variance_voxelwise'


dataset='7_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_7_Cryo_mediso_v_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=666
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=5
dataset_dict[dataset]['timeseries_interval']=None


dataset='7_RT_halo_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=266
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'


dataset='7_RT_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=100
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None

dataset='7_RT_med_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=333
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,500'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--scale_variance_voxelwise --highpass 0.01 --edge_cutoff 30'

dataset='47_RT_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=196
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None


dataset='94_Cryo_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=260
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR1']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
'
dataset_dict[dataset]['optimized_CR5']=f'--conf_list mot_24 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
'
dataset_dict[dataset]['optimized_CR6']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--scale_variance_voxelwise'
dataset_dict[dataset]['optimized_CR7']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=20,random_seed=1 --scale_variance_voxelwise'


dataset='94_Cryo_med_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=266
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,400'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_24 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'
dataset_dict[dataset]['optimized_CR5']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--ica_aroma apply=true,dim=0,random_seed=1 --scale_variance_voxelwise'


dataset='94_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=240
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
'
dataset_dict[dataset]['optimized_CR5']=f'--conf_list mot_24 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
'
dataset_dict[dataset]['optimized_CR6']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--scale_variance_voxelwise'


dataset='94_RT_iso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=266
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_24 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'


dataset='94_RT_mediso_f1'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=100
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None

dataset='94_RT_mediso_f2'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=400
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,600'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_24 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR6']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=20,random_seed=1'
dataset_dict[dataset]['optimized_CR7']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --scale_variance_voxelwise'


dataset='117_Cryo_iso_f'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=300
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']='5,450'
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_6 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=0,random_seed=1'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30'
dataset_dict[dataset]['optimized_CR6']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --scale_variance_voxelwise'
dataset_dict[dataset]['optimized_CR7']=f'--conf_list mot_6 aCompCor_5 WM_signal CSF_signal --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=false,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--highpass 0.01 --edge_cutoff 30 --ica_aroma apply=true,dim=20,random_seed=1 --scale_variance_voxelwise'


dataset='117_Cryo_mediso_v'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']=f'/scratch/m/mchakrav/desgab/data_preprocess/multicenter/rabies_{dataset}_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=400
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None


dataset='bids_grandjean_rest_awk_bold_only_subset_mediso'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/rabies_bids_grandjean_rest_awk_bold_only_subset_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=120
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None


dataset='bids_grandjean_rest_awk_bold_only_subset_awake'
dataset_dict[dataset]={}
dataset_dict[dataset]['rabies_out']='/scratch/m/mchakrav/desgab/data_preprocess/rabies_bids_grandjean_rest_awk_bold_only_subset_20221024'
dataset_dict[dataset]['FD_threshold']=0.05
dataset_dict[dataset]['min_timepoint']=120
dataset_dict[dataset]['tDOF_matching']=False
dataset_dict[dataset]['local_threads']=20
dataset_dict[dataset]['timeseries_interval']=None
dataset_dict[dataset]['optimized_CR2']=f'--conf_list mot_24 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]}'
dataset_dict[dataset]['optimized_CR3']=f'--conf_list mot_24 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--scale_variance_voxelwise'
dataset_dict[dataset]['optimized_CR4']=f'--conf_list mot_24 aCompCor_5 --image_scaling grand_mean_scaling \
--frame_censoring FD_censoring=true,FD_threshold={dataset_dict[dataset]["FD_threshold"]},DVARS_censoring=true,minimum_timepoint={dataset_dict[dataset]["min_timepoint"]} \
--scale_variance_voxelwise'


for dataset in list(dataset_dict.keys()):

    diagnosis_out=f'/scratch/m/mchakrav/desgab/multicenter_diagnosis/{dataset}'
    rabies_out = dataset_dict[dataset]['rabies_out']
    local_threads = dataset_dict[dataset]['local_threads']
    min_timepoint = dataset_dict[dataset]['min_timepoint']
    FD_threshold = dataset_dict[dataset]['FD_threshold']
    timeseries_interval = dataset_dict[dataset]['timeseries_interval']

    run_CR_call=f'''#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab
'''
    for conf_dir,conf_str in zip(
        ['raw', 'FD', 'mot6_FD', 'mot6_FD_standard', 'mot6_FD_DVARS', 'mot6_FD_WM_CSF', 'mot6_FD_aCompCor5', 'mot24_FD', 'mot6_FD_global', 'mot6_FD_highpass', 'mot6_FD_AROMA'],
        [
        f'--image_scaling grand_mean_scaling',
        f'--image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint} --scale_variance_voxelwise',
        f'--conf_list mot_6 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=true,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 WM_signal CSF_signal --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 aCompCor_5 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_24 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 global_signal --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint}',
        f'--conf_list mot_6 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint} --highpass 0.01 --edge_cutoff 30',
        f'--conf_list mot_6 --image_scaling grand_mean_scaling --frame_censoring FD_censoring=true,FD_threshold={FD_threshold},DVARS_censoring=false,minimum_timepoint={min_timepoint} --ica_aroma apply=true,dim=0,random_seed=1',
        ]):

        singularity_command=f'''

mkdir -p {diagnosis_out}/{conf_dir}
rm {diagnosis_out}/{conf_dir}/rabies_confound_correction.pkl
rm -r {diagnosis_out}/{conf_dir}/confound_correction_datasink

singularity run -B {rabies_out}:/rabies_out -B {diagnosis_out}/{conf_dir}:/diagnosis_out \
/home/m/mchakrav/desgab/singularity_images/rabies-0.5.0-dev.sif -p MultiProc --figure_format svg --local_threads {local_threads} confound_correction /rabies_out /diagnosis_out --read_datasink \
--smoothing_filter 0.3 '''

        singularity_command+=conf_str

        if '--frame_censoring' in conf_str:
            if dataset_dict[dataset]['tDOF_matching']:
                singularity_command+=' --match_number_timepoints'

        if not timeseries_interval is None:
            singularity_command+=f' --timeseries_interval {timeseries_interval}'

        run_CR_call+=singularity_command

    text_file = open(f"{dataset}/run_CR.sh", "wt")
    n = text_file.write(run_CR_call)
    text_file.close()


for dataset in list(dataset_dict.keys()):

    diagnosis_out=f'/scratch/m/mchakrav/desgab/multicenter_diagnosis/{dataset}'
    rabies_out = dataset_dict[dataset]['rabies_out']
    local_threads = dataset_dict[dataset]['local_threads']
    min_timepoint = dataset_dict[dataset]['min_timepoint']
    FD_threshold = dataset_dict[dataset]['FD_threshold']
    timeseries_interval = dataset_dict[dataset]['timeseries_interval']

    for conf_dir in ['optimized_CR1', 'optimized_CR2', 'optimized_CR3', 'optimized_CR4', 'optimized_CR5', 'optimized_CR6', 'optimized_CR7']:
        try:
            conf_str = dataset_dict[dataset][conf_dir]
        except:
            continue

        run_CR_call=f'''#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --nodes=1
#SBATCH --account=rrg-mchakrav-ab'''

        singularity_command=f'''

mkdir -p {diagnosis_out}/{conf_dir}
rm {diagnosis_out}/{conf_dir}/rabies_confound_correction.pkl
rm -r {diagnosis_out}/{conf_dir}/confound_correction_datasink

singularity run -B {rabies_out}:/rabies_out -B {diagnosis_out}/{conf_dir}:/diagnosis_out \
/home/m/mchakrav/desgab/singularity_images/rabies-0.5.0-dev.sif -p MultiProc --figure_format svg --local_threads {local_threads} confound_correction /rabies_out /diagnosis_out --read_datasink \
--smoothing_filter 0.3 '''

        singularity_command+=conf_str

        if '--frame_censoring' in conf_str:
            if dataset_dict[dataset]['tDOF_matching']:
                singularity_command+=' --match_number_timepoints'

        if not timeseries_interval is None:
            singularity_command+=f' --timeseries_interval {timeseries_interval}'

        run_CR_call+=singularity_command

        text_file = open(f"{dataset}/run_{conf_dir}.sh", "wt")
        n = text_file.write(run_CR_call)
        text_file.close()
