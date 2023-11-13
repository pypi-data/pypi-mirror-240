
from typing import Callable, Dict
from .create_action import Action

type Reducer[State: dict, ActionType: Action] = Callable[[State, ActionType], State]

def create_reducer[S: dict, A: Action](initial_state: dict, handlers: Dict[str, Reducer[dict, Action]]) -> Reducer[dict, Action]:
  """
  create a reducer function for use by the store.
  
  Args:
  - initial_state: The initial state of the reducer.
  - handlers: A dictionary of action types and their corresponding reducer functions.
  
  Returns:
  - A reducer function that can be used with the Redux store.
  """

  def reducer_fn(state: S, action: A) -> S:
    if action.type == "@@INIT":
      return initial_state
    if action["type"] in handlers:
      return handlers[action["type"]](state, action)
    else:
      return state

  return reducer_fn
  