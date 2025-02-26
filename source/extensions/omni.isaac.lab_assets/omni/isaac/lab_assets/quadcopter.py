# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the quadcopters"""

from __future__ import annotations

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR

##
# Configuration
##

CRAZYFLIE_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/Crazyflie/cf2x.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=10.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
        copy_from_source=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        joint_pos={
            ".*": 0.0,
        },
        joint_vel={
            "m1_joint": 200.0,
            "m2_joint": -200.0,
            "m3_joint": 200.0,
            "m4_joint": -200.0,
        },
    ),
    actuators={
        "dummy": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            stiffness=0.0,
            damping=0.0,
        ),
    },
)
"""Configuration for the Crazyflie quadcopter."""

OSPREY_CFG = ArticulationCfg(
    prim_path="{ENV_REGEX_NS}/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"/home/shlok/osprey/osprey_train/exts/osprey/osprey/assets/osprey_v1.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=10.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            articulation_enabled=True,
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
        copy_from_source=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.0),
        joint_pos={
            "osprey_arm_base_joint_1": -3.0,
            "osprey_arm_base_joint_2": 0.0,
            "osprey_finger_1_joint": 0.0,
            "osprey_finger_2_joint": 0.0
        },
        joint_vel={
            "osprey_rotor_0_joint": 953.0,
            "osprey_rotor_1_joint": 1078.0,
            "osprey_rotor_2_joint": -1078.0,
            "osprey_rotor_3_joint": -953.0,
        },
    ),
    actuators = {
        "arm_pitch_actuator":ImplicitActuatorCfg(
            joint_names_expr=["osprey_arm_base_joint_1"],
            effort_limit=400.0,
            velocity_limit=100.0,
            stiffness=0.3,
            damping=0.5,
        ),
        "arm_roll_actuator":ImplicitActuatorCfg(
            joint_names_expr=["osprey_arm_base_joint_2"],
            effort_limit=400.0,
            velocity_limit=100.0,
            stiffness=0.1,
            damping=0.1,
        ),
        "finger_1_actuator":ImplicitActuatorCfg(
            joint_names_expr=["osprey_finger_1_joint"],
            effort_limit=400.0,
            velocity_limit=100.0,
            stiffness=0.05,
            damping=0.01,
        ),
        "finger_2_actuator":ImplicitActuatorCfg(
            joint_names_expr=["osprey_finger_2_joint"],
            effort_limit=400.0,
            velocity_limit=100.0,
            stiffness=0.05,
            damping=0.01,
        ),
        "rotor_actuators":ImplicitActuatorCfg(
            joint_names_expr=[".*rotor_.*"],
            stiffness=0.0,
            damping=0.0,
        )
    }
)

# OSPREY_CFG = ArticulationCfg(
#     prim_path="{ENV_REGEX_NS}/Robot",
#     spawn=sim_utils.UsdFileCfg(
#         usd_path=f"/home/shlok/osprey/osprey_train/exts/osprey/osprey/assets/osprey_basic.usd",
#         rigid_props=sim_utils.RigidBodyPropertiesCfg(
#             disable_gravity=False,
#             max_depenetration_velocity=10.0,
#             enable_gyroscopic_forces=True,
#         ),
#         articulation_props=sim_utils.ArticulationRootPropertiesCfg(
#             articulation_enabled=True,
#             enabled_self_collisions=False,
#             solver_position_iteration_count=4,
#             solver_velocity_iteration_count=0,
#             sleep_threshold=0.005,
#             stabilization_threshold=0.001,
#         ),
#         copy_from_source=False,
#     ),
#     init_state=ArticulationCfg.InitialStateCfg(
#         pos=(0.0, 0.0, 1.0),
#         joint_pos={
#             ".*": 0.0,
#         },
#         joint_vel={
#             "osprey_rotor_0_joint": 953.0,
#             "osprey_rotor_1_joint": 1078.0,
#             "osprey_rotor_2_joint": -1078.0,
#             "osprey_rotor_3_joint": -953.0,
#         },
#     ),
#     actuators={
#         "dummy": ImplicitActuatorCfg(
#             joint_names_expr=[".*"],
#             stiffness=0.0,
#             damping=0.0,
#         ),
#     },
#     # actuators = {
#     #     "arm_pitch_actuator":ImplicitActuatorCfg(
#     #         joint_names_expr=["osprey_arm_base_joint_1"],
#     #         effort_limit=400.0,
#     #         velocity_limit=100.0,
#     #         stiffness=0.3,
#     #         damping=0.5,
#     #     ),
#     #     "arm_roll_actuator":ImplicitActuatorCfg(
#     #         joint_names_expr=["osprey_arm_base_joint_2"],
#     #         effort_limit=400.0,
#     #         velocity_limit=100.0,
#     #         stiffness=0.1,
#     #         damping=0.1,
#     #     ),
#     #     "finger_1_actuator":ImplicitActuatorCfg(
#     #         joint_names_expr=["osprey_finger_1_joint"],
#     #         effort_limit=400.0,
#     #         velocity_limit=100.0,
#     #         stiffness=0.05,
#     #         damping=0.01,
#     #     ),
#     #     "finger_2_actuator":ImplicitActuatorCfg(
#     #         joint_names_expr=["osprey_finger_2_joint"],
#     #         effort_limit=400.0,
#     #         velocity_limit=100.0,
#     #         stiffness=0.05,
#     #         damping=0.01,
#     #     ),
#     #     "rotor_actuators":ImplicitActuatorCfg(
#     #         joint_names_expr=[".*rotor_.*"],
#     #         stiffness=0.0,
#     #         damping=0.0,
#     #     )
#     # }
# )