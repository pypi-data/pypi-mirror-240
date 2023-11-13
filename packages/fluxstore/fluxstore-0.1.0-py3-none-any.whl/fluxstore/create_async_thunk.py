# from typing import Callable
# from .create_action import Action, Payload, ActionCreator

# def create_async_thunk[T: str, P: Payload](t: str, thunk: Callable[[Payload], Action]) -> ActionCreator[str, Payload]:
#   """
#   Returns a function that creates an action object with the given type and payload.
#   Actions should be dispatched to the store using the store.dispatch() method.

#   Args:
#   - t (str): The type of the action.

#   Returns:
#   - action_creator (function): A function that creates an action object with the given type and payload.
#   """
#   def thunk_action_creator(payload: P) -> Action[T, P]:
#     return { "type": t, "payload": payload,  thunk: thunk}
#   return thunk_action_creator