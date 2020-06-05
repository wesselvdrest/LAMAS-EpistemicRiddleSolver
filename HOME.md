# Introduction
For our Logical Aspects of Multi-agent Systems project we wanted to make a riddle solver. Making a program that is able to solve all possible riddles thrown at it would be very cool but probably a bit too ambitious for this assignment. That is why we chose to focus on riddles that relate to the operators found in Kripke logic that can be expressed using Kripke models. In general in these riddles the knowledge of agents is represented in world states in a Kripke model and the amount of possible states will be reduced as more information is made known to the agents. Where the human observer of such a riddle would most likely not be immediately able to understand the reasoning behind the solution to such a riddle our solver is able to analyze a proposition that contains none, some or all the sequentially added information given to the agents throughout the riddle. And when all the possible information of a riddle is put into a proposition the solver will analyze it as valid in the model of the riddle. But more detail on this will follow in the method.

## Example Riddles
### Muddy Children
A father takes his three perfectly logically thinking children to the park. The children go and play until it is time to go and the father calls them back to him. He sees that two of the children have mud on their foreheads. The father then says, "At least one of you has mud on your forehead", followed by, "If you know you have mud on your forehead step forward". No child steps forward. The father then repeats his question, "If you know you have mud on your forehead step forward". This time the two children with mud on their forehead step forward. 

### Drinking Logicians
Three logicians walk into a bar to have a drink. The bartender asks the logicians, "Do all of you want a drink?". The first logician replies with, "I don't know". The second logician replies with, "I don't know". Then the third logician replies to the bartender, "Yes!".

### Cheryl's Birthday
Albert and Bernard both want to know Cheryl's birthday. Cheryl's does not want to make it too easy for them and gives them a list of options that could be her birthday, the list of possibilities is as follows: May 15, May 16, May 19, June 17, June 18, July 14, July 16, Aug 14, Aug 15, Aug 17. She then whispers in Albert's ear the month of her birthday and in Bernard's ear the date. Albert then announces, "I do not know Cheryl's birthday but I know that Bernard does not know either". Bernard now announces, "At first I did not know Cheryl's birthday but now I know!". To which Albert replies, "Then I know her birthday as well!". And they both state at the same time that Cheryl's birthday is July 16. 


