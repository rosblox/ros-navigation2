# Containerized navigation2 packages

ROS2 Navigation Framework and System 

Main repo: https://github.com/ros-planning/navigation2
Documentation: https://navigation.ros.org/index.html


## Usage

On host:
```
./build.sh #Builds and tags Docker image
./run.sh   #Runs Docker image with correct options 
```
    
Inside container:
```
build   #Alias to build colcon_ws as root user
run     #Alias to run ROS package as correct user
```
