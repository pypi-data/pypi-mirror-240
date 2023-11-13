"""
This module defines the Action class and related types for creating actions in pyflux.

Payload: A type alias for a dictionary or None.
Action: A dictionary with a "type" key and a "payload" key.
ActionCreator: A callable that takes a payload and returns an Action.

"""
from typing import Callable, TypeVar

type Payload[PT: dict] = PT | None
type Action[AT: str, AP: Payload] = { "type": AT, "payload": AP}
type ActionCreator[TC: str, PC: Payload] = Callable[[PC],Action[TC, PC]]



def create_action[T: str, P: Payload](t: str) -> ActionCreator[str, Payload]:
  """
  Returns a function that creates an action object with the given type and payload.
  Actions should be dispatched to the store using the store.dispatch() method.

  Args:
  - t (str): The type of the action.

  Returns:
  - action_creator (function): A function that creates an action object with the given type and payload.
  """
  def action_creator(payload: P) -> Action[T, P]:
    return { "type": t, "payload": payload }
  return action_creator
