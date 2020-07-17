from itertools import chain

class DeterministicFiniteAutomata:

    def __init__(self, quantity_states):
        self.dfa = {}
        self.quantity_states = quantity_states

    def createAutomata(self):
        for state in range(self.quantity_states):
            self.dfa['Q' + str(state)] = {}
            for transition in range(2):
                self.dfa['Q' + str(state)][transition] = 'Q' + str(transition)
        return self.dfa

    def validateLanguage(transition_states, start_state, set_acceptence, input_language):
        current_state = start_state
        keys = set(chain.from_iterable(i.keys() for i in transition_states.values()))
        set_boolean = [int(char) in keys for char in input_language]
        for idx in range(len(set_boolean)):

          if set_boolean[idx] != True:
              current_state = None
              return current_state in set_acceptence
          else:
               current_state = transition_states[current_state][input_language[idx]]
        return current_state in set_acceptence