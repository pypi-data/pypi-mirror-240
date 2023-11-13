"""
This module implements a simple state management system inspired by ReduxJS.

The core concept of this system is the store, which holds the state of the application and provides a way to dispatch actions that modify that state. The store is created by passing a reducer function to the createStore function.

The reducer function takes the current state and an action as arguments, and returns a new state based on the action. Actions are plain objects that have a type field and an optional payload field.

This module also provides some utility functions for working with actions and reducers, such as createAction and combineReducers.

Example usage:

  from pyflux import create_action, create_store, create_reducer

  # Define some actions
  increment = create_action('INCREMENT')
  decrement = create_action('DECREMENT')

  # Define a reducer
  def counter(state=0, action):
    if action.type == 'INCREMENT':
      return state + 1
    elif action.type == 'DECREMENT':
      return state - 1
    else:
      return state

  # Combine multiple reducers into one
  rootReducer = create_reducer({
    'increment': counter,
    'decrement': counter,
  })

  # Create the store
  store = create_store(rootReducer)

  # Dispatch some actions
  store.dispatch(increment())
  store.dispatch(decrement())
"""
