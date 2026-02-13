import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

from whole_body_tracking.assets import ASSET_DIR


# THS_ACTION_SCALE = 0.5

THS_23DOF_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # fix_base=False,
        # replace_cylinders_with_capsules=True,
        usd_path=f"{ASSET_DIR}/ths_23dof/usd/ths_23dof.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=4
        ),
        # joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
        #     gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        # ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.2),
        rot=(0,1,0,-1),  # (w,x,y,z) 趴姿
        # rot=(0,1,0,1),  # (w,x,y,z) 躺姿
        # rot=(1,0,0,0),  # (w,x,y,z) 站姿
        joint_pos={      
                    "left_hip_pitch_joint": 0.3,                        
                    "left_hip_roll_joint": 0.0,          
                    "left_hip_yaw_joint": 0.0,           
                    "left_knee_joint": -0.6,             
                    "left_ankle_pitch_joint": -0.3,      
                    "left_ankle_roll_joint": 0.0,        
                    "right_hip_pitch_joint": -0.3,       
                    "right_hip_roll_joint": 0.0,         
                    "right_hip_yaw_joint": 0.0,          
                    "right_knee_joint": 0.6,             
                    "right_ankle_pitch_joint": 0.3,      
                    "right_ankle_roll_joint": 0.0,       
                    "torso_joint": 0.0,                  
                    "left_shoulder_pitch_joint": 0.0,    
                    "left_shoulder_roll_joint": 1.3,     
                    "left_shoulder_yaw_joint": -0.6,     
                    "left_elbow_joint": 0.3,             
                    "left_wrist_roll_joint": 0.0,        
                    "right_shoulder_pitch_joint": 0.0,   
                    "right_shoulder_roll_joint": -1.3,   
                    "right_shoulder_yaw_joint": 0.6,     
                    "right_elbow_joint": -0.3,           
                    "right_wrist_roll_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
        actuators={                                                         
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[    
                ".*_hip_pitch_joint",  
                ".*_hip_roll_joint",                             
                ".*_hip_yaw_joint",   
                ".*_knee_joint",      
            ],
            effort_limit_sim={              
                ".*_hip_pitch_joint":  50.0,                                 
                ".*_hip_roll_joint":   50.0,  
                ".*_hip_yaw_joint":    30.0,  
                ".*_knee_joint":       50.0,  
            },
            velocity_limit_sim={         
                ".*_hip_pitch_joint":  10.0,                                
                ".*_hip_roll_joint":   10.0, 
                ".*_hip_yaw_joint":    10.0, 
                ".*_knee_joint":       10.0, 
            },
            stiffness={                                                 
                ".*_hip_pitch_joint":  100.0,                                
                ".*_hip_roll_joint":   100.0,  
                ".*_hip_yaw_joint":    50.0,  
                ".*_knee_joint":       100.0,  

            },
            damping={                                                    
                ".*_hip_pitch_joint":  3.0,                                 
                ".*_hip_roll_joint":   3.0, 
                ".*_hip_yaw_joint":    2.0, 
                ".*_knee_joint":       3.0, 
            },

        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[                                              
                ".*_ankle_pitch_joint",                                     
                ".*_ankle_roll_joint",                                      
            ],
            effort_limit_sim={                                              
                ".*_ankle_pitch_joint":  15.0,                                
                ".*_ankle_roll_joint":   12.0,                                
            },
            velocity_limit_sim={                                            
                ".*_ankle_pitch_joint":  10.0,                                
                ".*_ankle_roll_joint":   10.0,                                
            },
            stiffness={                                                     
                ".*_ankle_pitch_joint":  30.0,                                 
                ".*_ankle_roll_joint":   20.0,                                
            },
            damping={                                                      
                ".*_ankle_pitch_joint":  1.5,                                 
                ".*_ankle_roll_joint":   1.0,                                 
            },
        ),
        "torso":ImplicitActuatorCfg(                
            joint_names_expr=[                                             
                "torso_joint",                                              
            ],
            effort_limit_sim={                                            
                "torso_joint":           20.0,    
            },
            velocity_limit_sim={                                           
                "torso_joint":           10.0,    
            },
            stiffness={                                                   
                "torso_joint":           20.0,     
            },
            damping={                                                     
                "torso_joint":           1.5,     
            },
        ),
        "arms": ImplicitActuatorCfg(    

            joint_names_expr=[                                             
                ".*_shoulder_pitch_joint",                                  
                ".*_shoulder_roll_joint",       
                ".*_shoulder_yaw_joint",        
                ".*_elbow_joint",               
                ".*_wrist_roll_joint"           
            ],
            effort_limit_sim={                                            
                ".*_shoulder_pitch_joint":  15.0,   
                ".*_shoulder_roll_joint":   12.0,   
                ".*_shoulder_yaw_joint":    12.0,   
                ".*_elbow_joint":           12.0,   
                ".*_wrist_roll_joint":      12.0,
            },
            velocity_limit_sim={                                           
                ".*_shoulder_pitch_joint":  10.0,   
                ".*_shoulder_roll_joint":   10.0,   
                ".*_shoulder_yaw_joint":    10.0,   
                ".*_elbow_joint":           10.0,   
                ".*_wrist_roll_joint":      10.0,
            },
            stiffness={                                                   
                ".*_shoulder_pitch_joint":  15.0,   
                ".*_shoulder_roll_joint":   15.0,   
                ".*_shoulder_yaw_joint":    10.0,   
                ".*_elbow_joint":           10.0,   
                ".*_wrist_roll_joint":      10.0,
            },
            damping={                                                     
                ".*_shoulder_pitch_joint":  1.0, 
                ".*_shoulder_roll_joint":   1.0,   
                ".*_shoulder_yaw_joint":    0.7, 
                ".*_elbow_joint":           0.7, 
                ".*_wrist_roll_joint":      0.7,
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
            # THS_ACTION_SCALE[n] = 0.25 * e[n] / s[n]
            THS_ACTION_SCALE[n] = 0.5