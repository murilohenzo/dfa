from dfa import DeterministicFiniteAutomata

automata = DeterministicFiniteAutomata(4).createAutomata()
language = [1,0,1]

automata['Q0'][0] = 'Q2'
automata['Q0'][1] = 'Q1'
automata['Q1'][0] = 'Q2'
automata['Q1'][1] = 'Q0'
automata['Q2'][0] = 'Q1'
automata['Q2'][1] = 'Q3'
automata['Q3'][0] = 'Q1'
automata['Q3'][1] = 'Q0'

print(automata)

validation = DeterministicFiniteAutomata.validateLanguage(automata, 'Q0', {'Q0', 'Q3'}, language)
print(validation)