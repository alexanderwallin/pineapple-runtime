from live import *

import tempo_modifier
import feel_modifier

#
# Scan the currently open Ableton Live set.
#
# The scan of the current set is cached in order to not
# having to rescan the set on each save, so when tracks
# or effects are added, some CLI argument (or the like)
# will have to be provided whenever the current setup
# cease being up-to-date.
#
class PineappleSet:

  # This is our state, which will be modified here
  # by a list of reducers
  state = {}
  reducers = [feel_modifier, tempo_modifier]

  #
  # Constructor
  #
  def __init__(self):

    # Scan the currently open Ableton Live set
    self.set = Set()
    self.set.scan(scan_devices = True)

  #
  # Initiates a stupid loop where tempo is changed
  # randomly at every beat.
  #
  def run(self):
    while True:
      self.set.wait_for_next_beat()

      self.reduce_state()
      self.apply_state()

  #
  # Reduces the state by calling reduce() on all reducers
  #
  def reduce_state(self):
    for reducer in self.reducers:
      self.state = reducer.reduce(self.state, self.set)

    print "current state", self.state

  #
  # Applies the current state
  #
  def apply_state(self):

    # Tempo
    tempoMultiplier = 2 if self.state['feel']['value'] == feel_modifier.Feel.intense else 1
    self.set.tempo = self.state['tempo'] * tempoMultiplier

    # Eerie resonator
    resonator = self.set.tracks[1].devices[1]
    if resonator:
      resonator_on = 1 if self.state['feel']['value'] == feel_modifier.Feel.eerie else 0
      resonator.set_parameter('Device On', resonator_on)


# Intanciates a pineapple set and runs its loop
set = PineappleSet()
set.run()
