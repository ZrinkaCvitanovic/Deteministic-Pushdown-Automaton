# Deterministic pushdown automaton
A simulation of a deterministic pushdown automaton

The automaton takes input in the following format:<br />
(1) multiple user inputs separated by "|"<br />
(2) a set of all states (Q)<br />
(3) the alphabet (∑)<br />
(4) a set of all stack symbols (Γ)<br />
(5) a set of all finite states (F)<br />
(6) the initial state (q0)<br />
(7) the initial stack symbol (Z0)<br />
... all transition functions in format: currentState, inputCharacter, stackSymbol -> newState, stack<br />
<br />
The program prints all states of an automaton while parsing each character of each input in line 1. <br />
For each character it prints the new state and the current stack.<br /><br />
At the end, if the final state is acceptable,the automaton prints "1", else it prints "0".<br />
If an automat cannot parse all characters because a certain transition is undefined, it prints "fail".<br />
