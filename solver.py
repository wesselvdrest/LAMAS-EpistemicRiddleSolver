import argparse
from model import Model
from expressions import *

# S5 Kripke model solver

# Kripke model contains:
# S              -- A set of States
# Pi             -- A dictionary of valuations per state
# R_1 ... R_m    -- A set of Relations 

# The logic which we are using can be defined by subclassing BooleanAlgebra
# Essentially, we are adding the rules for the K, C, [] and <> operators.

def parse_proposition(string):
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    print(string)
    expression = Expression(string)
    print(expression)
    expression = expression.expr

    return expression

def valid(model, pointed_state, proposition):
    """ A proposition can have many forms. We will use the truth
    definition of the S5 language operators, the C operator and
    the public announcement operators to determine whether the
    proposition is valid.

    The truth definition:
    (M, s) |= p        iff valuation(s)(p) = true
    (M, s) |= p & q    iff (M, s) |= p and (M, s) |= q
    (M, s) |= ~p       iff (M, s) not |= p
    (M, s) |= K{A}p    iff (M, t) |= p for all (s, t) in Rel{A}
    (M, s) |= Cp       iff (M, t) |= p for all (s, t) in the union of Rel(A) .. Rel(Z)
    (M, s) |= [p]q     iff (M, s) |= p implies that (M|p, s) |= q
    (M, s) |= <p>q     iff (M, s) |= p and (M|p, s) |= q

    The pointed state can be extracted from the model. A ! denotes the 
    true world.
    """
    # An atom is valid in (M, s) if the atom is in the valuation    

    # print(model)

    # TODO: Fix in the parser that we do not get propositions of type Expression    
    if isinstance(proposition, Expression):
        # This is a quick fix
        proposition = proposition.expr

    if isinstance(proposition, Atom):
        prop_is_valid = proposition.arg in model.valuations[str(pointed_state)]

    elif isinstance(proposition, AND):
        prop_is_valid = valid(model, pointed_state, proposition.arg1) and valid(model, pointed_state, proposition.arg2)

    elif isinstance(proposition, NOT):
        prop_is_valid = not valid(model, pointed_state, proposition.arg)

    elif isinstance(proposition, OR):
        prop_is_valid = valid(model, pointed_state, proposition.arg1) or valid(model, pointed_state, proposition.arg2)


    elif isinstance(proposition, K):
        agent = proposition.agent
        prop_is_valid = True
        for relation in model.relations[agent]:
            if pointed_state in relation:
                if pointed_state == relation[0]:
                    if not valid(model, relation[1], proposition.arg):
                        prop_is_valid = False
                        break
                else:
                    # pointed_state == relation[1]
                    if not valid(model, relation[0], proposition.arg):
                        prop_is_valid = False
                        break

    elif isinstance(proposition, C):
        # Determine which of the states are reachable in any number of steps
        # From the current pointed state
        reachable_states = {pointed_state}
        prev_len_reachable_states = 0   # Keep track of length so that we may stop the while loop
        while len(reachable_states) != prev_len_reachable_states:
            prev_len_reachable_states = len(reachable_states)
            for _, relations in model.relations.items():
                for relation in relations:
                    for state in reachable_states.copy():
                        if state in relation:
                            reachable_states.update({*relation})

        # If in any of the states in the set of reachable states, it does
        # not hold that proposition.arg (the argument of the C operator), then 
        # The proposition is not valid
        prop_is_valid = True
        for state in reachable_states:
            if not valid(model, state, proposition.arg):
                prop_is_valid = False
                break

    elif isinstance(proposition, Box):
        # The announcement deletes some of the states and relations
        # The proposition is valid if the argument is true regardless of the announcement

        # If I understand it correctly, the proposition should thus be valid
        # if either the announcement is false, or the argument is true
        # TODO: CONFIRM THAT THIS IS INDEED THE CASE! Correct me on this one!
        prop_is_valid = not valid(model, pointed_state, proposition.arg1) or valid(model, pointed_state, proposition.arg2)

    elif isinstance(proposition, Diamond):
        # The announcement deletes some of the states and relations
        # Namely, the announcement deletes all states in which the announcement is invalid
        viable_states = model.states.copy()
        for state in model.states:
            if not valid(model, state, proposition.arg1):
                viable_states.remove(state)

        temp_model = Model.copy(model)
        temp_model.set_states(viable_states)

        if pointed_state not in temp_model.states:
            prop_is_valid = False
        else:
            prop_is_valid = valid(temp_model, pointed_state, proposition.arg2)


    return prop_is_valid
      
def where(model, proposition):
    in_worlds = []
    for state in model.states:
        pointed_state = state

        if valid(model, pointed_state, proposition):
            in_worlds.append(pointed_state)

    return in_worlds

def main():
    parser = argparse.ArgumentParser("Kripke model solver")
    parser.add_argument("-m", "--model", metavar="FILE", required=True, help="The filename that contains the Kripke model")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--valid", metavar="FILE", help="The filename in which a proposition is given. The valid() function will be run on that proposition.")
    group.add_argument("-w", "--where", metavar="FILE", help="The filename in which a proposition is given. The where() function will be run on that proposition.")
    args = parser.parse_args()
    model = Model.fromtxtfile(args.model)
    print(model)

    if not args.valid and not args.where:
        print("No filename specified for either the valid or where functions.")
        parser.print_help()

    # We now have the model defined.
    # Now we can ask whether a proposition is valid
    if args.valid:
        with open(args.valid, "r") as f:
            contents = f.readlines()

        pointed_state = model.pointed_state        

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)
                # TODO: Print unicode double turnstile and the negation of the double turnstile!
                if valid(model, pointed_state, proposition):
                    turnstile = u'\u22A8'
                    print(f"(M, {pointed_state}) {turnstile} {string}")
                else:
                    not_turnstile = u'\u22AD'
                    print(f"(M, {pointed_state}) {not_turnstile} {string}")
                print()

    # We can also ask where the proposition is valid
    if args.where:
        with open(args.where, "r") as f:
            contents = f.readlines()

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)
                in_worlds = where(model, proposition)
                print(f"The proposition {proposition} is true in worlds {in_worlds}.")


if __name__ == "__main__":
    main()