# LAMAS Project

## Format of Kripke model

## Format of propositions
The operators that can be used are:  
& for AND  
| for OR  
~ for NOT
C for Common Knowledge  
K{A} for agent A knows that  
And of course the parentheses can be used to denote scope ( )  
To be added: [] and <> for announcements  


The following are all valid propositions:
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
