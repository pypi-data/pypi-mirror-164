#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Utilities used to handle agent observations.
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

import gym
import numpy as np

__all__ = ("ObservationHandler",)


class ObservationHandler:
    """
    Ensures observation spaces from a WOB environment are correct.
    """

    def __init__(self, observation_specs):
        list_spaces = []
        self.sensors = []
        for spec in observation_specs:
            self.sensors.append(spec.name.split(":")[-1])
            list_spaces.append(
                gym.spaces.Box(-np.inf, np.inf, dtype=np.float32, shape=spec.shape)
            )
        self.observation_space = gym.spaces.Tuple(list_spaces)

    def __getitem__(self, k):
        return self.observation_space[self.sensors.index(k)]
