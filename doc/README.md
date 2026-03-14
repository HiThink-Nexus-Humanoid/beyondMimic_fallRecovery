```bash
# fall_recovery 指令

python scripts/csv_to_npz.py --input_file scripts/data/fall_recovery.csv --input_fps 1  --output_fps 50 --output_name fall_recovery_traj --headless

python scripts/replay_npz.py --registry_name=htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj


# 训练
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj  --logger wandb --log_project_name motion-fall_recovery_traj --run_name fall_recovery_track1 --num_envs=4096 --headless

# 播放动作
python scripts/rsl_rl/play.py --task=Tracking-Flat-THS-v0 --num_envs=4 --wandb_path=htzhouhit-ths/motion-fall_recovery_traj/wde32g5i
```







```bash
python scripts/csv_to_npz.py --input_file scripts/data/0007_Walking001_stageii.csv --input_fps 30 --output_name walking --headless


python scripts/csv_to_npz.py --input_file scripts/data/0005_Jogging001_stageii.csv --input_fps 30 --output_name jogging --headless

python scripts/csv_to_npz.py --input_file scripts/data/fall_recovery.csv --input_fps 1  --output_fps 1 --output_name fall_recovery --headless

python scripts/csv_to_npz.py --input_file scripts/data/fall_recovery.csv --input_fps 1  --output_fps 50 --output_name fall_recovery_traj --headless
```


```bash
python scripts/replay_npz.py --registry_name=htzhouhit-ths-org/wandb-registry-motions/fall_recovery


python scripts/replay_npz.py --registry_name=htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj
```


### 训练
```bash
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking \
--headless --logger wandb --log_project_name motion_walk --run_name walk

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking --logger wandb --log_project_name motion_walk --run_name walk

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking \
--headless --logger wandb --log_project_name motion_walk --run_name walk --num_envs=4096



python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery \
--headless --logger wandb --log_project_name motion-fall_recovery --run_name fall_recovery2 --num_envs=4096

python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery --logger wandb --log_project_name motion-fall_recovery --run_name fall_recovery --num_envs=4096




python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj_fast
 --logger wandb --log_project_name motion-fall_recovery_traj_fast --run_name fall_recovery_track3 --num_envs=4096 --headless

# 0312 
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj  --logger wandb --log_project_name motion-fall_recovery_traj_fast --run_name fall_recovery_track4 --num_envs=4096 --headless

# 0313
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery_traj  --logger wandb --log_project_name motion-fall_recovery_traj_fast --run_name fall_recovery_track7 --num_envs=4096 --headless


##########################################
# 重新训练指令如下：
python scripts/rsl_rl/train.py \
  --task=Tracking-Flat-THS-v0 \
  --registry_name htzhouhit-ths-org/wandb-registry-motions/fall_recovery \
  --logger wandb \
  --log_project_name motion-fall_recovery_traj_fast \
  --run_name fall_recovery_track0 \
  --num_envs=4096 \
  --resume=True \
  --load_run fall_recovery_track0 \
  --checkpoint last
  --load_run参数值:

# 需要填写你之前训练的运行目录名称
# 默认情况下，运行目录格式为{时间戳}_{run_name}
# 例如：2023-10-15_14-30-00_fall_recovery_track0
# 你可以在logs/rsl_rl/fall_recovery目录下查找
# --checkpoint参数选项:

# last: 加载最新的检查点（推荐）
# 具体检查点编号：如600（对应你训练到的步数）
# best: 加载性能最好的检查点
# 检查点保存位置:

# 检查点默认保存在logs/rsl_rl/fall_recovery/{时间戳}_{run_name}/checkpoints/目录
# 从你提供的配置可知save_interval = 50，意味着每50次迭代保存一次
# W&B同步:

# 当使用W&B时，训练会自动连接到之前的运行
# 确保--log_project_name与之前一致，以便在W&B中继续记录
```


### 播放
```bash
python scripts/rsl_rl/play.py --task=Tracking-Flat-THS-v0 --num_envs=2 --wandb_path={wandb-run-path}   ###在网页上复制

python scripts/rsl_rl/play.py --task=Tracking-Flat-THS-v0 --num_envs=4096 --wandb_path=htzhouhit-ths/motion-fall_recovery_traj_fast/afv6xptw
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