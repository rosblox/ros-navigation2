#/bin/python3

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, SetRemap 

from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    pkg_share = get_package_share_directory('nav2_bringup')


    # Update map file path in params file
    params_file = os.path.join(pkg_share, 'params/nav2_params.yaml')

    param_substitutions = {
        'yaml_filename': os.path.join(pkg_share, 'maps/goat_world.yaml')
        }

    configured_params = RewrittenYaml(
        source_file=params_file,
        root_key='',
        param_rewrites=param_substitutions,
        convert_types=True)


    # Start map server
    lifecycle_nodes = ['map_server']
    map_server_node = Node(
                package='nav2_map_server',
                executable='map_server',
                name='map_server',
                output='screen',
                parameters=[configured_params],
                arguments=['--ros-args', '--log-level', 'info'])

    map_server_lifecycle_node = Node(
                package='nav2_lifecycle_manager',
                executable='lifecycle_manager',
                name='lifecycle_manager_map_server',
                output='screen',
                arguments=['--ros-args', '--log-level', 'info'],
                parameters=[{'use_sim_time': False},
                            {'autostart': True},
                            {'node_names': lifecycle_nodes}])


    # # Start navigation
    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    nav2_container_node =  Node(
            name='nav2_container',
            package='rclcpp_components',
            executable='component_container_isolated',
            parameters=[configured_params, {'autostart': True}],
            remappings=remappings,
            output='screen')

    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')

    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_nav2_bringup, 'launch/navigation_launch.py')),
        launch_arguments={'params_file': params_file, 
                          'use_composition': 'True'}.items(),
    )

    # pkg_nav2_bringup = get_package_share_directory('nav2_bringup')

    # navigation_include = GroupAction(
    #     actions=[
    #         SetRemap(src='/cmd_vel', dst='/diff_drive_controller/cmd_vel_unstamped'),

    #         Node(
    #             name='nav2_container',
    #             package='rclcpp_components',
    #             executable='component_container_isolated',
    #             parameters=[configured_params, {'autostart': True}],
    #             output='screen'),


    #         IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource(pkg_nav2_bringup + '/launch/navigation_launch.py'),
    #             launch_arguments = {
    #                 'params_file': [configured_params],
    #                 'use_composition': 'True'
    #             }.items(),
    #         )
    #     ]
    # )

    return LaunchDescription(
        [
            map_server_node,
            map_server_lifecycle_node,
            nav2_container_node,
            nav2_bringup_launch
        ]
    )


