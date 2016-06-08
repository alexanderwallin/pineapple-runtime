
# The different available feels
class Feel:
  intense = 'intense'
  eerie = 'eerie'

active_feels = [Feel.eerie, Feel.intense]

def _get_initial_state(start_time):
  return {
    'value': Feel.eerie,
    'last_time': start_time
  }

def _get_next_feel(current_feel):
  if current_feel == Feel.eerie:
    return Feel.intense
  else:
    return Feel.eerie

# Reducer function
def reduce(prev_state, set):
  next_state = dict(prev_state)

  if not 'feel' in next_state:
    next_state['feel'] = _get_initial_state(set.time)
  else:
    if set.time - prev_state['feel']['last_time'] > 4.0:
      next_state['feel']['value'] = _get_next_feel(next_state['feel']['value'])
      next_state['feel']['last_time'] = set.time

  return next_state
