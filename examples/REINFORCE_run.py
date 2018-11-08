import numpy as np
import os, sys
import RLkit
from RLkit.environment import Environment
from RLkit.algorithms import REINFORCE

network_specs = [
  {
    "type": "dense",
    "size": 64,
    "activation":"relu"
  },
  {
    "type": "dense",
    "size": 32,
    "activation":"relu"
  }
]
env_ = Environment(env_name="CartPole-v1", render = False)
agent = REINFORCE(env_, network_specs)
agent.train(episodes=6000, lr=0.01, gamma=1)