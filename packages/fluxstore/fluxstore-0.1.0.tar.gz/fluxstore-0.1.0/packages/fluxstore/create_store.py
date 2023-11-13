import asyncio
from threading import Thread
from .create_reducer import create_reducer, Reducer
from .create_action import Action


type StoreBehavior = "greedy" | "lazy"



def create_store(reducer, initial_state=None, store_behavior: StoreBehavior = "greedy"):
  """
  Creates a store object that holds the complete state tree of your app.
  The only way to change the state inside it is to dispatch an action on it.
  """
  state = initial_state
  dispatches = []
  thunks = []




  def get_state():
    if store_behavior=="lazy":
      # for i, thunk in enumerate(thunks):
      #   if not thunk.is_alive():
      #     thunks.pop(i)
      #     dispatches.append(thunk.join())
      for dispatch in dispatches:
        state = reducer(state, dispatch)
      dispatches.clear()
    
    return state

  def dispatch(action: Action):
    # if "thunk" in action:
    #   thunks.append(Thread(target=lambda : asyncio.run(action.thunk(action.payload))).start())
    # if store_behavior=="greedy":
    #   for i, thunk in enumerate(thunks):
    #     if not thunk.is_alive():
    #       thunks.pop(i)
    #       dispatches.append(thunk.join())
      for dispatch in dispatches:
        state = reducer(state, dispatch)
    dispatches.append(action)

  return {
    "get_state": get_state,
    "dispatch": dispatch
  }
