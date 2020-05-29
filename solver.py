import argparse
from model import Model

import expression_parser

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
    expr = expression_parser.Expression(string)
    print(expr)
    print()


def valid():
    pass

def where():
    pass

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

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)


    if args.where:
        with open(args.where, "r") as f:
            contents = f.readlines()

        for string in contents:
            if len(string) > 0:
                proposition = parse_proposition(string)


    # We now have the model defined.
    # Now we can ask whether a proposition is valid



if __name__ == "__main__":
    main()