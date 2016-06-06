
import random
from live import *

# Scan the currently open Ableton Live set.
#
# The scan of the current set is cached in order to not
# having to rescan the set on each save, so when tracks
# or effects are added, some CLI argument (or the like)
# will have to be provided whenever the current setup
# cease being up-to-date.
class PineappleSet:

  # The list of plugins which will alter the set
  plugins = []

  # Constructor
  def __init__(self):
    self.set = Set()
    self.set.scan()

  # Initiates a stupid loop where tempo is changed
  # randomly at every beat.
  def run(self):
    while True:
        self.set.wait_for_next_beat()
        self.set.tempo = 90 + random.randrange(0, 100, 1)

# Intanciates a pineapple set and runs its loop
set = PineappleSet()
set.run()

