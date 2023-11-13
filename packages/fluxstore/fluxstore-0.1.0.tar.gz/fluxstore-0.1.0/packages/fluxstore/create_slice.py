from .create_reducer import create_reducer, Reducer
from typing import Dict

def create_slice(reducers:Dict[str, Reducer]={}) -> Reducer:
  def call_reducers(state, reducers):
      """
      Calls each reducer in the given dictionary with the corresponding key in the state object.
      """
      for key, reducer in reducers.items():
          state[key] = reducer(state[key])
      return state
  return call_reducers

  
