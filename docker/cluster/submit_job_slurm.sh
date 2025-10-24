#!/usr/bin/env bash

# in the case you need to load specific modules on the cluster, add them here
# e.g., `module load eth_proxy`

# create job script with compute demands
# refer to DAIC documentation for what these params mean. - https://daic.tudelft.nl/docs/manual/job-submission/slurm-basics/
### MODIFY HERE FOR YOUR JOB ###
cat <<EOT > job.sh
#!/bin/bash

#SBATCH -n 1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:a40:1
#SBATCH --qos=medium
#SBATCH --time=20:00:00
#SBATCH --partition=cor,general
#SBATCH --mem-per-cpu=4096
#SBATCH --mail-type=END
#SBATCH --job-name="training-$(date +"%Y-%m-%dT%H:%M")"

previous=$(/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/tail -n '+2') 
# Pass the container profile first to run_singularity.sh, then all arguments intended for the executed script
bash "$1/docker/cluster/run_singularity_new.sh" "$1" "$2" "${@:3}"
/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/grep -v -F "$previous"

EOT

sbatch < job.sh
rm job.sh
