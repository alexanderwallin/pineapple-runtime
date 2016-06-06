from live import *

import plugin_tempo_changer

# Scan the currently open Ableton Live set.
#
# The scan of the current set is cached in order to not
# having to rescan the set on each save, so when tracks
# or effects are added, some CLI argument (or the like)
# will have to be provided whenever the current setup
# cease being up-to-date.
class PineappleSet:

  # The list of plugins which will alter the set
  plugins = [plugin_tempo_changer]

  # Constructor
  def __init__(self):

    # This is our state, which will be modified here
    # and there
    self.state = {
      'plugins': [plugin_tempo_changer]
    }

    # Scan the currently open Ableton Live set
    self.set = Set()
    self.set.scan()

  # Initiates a stupid loop where tempo is changed
  # randomly at every beat.
  def run(self):
    while True:
      self.set.wait_for_next_beat()

      for plugin in self.plugins:
        plugin.update(self.set)

# Intanciates a pineapple set and runs its loop
set = PineappleSet()
set.run()

