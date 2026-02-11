
```bash
python scripts/csv_to_npz.py --input_file scripts/data/0007_Walking001_stageii.csv --input_fps 30 --output_name walking --headless
```


```bash
python scripts/replay_npz.py --registry_name=htzhouhit-ths-org/wandb-registry-motions/walking
```


```bash
python scripts/rsl_rl/train.py --task=Tracking-Flat-THS-v0 --registry_name htzhouhit-ths-org/wandb-registry-motions/walking \
--headless --logger wandb --log_project_name motion_walk --run_name walk
```

