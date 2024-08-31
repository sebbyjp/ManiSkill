import gradio as gr
import gymnasium as gym
from mani_skill.envs.sapien_env import BaseEnv

# Initialize the ManiSkill environment
env = gym.make('ManiSkill-v0')  # Replace 'ManiSkill-v0' with the actual environment ID
env.reset()

def take_action(action):
    obs, reward, done, info = env.step(action)
    return obs  # Return the observation to display

# Create a Gradio interface
iface = gr.Interface(
    fn=take_action,
    inputs=gr.inputs.Textbox(label="Action"),
    outputs=gr.outputs.Image(type="numpy", label="Environment View"),
    live=True
)

# Launch the Gradio server
iface.launch()
