#!/bin/bash

REPOSITORY_NAME="$(basename "$(dirname -- "$( readlink -f -- "$0"; )")")"

docker run -it --rm \
--network=host \
--ipc=host --pid=host \
--env UID=$(id -u) \
--env GID=$(id -g) \
--volume ./navigation2/nav2_behavior_tree:/colcon_ws/src/navigation2/nav2_behavior_tree \
--volume ./slope_estimation_interfaces:/colcon_ws/src/slope_estimation_interfaces \
ghcr.io/rosblox/${REPOSITORY_NAME}:humble
