import random

# Update these to see hot reloaded changes
MIN_TEMPO = 120
MAX_TEMPO = 180

# A simple example of a pineapple plugin that randomly changes
# the set's tempo, pending from 90-190.
def reduce(state, set):
  try:
    state['tempo'] = MIN_TEMPO + random.randrange(0, MAX_TEMPO - MIN_TEMPO, 1)
  except Exception as e:
    print "[tempo reducer] Could not set new tempo:"
    print e

  return state
