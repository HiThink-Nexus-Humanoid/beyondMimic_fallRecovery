
```bash
python scripts/csv_to_npz.py --input_file scripts/data/0007_Walking001_stageii.csv --input_fps 30 --output_name walking --headless


python scripts/csv_to_npz.py --input_file scripts/data/0005_Jogging001_stageii.csv --input_fps 30 --output_name jogging --headless

python scripts/csv_to_npz.py --input_file scripts/data/fall_recovery.csv --input_fps 1  --output_fps 1 --output_name fall_recovery --headless
```


```bash
python scripts/replay_npz.py --registry_name=htzhouhit-ths-org/wandb-registry-motions/fall_recovery
```


### 训练
```bash
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking \
--headless --logger wandb --log_project_name motion_walk --run_name walk

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking --logger wandb --log_project_name motion_walk --run_name walk

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking \
--headless --logger wandb --log_project_name motion_walk --run_name walk --num_envs=4096



python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery \
--headless --logger wandb --log_project_name motion-fall_recovery --run_name fall_recovery --num_envs=4096

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery --logger wandb --log_project_name motion-fall_recovery --run_name fall_recovery --num_envs=4096

```


### 播放
```bash
python scripts/rsl_rl/play.py --task=Tracking-Flat-THS-v0 --num_envs=2 --wandb_path={wandb-run-path}

python scripts/rsl_rl/play.py --task=Tracking-Flat-THS-v0 --num_envs=2 --wandb_path=htzhouhit-ths/motion_walk/a0bfepu4
```


### wandb
https://wandb.ai/htzhouhit-ths




### ISAACLAB自研人形机器人各刚体定义， 总计30个刚体
Body names in the robot: ['base_link', 'left_hip_pitch_link', 'right_hip_pitch_link', 'torso_link', 'left_hip_roll_link', 
                        'right_hip_roll_link', 'left_shoulder_pitch_link', 'right_shoulder_pitch_link', 'left_hip_yaw_link', 'right_hip_yaw_link', 
                        'left_shoulder_roll_link', 'right_shoulder_roll_link', 'left_knee_link', 'right_knee_link', 'left_shoulder_yaw_link', 
                        'right_shoulder_yaw_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'left_elbow_link', 'right_elbow_link', 
                        'left_ankle_roll_link', 'right_ankle_roll_link', 'left_wrist_roll_link', 'right_wrist_roll_link', 'left_leg_heel_link', 
                        'left_leg_toe_link', 'right_leg_heel_link', 'right_leg_toe_link', 'left_palm_link', 'right_palm_link']


### ISAACLAB自研人形机器人各关节定义， 总计23个关节
self.robot.data.joint_names =  ['left_hip_pitch_joint', 'right_hip_pitch_joint', 'torso_joint', 'left_hip_roll_joint', 'right_hip_roll_joint',    
        'left_shoulder_pitch_joint', 'right_shoulder_pitch_joint', 'left_hip_yaw_joint', 'right_hip_yaw_joint', 'left_shoulder_roll_joint', 'right_shoulder_roll_joint', 'left_knee_joint', 'right_knee_joint', 'left_shoulder_yaw_joint', 'right_shoulder_yaw_joint', 
        'left_ankle_pitch_joint', 'right_ankle_pitch_joint', 'left_elbow_joint', 'right_elbow_joint', 'left_ankle_roll_joint', 
        'right_ankle_roll_joint', 'left_wrist_roll_joint', 'right_wrist_roll_joint']