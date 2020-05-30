# LAMAS Project

## Usage of the program
To see whether a given proposition is valid in a given Kripke model, run:  
```bash
python3 solver.py -m model_file -v proposition_file
```
To see where a given proposition holds in the given Kripke model, run:
```bash
python3 solver.py -m model_file -w proposition_file
```


## Format of Kripke model
For now, the Kripke model should be defined in a .txt file. We might change this to JSON later if we want and have time left. A model file should follow the format of the following example:  
```bash
States:
0
1
2
3
4
5
6
7!

Valuations:
0:
1: p
2: q
3: r
4: p q
5: q r
6: p r
7: p q r

Relations:
A: (0 1), (2 4), (3 6), (5 7)
B: (0 2), (3 5), (1 4), (6 7)
C: (0 3), (4 7), (2 5), (1 6)
```
Here, the ! behind a state number means that is the true world.

## Format of propositions
The operators that can be used are:  
& for AND  
| for OR  
~ for NOT  
C for Common Knowledge  
K{A} for agent A knows that  
<> for some truthful public announcement  
[] for every truthful public announcement  
And of course the parentheses can be used to denote scope ( )  


The following are all valid propositions:  
```bash
~(p & q) | ~r & s  
~(p & q) & r  
Cp  
~Cp  
~C~p  
C~p  
K{A}p  
~K{A}p  
~K{A}~p  
~K(A)p & Cp  
<p>q  
[p]q  
[p & q]r  
[p&q](r & q)  
[p&q]r & q  
p | <q>r  
```