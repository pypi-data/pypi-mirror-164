#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Actions require special handing when working with `mlagents_envs`, this module contains some utilties to do this.
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

import gym
import numpy as np
from gym_unity.envs import ActionFlattener, ActionTuple, UnityGymException
from mlagents_envs.base_env import ActionSpec

__all__ = ("ActionHandler", "DiscreteActionHandler", "ContinuousActionHandler")


def ActionHandler(action_spec: ActionSpec):
    """Alias for _ActionHandler, creates the correct handler for the given action_spec.

    Args:
        action_spec (ActionSpec): action specification (see mlagent_envs).

    Raises:
        UnityGymException: If the action spec is invalid

    Returns:
        _ActionHandler: handler for the given ActionSpec
    """
    if action_spec.is_continuous():
        return ContinuousActionHandler(action_spec)
    if action_spec.is_discrete():
        return DiscreteActionHandler(action_spec)
    # TODO support both discrete and continuous actions...
    # same as UnityToGymWrapper, its annoying to implement...
    raise UnityGymException(
        "This gym wrapper does not provide explicit support for both discrete and continuous actions."
    )


class _ActionHandler:  # Attempt to streamline actions sent/received from unity. Why is branching even a thing!
    def get_action_tuple(self, actions):
        raise NotImplementedError()


class ContinuousActionHandler(_ActionHandler):
    """Handler for continuous actions."""

    def __init__(self, action_spec):
        """Constructor.

        Args:
            action_spec (ActionSpec): action specification (see mlagent_envs).
        """
        self.num_agents = 1  # TODO multiagent?
        self.action_spec = action_spec
        self.action_size = self.action_spec.continuous_size
        high = np.array([1] * self.action_spec.continuous_size)
        self.action_space = gym.spaces.Box(-high, high, dtype=np.float32)

    def get_action_tuple(self, actions):
        if actions is None:
            return ActionTuple(np.zeros((self.num_agents, self.action_size)))
        if isinstance(actions, (int, float)):
            actions = np.array([float(actions)])
        elif isinstance(actions, (list, tuple)):
            actions = np.array(actions)
        if len(actions.shape) == 1:
            actions = actions[np.newaxis, :]
        return ActionTuple(continuous=actions)  # simple!


class DiscreteActionHandler(_ActionHandler):
    """Handler for discrete actions."""

    def __init__(self, action_spec):
        """Constructor.

        Args:
            action_spec (ActionSpec): action specification (see mlagent_envs).
        """
        self.action_spec = action_spec
        # always flatten action space?
        self.action_size = self.action_spec.discrete_size
        branches = self.action_spec.discrete_branches
        if self.action_size == 1:
            self._flattener = None
            self.action_space = gym.spaces.Discrete(branches[0])
        else:
            self._flattener = ActionFlattener(branches)
            self.action_space = self._flattener.action_space

    def get_action_tuple(self, actions):
        if actions is None:
            # TODO should this return an empty action tuple or throw an error?
            return ActionTuple()
        elif isinstance(actions, int):
            actions = np.array([actions])
        elif isinstance(actions, float):
            raise ValueError(
                f"Received discrete action {actions} that was of type {type(actions)} when it should be int."
            )
        elif isinstance(actions, (list, tuple)):
            actions = np.array(actions)
        else:
            raise ValueError(f"Invalid actions: {actions}")

        if self._flattener is not None:
            # bit of a shame this needs to happen... probably just dont use branches in unity... why are they even there!
            actions = np.array(
                [self._flattener.lookup_action(action) for action in actions]
            )
        actions = actions.reshape(actions.shape[0], self.action_size)
        return ActionTuple(discrete=actions)
