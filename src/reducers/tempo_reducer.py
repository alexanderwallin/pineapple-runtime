import random

# A simple example of a pineapple plugin that randomly changes
# the set's tempo, pending from 90-190.
def reduce(state, set):
  #print "reduce tempo", state
  state['tempo'] = 90 + random.randrange(0, 30, 1)
  return state
