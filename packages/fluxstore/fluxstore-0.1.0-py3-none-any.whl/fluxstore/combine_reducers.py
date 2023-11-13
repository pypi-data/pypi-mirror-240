from typing import List
from .create_action import Action
from .create_reducer import Reducer



def combine_reducers(reducers: List[Reducer]) -> Reducer:
  """
  Combines reducers.
  
  This allows the developer to combine multiple reducers into
  one.

  The resulting reducer function will take the state produced
  by the first reducer, and pass that as the initial value to
  the second reducer. The resulting state is constructed by
  taking the result of one reducer, then passing that as the
  initial value to the next reducer, and so on.

  A common use case for this API is to allow each reducer
  to manage an independent part of the global state, while
  allowing each reducer to operate independently.
  
  Args:
  - reducers: The list of reducers to combine.
  
  Returns:
  - A combined reducer.
  """

  def combined_reducers(state: dict, action: Action) -> Reducer:
    next_state = state
    for reducer in reducers:
      next_state = reducer(next_state, action)
    return next_state

  return combined_reducers
  