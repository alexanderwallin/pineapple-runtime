import random

# A simple example of a pineapple plugin that randomly changes
# the set's tempo, pending from 90-190.
def update(set):
  set.tempo = 90 + random.randrange(0, 100, 1)
