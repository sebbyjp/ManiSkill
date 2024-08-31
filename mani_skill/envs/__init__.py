from gymnasium.envs.registration import register

register(
    id='ManiSkill-v0',
    entry_point='mani_skill.envs:YourCorrectEnvClass',  # Replace 'YourCorrectEnvClass' with the actual class name
    max_episode_steps=1000,  # Adjust as needed
)
from .tasks import *
