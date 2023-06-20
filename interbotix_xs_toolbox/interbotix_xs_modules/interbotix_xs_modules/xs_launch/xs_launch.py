# Copyright 2022 Trossen Robotics
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from typing import List, Optional, Text, Union

from launch import LaunchContext, SomeSubstitutionsType
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    EnvironmentVariable,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution,
)
from launch_ros.substitutions import FindPackageShare


class DeclareInterbotixXSArmRobotDescriptionLaunchArgument(DeclareLaunchArgument):
    """Generate a URDF of an Arm through a modified DeclareLaunchArgument object."""

    def __init__(
        self,
        *,
        default_value: Optional[SomeSubstitutionsType] = Command([
            FindExecutable(name='xacro'), ' ',
            PathJoinSubstitution([
                FindPackageShare('interbotix_xsarm_descriptions'),
                'urdf',
                LaunchConfiguration('robot_model')
            ]), '.urdf.xacro ',
            'robot_name:=', LaunchConfiguration('robot_name'), ' ',
            'base_link_frame:=', LaunchConfiguration('base_link_frame'), ' ',
            'use_gripper:=', LaunchConfiguration('use_gripper'), ' ',
            'show_ar_tag:=', LaunchConfiguration('show_ar_tag'), ' ',
            'show_gripper_bar:=', LaunchConfiguration('show_gripper_bar'), ' ',
            'show_gripper_fingers:=', LaunchConfiguration('show_gripper_fingers'), ' ',
            'use_world_frame:=', LaunchConfiguration('use_world_frame'), ' ',
            'external_urdf_loc:=', LaunchConfiguration('external_urdf_loc'), ' ',
            'hardware_type:=', LaunchConfiguration('hardware_type'), ' ',
        ]),
        **kwargs
    ) -> None:
        """
        Construct the modified DeclareLaunchArgument object.

        :param default_value: The default model given to the parent DeclareLaunchArgument; if you
            want to override this value, it must follow the convention in this object's source
        """
        super().__init__(
            name='robot_description',
            default_value=default_value,
            description=(
                'URDF of the robot; this is typically generated by the xacro command.'
            ),
            choices=None,
            **kwargs
        )


class DeclareInterbotixXSCobotRobotDescriptionLaunchArgument(DeclareLaunchArgument):
    """Generate a URDF of an Arm through a modified DeclareLaunchArgument object."""

    def __init__(
        self,
        *,
        default_value: Optional[SomeSubstitutionsType] = Command([
            FindExecutable(name='xacro'), ' ',
            PathJoinSubstitution([
                FindPackageShare('interbotix_xscobot_descriptions'),
                'urdf',
                LaunchConfiguration('robot_model')
            ]), '.urdf.xacro ',
            'robot_name:=', LaunchConfiguration('robot_name'), ' ',
            'base_link_frame:=', LaunchConfiguration('base_link_frame'), ' ',
            'use_gripper:=', LaunchConfiguration('use_gripper'), ' ',
            'show_ar_tag:=', LaunchConfiguration('show_ar_tag'), ' ',
            'show_gripper_bar:=', LaunchConfiguration('show_gripper_bar'), ' ',
            'show_gripper_fingers:=', LaunchConfiguration('show_gripper_fingers'), ' ',
            'use_world_frame:=', LaunchConfiguration('use_world_frame'), ' ',
            'external_urdf_loc:=', LaunchConfiguration('external_urdf_loc'), ' ',
            'hardware_type:=', LaunchConfiguration('hardware_type'), ' ',
        ]),
        **kwargs
    ) -> None:
        """
        Construct the modified DeclareLaunchArgument object.

        :param default_value: The default model given to the parent DeclareLaunchArgument; if you
            want to override this value, it must follow the convention in this object's source
        """
        super().__init__(
            name='robot_description',
            default_value=default_value,
            description=(
                'URDF of the robot; this is typically generated by the xacro command.'
            ),
            choices=None,
            **kwargs
        )



class DeclareInterbotixXSLoCoBotRobotDescriptionLaunchArgument(DeclareLaunchArgument):
    """Generate a URDF of a LoCoBot through a modified DeclareLaunchArgument object."""

    def __init__(
        self,
        *,
        default_value: Optional[SomeSubstitutionsType] = Command([
            FindExecutable(name='xacro'), ' ',
            PathJoinSubstitution([
                FindPackageShare('interbotix_xslocobot_descriptions'),
                'urdf',
                'locobot.urdf.xacro'
            ]), ' ',
            'arm_model:=', LaunchConfiguration('arm_model'), ' ',
            'robot_name:=', LaunchConfiguration('robot_name'), ' ',
            'base_model:=', LaunchConfiguration('base_type'), ' ',
            'robot_model:=', LaunchConfiguration('robot_model'), ' ',
            'robot_name:=', LaunchConfiguration('robot_name'), ' ',
            'use_gripper:=', LaunchConfiguration('use_gripper'), ' ',
            'show_ar_tag:=', LaunchConfiguration('show_ar_tag'), ' ',
            'show_gripper_bar:=', LaunchConfiguration('show_gripper_bar'), ' ',
            'show_gripper_fingers:=', LaunchConfiguration('show_gripper_fingers'), ' ',
            'use_lidar:=', LaunchConfiguration('use_lidar'), ' ',
            'external_urdf_loc:=', LaunchConfiguration('external_urdf_loc'), ' ',
            'hardware_type:=', LaunchConfiguration('hardware_type'), ' ',
        ]),
        **kwargs
    ) -> None:
        """
        Construct the modified DeclareLaunchArgument object.

        :param default_value: The default model given to the parent DeclareLaunchArgument; if you
            want to override this value, it must follow the convention in this object's source
        """
        super().__init__(
            name='robot_description',
            default_value=default_value,
            description=(
                'URDF of the robot; this is typically generated by the xacro command.'
            ),
            choices=None,
            **kwargs
        )


def construct_interbotix_xsarm_semantic_robot_description_command(
    robot_model: str,
    config_path: Union[PathJoinSubstitution, str],
) -> Command:
    """
    Construct the Arm semantic robot description required by MoveIt.

    :param robot_model: The performed robot_model LaunchConfiguration
    :param config_path: The absolute path to the parent directory of the directory containing the
        srdf
    :return: A launch.substitutions.Command containing info to build the srdf

    :details: The LaunchConfigurations used in this method must already have been declared. This
        can be done by using the declare_interbotix_xsarm_robot_description_launch_arguments method
        to declare the robot_description launch args.
    """
    return Command([
        PathJoinSubstitution([
            FindExecutable(name='xacro')
        ]),
        ' ',
        config_path,
        f'/srdf/{robot_model}.srdf.xacro', ' ',
        'robot_name:=', LaunchConfiguration('robot_name'), ' ',
        'base_link_frame:=', LaunchConfiguration('base_link_frame'), ' ',
        'use_gripper:=', LaunchConfiguration('use_gripper'), ' ',
        'show_ar_tag:=', LaunchConfiguration('show_ar_tag'), ' ',
        'show_gripper_bar:=', LaunchConfiguration('show_gripper_bar'), ' ',
        'show_gripper_fingers:=', LaunchConfiguration('show_gripper_fingers'), ' ',
        'use_world_frame:=', LaunchConfiguration('use_world_frame'), ' ',
        'external_urdf_loc:=', LaunchConfiguration('external_urdf_loc'), ' ',
        'external_srdf_loc:=', LaunchConfiguration('external_srdf_loc'), ' ',
        'hardware_type:=', LaunchConfiguration('hardware_type'), ' ',
    ])

def construct_interbotix_xscobot_semantic_robot_description_command(
    robot_model: str,
    config_path: Union[PathJoinSubstitution, str],
) -> Command:
    """
    Construct the Arm semantic robot description required by MoveIt.

    :param robot_model: The performed robot_model LaunchConfiguration
    :param config_path: The absolute path to the parent directory of the directory containing the
        srdf
    :return: A launch.substitutions.Command containing info to build the srdf

    :details: The LaunchConfigurations used in this method must already have been declared. This
        can be done by using the declare_interbotix_xsarm_robot_description_launch_arguments method
        to declare the robot_description launch args.
    """
    return Command([
        PathJoinSubstitution([
            FindExecutable(name='xacro')
        ]),
        ' ',
        config_path,
        f'/srdf/{robot_model}.srdf.xacro', ' ',
        'robot_name:=', LaunchConfiguration('robot_name'), ' ',
        'base_link_frame:=', LaunchConfiguration('base_link_frame'), ' ',
        'use_gripper:=', LaunchConfiguration('use_gripper'), ' ',
        'show_ar_tag:=', LaunchConfiguration('show_ar_tag'), ' ',
        'show_gripper_bar:=', LaunchConfiguration('show_gripper_bar'), ' ',
        'show_gripper_fingers:=', LaunchConfiguration('show_gripper_fingers'), ' ',
        'use_world_frame:=', LaunchConfiguration('use_world_frame'), ' ',
        'external_urdf_loc:=', LaunchConfiguration('external_urdf_loc'), ' ',
        'external_srdf_loc:=', LaunchConfiguration('external_srdf_loc'), ' ',
        'hardware_type:=', LaunchConfiguration('hardware_type'), ' ',
    ])


def construct_interbotix_xslocobot_semantic_robot_description_command(
    robot_model: str,
    config_path: Union[PathJoinSubstitution, str],
) -> Command:
    """
    Construct the LoCoBot semantic robot description required by MoveIt.

    :param robot_model: The performed robot_model LaunchConfiguration
    :param config_path: The absolute path to the parent directory of the directory containing the
        srdf
    :return: A launch.substitutions.Command containing info to build the srdf

    :details: The LaunchConfigurations used in this method must already have been declared. This
        can be done by using the declare_interbotix_xslocobot_robot_description_launch_arguments
        method to declare the robot_description launch args.
    """
    return Command([
        PathJoinSubstitution([
            FindExecutable(name='xacro')
        ]),
        ' ',
        config_path,
        f'/srdf/{robot_model}.srdf.xacro', ' ',
        'robot_name:=', LaunchConfiguration('robot_name'), ' ',
        'use_lidar:=', LaunchConfiguration('use_lidar'), ' ',
        'base_type:=', LaunchConfiguration('base_type'), ' ',
        'external_srdf_loc:=', LaunchConfiguration('external_srdf_loc'), ' ',
    ])


def declare_interbotix_xsarm_robot_description_launch_arguments(
    *,
    base_link_frame: Text = 'base_link',
    use_gripper: Text = 'true',
    show_ar_tag: Text = 'false',
    show_gripper_bar: Text = 'true',
    show_gripper_fingers: Text = 'true',
    use_world_frame: Text = 'true',
    external_urdf_loc: Text = '',
    hardware_type: Text = 'actual',
) -> List[DeclareLaunchArgument]:
    """
    Return the `robot_description` DeclareLaunchArgument and its required children.

    DeclareLaunchArgument objects:
        - `base_link_frame`
        - `use_gripper`
        - `show_ar_tag`
        - `show_gripper_bar`
        - `show_gripper_fingers`
        - `use_world_frame`
        - `external_urdf_loc`
        - `hardware_type`

    :details: Include this in your LaunchDescription by appending its output to the list of
        DeclareLaunchArguments
    """
    return [
        DeclareLaunchArgument(
            'base_link_frame',
            default_value=TextSubstitution(text=base_link_frame),
            description=(
                "name of the 'root' link on the arm; typically `base_link`, but can be changed if "
                'attaching the arm to a mobile base that already has a `base_link` frame.'
            ),
        ),
        DeclareLaunchArgument(
            'use_gripper',
            default_value=TextSubstitution(text=use_gripper),
            choices=('true', 'false'),
            description=(
                'if `true`, the default gripper is included in the `robot_description`; '
                'if `false`, it is left out; set to `false` if not using the default gripper.'
            ),
        ),
        DeclareLaunchArgument(
            'show_ar_tag',
            default_value=show_ar_tag,
            choices=('true', 'false'),
            description=(
                'if `true`, the AR tag mount is included in the `robot_description`; if '
                '`false`, it is left out; set to `true` if using the AR tag mount in your project.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_bar',
            default_value=show_gripper_bar,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper_bar link is included in the `robot_description`;'
                ' if `false`, the gripper_bar and finger links are not loaded. Set to `false` if '
                'you have a custom gripper attachment.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_fingers',
            default_value=show_gripper_fingers,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper fingers are included in the `robot_description`; '
                'if `false`, the gripper finger links are not loaded. Set to `false` if you have '
                'custom gripper fingers.'
            ),
        ),
        DeclareLaunchArgument(
            'use_world_frame',
            default_value=use_world_frame,
            choices=('true', 'false'),
            description=(
                "set this to `true` if you would like to load a 'world' frame to the "
                "`robot_description` which is located exactly at the 'base_link' frame "
                'of the robot; if using multiple robots or if you would like to attach the '
                "'base_link' frame of the robot to a different frame, set this to `false`."
            ),
        ),
        DeclareLaunchArgument(
            'external_urdf_loc',
            default_value=TextSubstitution(text=external_urdf_loc),
            description=(
                'the file path to the custom urdf.xacro file that you would like to include in the'
                " Interbotix robot's urdf.xacro file."
            ),
        ),
        DeclareLaunchArgument(
            'hardware_type',
            choices=(
                'actual',
                'fake',
                'gz_classic',
            ),
            default_value=hardware_type,
            description=(
                'configures the `robot_description` to use the actual hardware, fake '
                'hardware, or hardware simulated in Gazebo.'
            ),
        ),
        DeclareInterbotixXSArmRobotDescriptionLaunchArgument(),
    ]


def declare_interbotix_xscobot_robot_description_launch_arguments(
    *,
    base_link_frame: Text = 'base_link',
    use_gripper: Text = 'true',
    show_ar_tag: Text = 'false',
    show_gripper_bar: Text = 'true',
    show_gripper_fingers: Text = 'true',
    use_world_frame: Text = 'true',
    external_urdf_loc: Text = '',
    hardware_type: Text = 'actual',
) -> List[DeclareLaunchArgument]:
    """
    Return the `robot_description` DeclareLaunchArgument and its required children.

    DeclareLaunchArgument objects:
        - `base_link_frame`
        - `use_gripper`
        - `show_ar_tag`
        - `show_gripper_bar`
        - `show_gripper_fingers`
        - `use_world_frame`
        - `external_urdf_loc`
        - `hardware_type`

    :details: Include this in your LaunchDescription by appending its output to the list of
        DeclareLaunchArguments
    """
    return [
        DeclareLaunchArgument(
            'base_link_frame',
            default_value=TextSubstitution(text=base_link_frame),
            description=(
                "name of the 'root' link on the arm; typically `base_link`, but can be changed if "
                'attaching the arm to a mobile base that already has a `base_link` frame.'
            ),
        ),
        DeclareLaunchArgument(
            'use_gripper',
            default_value=TextSubstitution(text=use_gripper),
            choices=('true', 'false'),
            description=(
                'if `true`, the default gripper is included in the `robot_description`; '
                'if `false`, it is left out; set to `false` if not using the default gripper.'
            ),
        ),
        DeclareLaunchArgument(
            'show_ar_tag',
            default_value=show_ar_tag,
            choices=('true', 'false'),
            description=(
                'if `true`, the AR tag mount is included in the `robot_description`; if '
                '`false`, it is left out; set to `true` if using the AR tag mount in your project.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_bar',
            default_value=show_gripper_bar,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper_bar link is included in the `robot_description`;'
                ' if `false`, the gripper_bar and finger links are not loaded. Set to `false` if '
                'you have a custom gripper attachment.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_fingers',
            default_value=show_gripper_fingers,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper fingers are included in the `robot_description`; '
                'if `false`, the gripper finger links are not loaded. Set to `false` if you have '
                'custom gripper fingers.'
            ),
        ),
        DeclareLaunchArgument(
            'use_world_frame',
            default_value=use_world_frame,
            choices=('true', 'false'),
            description=(
                "set this to `true` if you would like to load a 'world' frame to the "
                "`robot_description` which is located exactly at the 'base_link' frame "
                'of the robot; if using multiple robots or if you would like to attach the '
                "'base_link' frame of the robot to a different frame, set this to `false`."
            ),
        ),
        DeclareLaunchArgument(
            'external_urdf_loc',
            default_value=TextSubstitution(text=external_urdf_loc),
            description=(
                'the file path to the custom urdf.xacro file that you would like to include in the'
                " Interbotix robot's urdf.xacro file."
            ),
        ),
        DeclareLaunchArgument(
            'hardware_type',
            choices=(
                'actual',
                'fake',
                'gz_classic',
            ),
            default_value=hardware_type,
            description=(
                'configures the `robot_description` to use the actual hardware, fake '
                'hardware, or hardware simulated in Gazebo.'
            ),
        ),
        DeclareInterbotixXSCobotRobotDescriptionLaunchArgument(),
    ]




def declare_interbotix_xslocobot_robot_description_launch_arguments(
    *,
    use_gripper: Text = 'true',
    show_ar_tag: Text = 'true',
    show_gripper_bar: Text = 'true',
    show_gripper_fingers: Text = 'true',
    external_urdf_loc: Text = '',
    hardware_type: Text = 'actual',
) -> List[DeclareLaunchArgument]:
    """
    Return the `robot_description` DeclareLaunchArgument and its required children.

    DeclareLaunchArgument objects:
        - `base_type`
        - `use_gripper`
        - `show_ar_tag`
        - `show_gripper_bar`
        - `show_gripper_fingers`
        - `external_urdf_loc`
        - `hardware_type`

    :details: Include this in your LaunchDescription by appending its output to the list of
        DeclareLaunchArguments
    """
    return [
        DeclareLaunchArgument(
            'base_type',
            default_value=EnvironmentVariable('INTERBOTIX_XSLOCOBOT_BASE_TYPE'),
            choices=('kobuki', 'create3'),
            description='the base type of the LoCoBot.',
        ),
        DeclareLaunchArgument(
            'use_gripper',
            default_value=TextSubstitution(text=use_gripper),
            choices=('true', 'false'),
            description=(
                'if `true`, the default gripper is included in the `robot_description`; '
                'if `false`, it is left out; set to `false` if not using the default gripper.'
            ),
        ),
        DeclareLaunchArgument(
            'show_ar_tag',
            default_value=show_ar_tag,
            choices=('true', 'false'),
            description=(
                'if `true`, the AR tag mount is included in the `robot_description`; if '
                '`false`, it is left out; set to `true` if using the AR tag mount in your project.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_bar',
            default_value=show_gripper_bar,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper_bar link is included in the `robot_description`;'
                ' if `false`, the gripper_bar and finger links are not loaded. Set to `false` if '
                'you have a custom gripper attachment.'
            ),
        ),
        DeclareLaunchArgument(
            'show_gripper_fingers',
            default_value=show_gripper_fingers,
            choices=('true', 'false'),
            description=(
                'if `true`, the gripper fingers are included in the `robot_description`; '
                'if `false`, the gripper finger links are not loaded. Set to `false` if you have '
                'custom gripper fingers.'
            ),
        ),
        DeclareLaunchArgument(
            'external_urdf_loc',
            default_value=TextSubstitution(text=external_urdf_loc),
            description=(
                'the file path to the custom urdf.xacro file that you would like to include in the'
                " Interbotix robot's urdf.xacro file."
            ),
        ),
        DeclareLaunchArgument(
            'hardware_type',
            choices=(
                'actual',
                'fake',
                'gz_classic',
            ),
            default_value=hardware_type,
            description=(
                'configures the `robot_description` to use the actual hardware, fake '
                'hardware, or hardware simulated in Gazebo.'
            ),
        ),
        DeclareInterbotixXSLoCoBotRobotDescriptionLaunchArgument(),
    ]


def determine_use_sim_time_param(
    context: LaunchContext,
    hardware_type_launch_arg: LaunchConfiguration
) -> Union[TextSubstitution, LaunchConfiguration]:
    """
    Set `use_sim_time` parameter to `true` if using simulated hardware.

    :param context: The launch context
    :param hardware_type: The `hardware_type` LaunchConfiguration
    :return: True if hardware is simulated, the `use_sim_time` LaunchConfiguration otherwise
    """
    if hardware_type_launch_arg.perform(context) in ('gz_classic'):
        return TextSubstitution(text='true')
    else:
        return LaunchConfiguration('use_sim_time')
