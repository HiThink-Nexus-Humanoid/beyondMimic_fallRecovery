

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from whole_body_tracking.assets import ASSET_DIR


# 定义一个名为 THS_23DOF 的关节体（Articulation）配置对象
THS_23DOF_CFG = ArticulationCfg(                                         
    spawn=sim_utils.UsdFileCfg(                                     # 配置生成方式：从 USD 文件加载模型
        usd_path=f"{ASSET_DIR}/ths_23dof/usd/ths_23dof.usd",  # USD 模型文件的完整路径，使用 ISAAC_ASSET_DIR 环境变量拼接
        activate_contact_sensors=True,                              # 激活接触传感器，用于检测碰撞接触信息
        # 刚体物理属性配置
        rigid_props=sim_utils.RigidBodyPropertiesCfg(               
            disable_gravity=False,                                  # 不禁用重力，物体受重力影响
            retain_accelerations=False,                             # 不保留加速度缓存，节省内存
            linear_damping=0.0,                                     # 线性阻尼为 0，运动不受线性阻力衰减
            angular_damping=0.0,                                    # 角阻尼为 0，旋转不受阻力衰减
            max_linear_velocity=1000.0,                             # 最大线速度限制为 1000.0 m/s
            max_angular_velocity=1000.0,                            # 最大角速度限制为 1000.0 rad/s
            max_depenetration_velocity=1.0,                         # 最大脱离穿透速度设为 1.0，防止碰撞解决过快
        ),
        # 关节体根节点属性配置
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(  
            enabled_self_collisions= False,                          # 禁用自碰撞检测，关节体各部分不会相互碰撞
            solver_position_iteration_count=8,                      # 位置求解器迭代次数为 8，提高位置精度
            solver_velocity_iteration_count=4,                      # 速度求解器迭代次数为 4，提高速度精度 
        ),
    ),
 
    # 定义关节体的初始状态配置
    init_state=ArticulationCfg.InitialStateCfg( 
        pos=(0.0, 0.0, 0.752),                                    # 初始世界坐标位置 (x, y, z)
        # 设置各关节的初始角度（位置），单位为弧度
        joint_pos={      
            "left_hip_pitch_joint": 0.3,                           # 左髋俯仰关节初始角度                        
            "left_hip_roll_joint": 0.0,                            # 左髋横滚关节初始角度
            "left_hip_yaw_joint": 0.0,                             # 左髋偏航关节初始角度
            "left_knee_joint": -0.6,                               # 左膝俯仰关节初始角度 
            "left_ankle_pitch_joint": -0.3,                        # 左脚踝俯仰关节初始角度 
            "left_ankle_roll_joint": 0.0,                          # 左脚踝横滚关节初始角度 
            "right_hip_pitch_joint": -0.3,                         # 右髋俯仰关节初始角度 
            "right_hip_roll_joint": 0.0,                           # 右髋横滚关节初始角度
            "right_hip_yaw_joint": 0.0,                            # 右髋偏航关节初始角度 
            "right_knee_joint": 0.6,                               # 右膝俯仰关节初始角度 
            "right_ankle_pitch_joint": 0.3,                        # 右脚踝俯仰关节初始角度 
            "right_ankle_roll_joint": 0.0,                         # 右脚踝横滚关节初始角度 
            "torso_joint": 0.0,                                     # 躯干(腰部)
            "left_shoulder_pitch_joint": 0.0,                      # 左肩俯仰关节初始角度 
            "left_shoulder_roll_joint": 1.3,                       # 左肩横滚关节初始角度 
            "left_shoulder_yaw_joint": -0.6,                       # 左肩偏航关节初始角度 
            "left_elbow_joint": 0.3,                               # 左肘俯仰关节初始角度 
            "left_wrist_roll_joint": 0.0,                           # 左手腕横滚
            "right_shoulder_pitch_joint": 0.0,                      # 右肩俯仰关节初始角度 
            "right_shoulder_roll_joint": -1.3,                      # 右肩横滚关节初始角度 
            "right_shoulder_yaw_joint": 0.6,                        # 右肩偏航关节初始角度 
            "right_elbow_joint": -0.3,                              # 右肘俯仰关节初始角度
            "right_wrist_roll_joint": 0.0,
        },
        joint_vel={".*": 0.0},                                      # 使用正则表达式 ".*" 匹配所有关节，初始速度设为 0.0（静止启动）
    ),


    soft_joint_pos_limit_factor=0.9,                                      # 关节位置软限制因子设为 0.9，限制范围略小于物理极限以保护仿真稳定
    # 定义驱动器配置字典，用于设置不同关节组的驱动参数
    actuators={                                                         
        "legs": ImplicitActuatorCfg(                            # 为腿部关节组创建隐式驱动器配置
            # 使用正则表达式匹配腿部相关关节名称
            joint_names_expr=[    
                ".*_hip_pitch_joint",                                     # 匹配左右髋俯仰关节 
                ".*_hip_roll_joint",                                      # 匹配左右髋横滚关节                           
                ".*_hip_yaw_joint",                                       # 匹配左右髋偏航关节
                ".*_knee_joint",                                          # 匹配左右膝俯仰关节
            ],
            # 仿真中的力矩限制
            effort_limit_sim={              
                ".*_hip_pitch_joint":  50,                                # 髋俯仰关节                               
                ".*_hip_roll_joint":   50,                                # 髋横滚关节
                ".*_hip_yaw_joint":    30,                                # 髋偏航关节
                ".*_knee_joint":       50,                                # 膝俯仰关节
            },
            # 仿真中的最大速度限制
            velocity_limit_sim={         
                ".*_hip_pitch_joint":  10,                              # 髋俯仰关节                               
                ".*_hip_roll_joint":   10,                              # 髋横滚关节
                ".*_hip_yaw_joint":    10,                              # 髋偏航关节
                ".*_knee_joint":       10,                              # 膝俯仰关节
            },
            
            # 关节刚度系数
            stiffness={                                                 
                ".*_hip_pitch_joint":  0,                             # 俯仰关节                                    
                ".*_hip_roll_joint":   0,                             # 髋横滚关节
                ".*_hip_yaw_joint":    0,                              # 髋偏航关节
                ".*_knee_joint":       0,                             # 关节

            },
            # 关节阻尼系数  
            damping={                                                    
                ".*_hip_pitch_joint":  0.,                               # 髋俯仰关节                                    
                ".*_hip_roll_joint":   0.,                               # 髋横滚关节  
                ".*_hip_yaw_joint":    0.,                             # 髋偏航关节
                ".*_knee_joint":       0.,                               # 膝俯仰关节
            },

        ),
        "feet": ImplicitActuatorCfg(                           # 为脚踝部关节组创建隐式驱动器配置
            # 使用正则表达式匹配脚部相关关节名称
            joint_names_expr=[                                              
                ".*_ankle_pitch_joint",                                     # 匹配左右脚踝俯仰关节
                ".*_ankle_roll_joint",                                      # 匹配左右脚踝横滚关节
            ],
            # 仿真中的力矩 限制
            effort_limit_sim={                                              
                ".*_ankle_pitch_joint":  15,                                # 脚踝俯仰关节
                ".*_ankle_roll_joint":   12,                                # 脚踝横滚关节
            },
            # 仿真中的速度限制
            velocity_limit_sim={                                            
                ".*_ankle_pitch_joint":  10,                                # 脚踝俯仰关节
                ".*_ankle_roll_joint":   10,                                # 脚踝横滚关节
            },
            # 关节刚度系数
            stiffness={                                                     
                ".*_ankle_pitch_joint":  0,                                # 脚踝俯仰关节
                ".*_ankle_roll_joint":   0,                                # 脚踝横滚关节
            },
            # 关节阻尼系数
            damping={                                                      
                ".*_ankle_pitch_joint":  0,                                 # 脚踝俯仰关节
                ".*_ankle_roll_joint":   0,                                # 脚踝横滚关节
            },
        ),
        "torso":ImplicitActuatorCfg(                                 # 为躯干创建隐式驱动器配置   
            # 使用正则表达式匹配手臂相关关节名称                             
            joint_names_expr=[                                             
                "torso_joint",                                               # 匹配腰部偏航关节
            ],
            # 仿真中的力矩限制
            effort_limit_sim={                                            
                "torso_joint":           20,                                 # 躯干腰部关节
            },
            # 仿真中的速度限制
            velocity_limit_sim={                                           
                "torso_joint":           10,                                 # 躯干腰部关节
            },
            # 关节刚度系数
            stiffness={                                                   
                "torso_joint":           0,                                 # 躯干腰部关节
            },
            # 关节阻尼系数
            damping={                                                     
                "torso_joint":           0,                                # 躯干腰部关节
            },
        ),
        "arms": ImplicitActuatorCfg(                               # 为手臂关节组创建隐式驱动器配置   
            # 使用正则表达式匹配手臂相关关节名称                             
            joint_names_expr=[                                             
                ".*_shoulder_pitch_joint",                                  # 匹配左右肩俯仰关节
                ".*_shoulder_roll_joint",                                   # 匹配左右肩横滚关节
                ".*_shoulder_yaw_joint",                                    # 匹配左右肩偏航关节
                ".*_elbow_joint",                                           # 匹配左右肘俯仰关节
                ".*_wrist_roll_joint"                                       # 匹配左右手腕横滚
            ],
            # 仿真中的力矩限制
            effort_limit_sim={                                            
                ".*_shoulder_pitch_joint":  15,                             # 肩俯仰关节
                ".*_shoulder_roll_joint":   12,                             # 肩横滚关节
                ".*_shoulder_yaw_joint":    12,                             # 肩偏航关节
                ".*_elbow_joint":           12,                             # 肘俯仰关节
                ".*_wrist_roll_joint":      12,
            },
            # 仿真中的速度限制
            velocity_limit_sim={                                           
                ".*_shoulder_pitch_joint":  10,                             # 肩俯仰关节
                ".*_shoulder_roll_joint":   10,                             # 肩横滚关节
                ".*_shoulder_yaw_joint":    10,                             # 肩偏航关节
                ".*_elbow_joint":           10,                             # 肘俯仰关节
                ".*_wrist_roll_joint":      10,
            },
            # 关节刚度系数
            stiffness={                                                   
                ".*_shoulder_pitch_joint":  0,                             # 肩俯仰关节
                ".*_shoulder_roll_joint":   0,                             # 肩横滚关节
                ".*_shoulder_yaw_joint":    0,                             # 肩偏航关节
                ".*_elbow_joint":           0,                             # 肘俯仰关节
                ".*_wrist_roll_joint":      0,
            },
            # 关节阻尼系数
            damping={                                                     
                ".*_shoulder_pitch_joint":  0,                             # 肩俯仰关节 
                ".*_shoulder_roll_joint":   0,                             # 肩横滚关节   
                ".*_shoulder_yaw_joint":    0,                            # 肩偏航关节 
                ".*_elbow_joint":           0,                            # 肘俯仰关节
                ".*_wrist_roll_joint":      0,
            },
        ),

    },
)
THS_ACTION_SCALE = {}
for a in THS_23DOF_CFG.actuators.values():
    e = a.effort_limit_sim
    s = a.stiffness
    names = a.joint_names_expr
    if not isinstance(e, dict):
        e = {n: e for n in names}
    if not isinstance(s, dict):
        s = {n: s for n in names}
    for n in names:
        if n in e and n in s and s[n]:
            THS_ACTION_SCALE[n] = 0.25 * e[n] / s[n]




'''
#----------------------------lab or mujoco/urdf 顺序对照表----------------------------
#  isaac
0'left_hip_pitch_joint', 
1'right_hip_pitch_joint', 
2'torso_joint', 
3'left_hip_roll_joint', 
4'right_hip_roll_joint', 
5'left_shoulder_pitch_joint', 
6'right_shoulder_pitch_joint', 
7'left_hip_yaw_joint', 
8'right_hip_yaw_joint', 
9'left_shoulder_roll_joint', 
10'right_shoulder_roll_joint', 
11'left_knee_joint', 
12'right_knee_joint', 
13'left_shoulder_yaw_joint', 
14'right_shoulder_yaw_joint', 
15'left_ankle_pitch_joint', 
16'right_ankle_pitch_joint', 
17'left_elbow_joint', 
18'right_elbow_joint', 
19'left_ankle_roll_joint', 
20'right_ankle_roll_joint', 
21'left_wrist_roll_joint', 
22'right_wrist_roll_joint'


#  mujoco_idx 
0"left_hip_pitch_joint": 0.3,                           # 左髋俯仰关节初始角度                        
1"left_hip_roll_joint": 0.0,                            # 左髋横滚关节初始角度
2"left_hip_yaw_joint": 0.0,                             # 左髋偏航关节初始角度
3"left_knee_joint": -0.6,                               # 左膝俯仰关节初始角度 
4"left_ankle_pitch_joint": -0.3,                        # 左脚踝俯仰关节初始角度 
5"left_ankle_roll_joint": 0.0,                          # 左脚踝横滚关节初始角度 
6"right_hip_pitch_joint": -0.3,                         # 右髋俯仰关节初始角度 
7"right_hip_roll_joint": 0.0,                           # 右髋横滚关节初始角度
8"right_hip_yaw_joint": 0.0,                            # 右髋偏航关节初始角度 
9"right_knee_joint": 0.6,                               # 右膝俯仰关节初始角度 
10"right_ankle_pitch_joint": 0.3,                        # 右脚踝俯仰关节初始角度 
11"right_ankle_roll_joint": 0.0,                         # 右脚踝横滚关节初始角度 
12"torso_joint": 0.0,                                     # 躯干(腰部)
13"left_shoulder_pitch_joint": 0.0,                      # 左肩俯仰关节初始角度 
14"left_shoulder_roll_joint": 1.3,                       # 左肩横滚关节初始角度 
15"left_shoulder_yaw_joint": -0.6,                       # 左肩偏航关节初始角度 
16"left_elbow_joint": 0.3,                               # 左肘俯仰关节初始角度 
17"left_wrist_roll_joint": 0.0,                           # 左手腕横滚
18"right_shoulder_pitch_joint": 0.0,                      # 右肩俯仰关节初始角度 
19"right_shoulder_roll_joint": -1.3,                      # 右肩横滚关节初始角度 
20"right_shoulder_yaw_joint": 0.6,                        # 右肩偏航关节初始角度 
21"right_elbow_joint": -0.3,                              # 右肘俯仰关节初始角度
22"right_wrist_roll_joint": 0.0,


self.mujoco_to_isaac_idx           = [   
0    0, # left_hip_pitch_joint
1    6, # right_hip_pitch_joint
2    12,# torso_joint 
3    1, # left_hip_roll_joint 
4    7, # right_hip_roll_joint
5    13,# left_shoulder_pitch_joint  
6    18,# right_shoulder_pitch_joint
7    2, # left_hip_yaw_joint   
8    8, # right_hip_yaw_joint 
9    14,# left_shoulder_roll_joint 
10   19,# right_shoulder_roll_joint  
11   3, # left_knee_joint 
12   9, # right_knee_joint
13   15,# left_shoulder_yaw_joint  
14   20,# right_shoulder_yaw_joint
15   4, # left_ankle_pitch_joint
16   10,# right_ankle_pitch_joint 
17   16,# left_elbow_joint 
18   21,# right_elbow_joint
19   5, # left_ankle_roll_joint
20   11,# right_ankle_roll_joint
21   17,# left_wrist_roll_joint
22   22,# right_wrist_roll_joint
]


self.isaac_to_mujoco_idx           = [      
0    0, # left_hip_pitch_joint 
1    3, # left_hip_roll_joint
2    7, # left_hip_yaw_joint
3    11,# left_knee_joint
4    15,# left_ankle_pitch_joint
5    19,# left_ankle_roll_joint
6    1, # right_hip_pitch_joint
7    4, # right_hip_roll_joint
8    8, # right_hip_yaw_joint
9    12,# right_knee_joint
10   16,# right_ankle_pitch_joint
11   20,# right_ankle_roll_joint
12   2, # torso_joint
13   5, # left_shoulder_pitch_joint
14   9, # left_shoulder_roll_joint
15   13,# left_shoulder_yaw_joint
16   17,# left_elbow_joint
17   21,# left_wrist_roll_joint
18   6, # right_shoulder_pitch_joint
19   10,# right_shoulder_roll_joint
20   14,# right_shoulder_yaw_joint
21   18,# right_elbow_joint
22   22,# right_wrist_roll_joint
]






'''
