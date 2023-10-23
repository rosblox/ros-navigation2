#!/bin/bash

REPOSITORY_NAME="$(basename "$(dirname -- "$( readlink -f -- "$0"; )")")"

docker run -it --rm \
--network=host \
--env ROS_DOMAIN_ID=23 \
--volume ./navigation2/nav2_behavior_tree:/colcon_ws/src/navigation2/nav2_behavior_tree \
--volume ./slope_estimation_interfaces:/colcon_ws/src/slope_estimation_interfaces \
--volume ./winch_control_interfaces:/colcon_ws/src/winch_control_interfaces \
--volume ./nav2_bringup/nav2_bringup_launch.py:/opt/ros/humble/share/nav2_bringup/launch/nav2_bringup_launch.py \
--volume ./nav2_bringup/nav2_params.yaml:/opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml \
--volume ./nav2_bringup/goat_world.yaml:/opt/ros/humble/share/nav2_bringup/maps/goat_world.yaml \
--volume ./nav2_bringup/goat_world_empty.pgm:/opt/ros/humble/share/nav2_bringup/maps/goat_world_empty.pgm \
--volume ./nav2_bringup/navigate_to_pose_w_replanning_rolling_and_recovery.xml:/opt/ros/humble/share/nav2_bt_navigator/behavior_trees/navigate_to_pose_w_replanning_and_recovery.xml \
ghcr.io/rosblox/${REPOSITORY_NAME}:humble

# --ipc=host --pid=host \
# --env UID=$(id -u) \
# --env GID=$(id -g) \