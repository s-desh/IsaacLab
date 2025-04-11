#!/bin/sh


# change paths to your local paths

# Function to build IsaacLab base image
build_isaaclab() {
    echo "Building IsaacLab base image"
    cd /home/shlok/osprey/IsaacLab/docker || exit
    ./container.py start
    ./container.py stop
}

# Function to build Osprey Train image
build_osprey_train() {
    echo "Building Osprey Train - IsaacLab extension image"
    cd /home/shlok/osprey/osprey_train/docker || exit
    docker compose --env-file .env.base --file docker-compose.yaml build isaac-lab-template
}

# Function to push image to cluster
push_to_cluster() {
    echo "Pushing image to cluster!"
    cd /home/shlok/osprey/IsaacLab/docker || exit
    ./cluster/cluster_interface.sh push template
}

# Function to submit job
submit_job() {
    echo "Submitting job"
    cd /home/shlok/osprey/IsaacLab/docker/cluster || exit
    ./cluster_interface.sh job template --task=Isaac-OspreyArmControl-v0 --num_envs 4096 --headless
}

# Function to sync logs
sync_logs() {
    echo "Syncing logs from DAIC server"
    rsync -rh ssdeshmukh@login.daic.tudelft.nl:/tudelft.net/staff-umbrella/AICUM/osprey/isaac-lab-template.sif/workspace/isaaclab_extension_template/logs ~/osprey/logs/skrl/daic
}

# Display usage information
usage() {
    echo "Usage: $0 {build-isaaclab|build-osprey-train|push-cluster|submit-job|sync-logs}"
    exit 1
}

# Check for arguments
if [ $# -eq 0 ]; then
    usage
fi

# Execute the appropriate function
case "$1" in
    build-isaaclab)
        build_isaaclab
        ;;
    build-osprey-train)
        build_osprey_train
        ;;
    push-cluster)
        push_to_cluster
        ;;
    submit-job)
        submit_job
        ;;
    sync-logs)
        sync_logs
        ;;
    *)
        usage
        ;;
esac


# 11376081
# 11376169
# 11378121
# 11378194
# 11378437
# 11378438
# 11433479
# 11438881
