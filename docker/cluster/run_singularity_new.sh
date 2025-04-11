#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# load variables to set the Isaac Lab path on the cluster
source $SCRIPT_DIR/.env.cluster
source $SCRIPT_DIR/../.env.base

# make sure logs directory exists (in the permanent isaaclab directory)
mkdir -p "$CLUSTER_ISAACLAB_DIR/logs"
touch "$CLUSTER_ISAACLAB_DIR/logs/.keep"

# change wandb api key, bad practice but it works!
singularity exec \
    -B /tudelft.net/staff-umbrella/AICUM/osprey/isaac-lab-template.sif/workspace:/workspace:rw \
    --nv --writable --containall /tudelft.net/staff-umbrella/AICUM/osprey/isaac-lab-template.sif \
    bash -c "export ISAACLAB_PATH=/workspace/isaaclab && export WANDB_API_KEY=811275175236a22e47b9b4161ca325cd9be6440c && 
    cd /workspace/isaaclab_extension_template && /isaac-sim/python.sh ./scripts/osprey_hover/skrl_train.py ${@:3}"


if $REMOVE_CODE_COPY_AFTER_JOB; then
    rm -rf $1
fi

echo "(run_singularity.py): Return"
# singularity exec \
#     -B /home/shlok/osprey/IsaacLab/docker/cluster/exports/isaac-lab-template.sif/workspace:/workspace:rw \
#     --nv --writable --containall /home/shlok/osprey/IsaacLab/docker/cluster/exports/isaac-lab-template.sif \
#     bash -c "export ISAACLAB_PATH=/workspace/isaaclab && cd /workspace/isaaclab_extension_template && /isaac-sim/python.sh ./scripts/osprey_hover/skrl_train.py --task=Isaac-OspreyArmControl-v0 --num_envs 1024 --headless"
