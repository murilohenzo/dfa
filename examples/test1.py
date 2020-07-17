from dfa import DeterministicFiniteAutomata

automata = DeterministicFiniteAutomata(3).createAutomata()
language = [1,0,1,1,1,0,1]

automata['Q0'][0] = 'Q0'
automata['Q0'][1] = 'Q1'
automata['Q1'][0] = 'Q2'
automata['Q1'][1] = 'Q0'
automata['Q2'][0] = 'Q1'
automata['Q2'][1] = 'Q2'

print(automata)

validation = DeterministicFiniteAutomata.validateLanguage(automata, 'Q0', {'Q0'}, language)
print(validation)