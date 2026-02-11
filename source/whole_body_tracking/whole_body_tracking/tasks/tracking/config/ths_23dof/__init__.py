import gymnasium as gym
# from ..source.whole_body_tracking.whole_body_tracking.tasks.tracking.config.ths_23dof import flat_env_cfg
from . import flat_env_cfg

from . import agents

##
# Register Gym environments.
##

gym.register(
    id="Tracking-Flat-THS-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": flat_env_cfg.ThsFlatEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:ThsFlatPPORunnerCfg",
    },
)

