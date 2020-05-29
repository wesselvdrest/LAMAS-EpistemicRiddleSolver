import argparse
from model import Model
from expression_parser import *

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
    expr = Expression(string)
    print(expr)
    return expr

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

    The pointed state can be extracted from the model. A ! denotes the 
    true world.
    """
    # An atom is valid in (M, s) if the atom is in the valuation
    if isinstance(proposition, Atom):
        prop_is_valid = proposition.arg in model.valuations[pointed_state]

    elif isinstance(proposition, AND):
        prop_is_valid = valid(model, pointed_state, proposition.arg1) and valid(model, pointed_state, proposition.arg2)

    elif isinstance(proposition, NOT):
        prop_is_valid != valid(model, pointed_state, proposition.arg)

    elif isinstance(proposition, K):
        agent = proposition.agent
        # S5 has reflexive relations, so the proposition should also hold
        # in the pointed state
        prop_is_valid = valid(model, pointed_state, proposition.arg)

        if prop_is_valid:
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
        while len(reachable_states) != prev_len_reachable_states
            prev_len_reachable_states = len(reachable_states)
            for state in reachable states:
                for _, relations in model.relations.items():
                    for relation in relations:
                        if state in relation and pointed_state in relation:
                            reachable_states.add(state)

        # If in any of the states in the set of reachable states, it does
        # not hold that proposition.arg (the argument of the C operator), then 
        # The proposition is not valid
        prop_is_valid = True
        for state in reachable_states:
            if not valid(model, state, proposition.arg):
                prop_is_valid = False
                break

    elif isinstance(proposition, Box):
        # The announcement deletes some of the relations
        pass

    elif isinstance(proposition, Diamond):
        # The announcement deletes some of the relations
        pass

    return prop_is_valid
      
def where(model, proposition):
    in_worlds = []
    for state in model.states:
        pointed_state = state.replace("!", "")

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


    if args.valid:
        with open(args.valid, "r") as f:
            contents = f.readlines()

        # Get the pointed state
        for state in model.states:
            if "!" in state:
                pointed_state = state.replace("!", "")
                break

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)
                # TODO: Print unicode double turnstile and the negation of the double turnstile!
                if valid(model, pointed_state, proposition):
                    print(f"M |= {string}")
                else:
                    print(f"M !|= {string}")
                print()


    if args.where:
        with open(args.where, "r") as f:
            contents = f.readlines()

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)
                in_worlds = where(model, proposition)
                print(f"The proposition {proposition} is true in worlds {in_worlds}.")

    # We now have the model defined.
    # Now we can ask whether a proposition is valid



if __name__ == "__main__":
    main()