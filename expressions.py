"""
We got inspiration from the freely available online library boolean.py.
We tried subclassing BooleanAlgebra from boolean.py, but due to some
impoty errors, we decided to make our own parser.

An expression can be represented as a tree structure.
Our rules here:
Atoms are lower case letters, e.g. the atoms in (p & q) are p and q
The operators are: ~ | & ( ) K C [] <>
"""
class Atom:
    def __init__(self, arg):
        self.arg = arg
        self.order = 1

    def __repr__(self):
        return f"{self.arg}"

    def __len__(self):
        return 1

class NOT:
    def __init__(self, arg):
        """The NOT operator has an argument.
        It is negating something!"""
        self.arg = arg
        self.order = 1

    def __repr__(self):
        return f"NOT({self.arg})"

    def __len__(self):
        return len(self.arg) + 1

class AND:
    def __init__(self, arg1, arg2):
        """The AND operator has 2 arguments."""
        self.arg1 = arg1
        self.arg2 = arg2
        self.order = 2

    def __repr__(self):
        return f"AND({self.arg1}, {self.arg2})"

    def __len__(self):
        return len(self.arg1) + len(self.arg2) + 1


class OR:
    def __init__(self, arg1, arg2):
        """The OR operator has 2 arguments."""
        self.arg1 = arg1
        self.arg2 = arg2
        self.order = 2

    def __repr__(self):
        return f"OR({self.arg1}, {self.arg2})"

    def __len__(self):
        return len(self.arg1) + len(self.arg2) + 1

class C:
    def __init__(self, arg):
        self.arg = arg
        self.order = 1

    def __repr__(self):
        return f"C({self.arg})"

    def __len__(self):
        return len(self.arg) + 1

class K:
    """Agent {agent} knows that arg"""
    def __init__(self, agent, arg):
        self.agent = agent
        self.arg = arg
        self.order = 1

    def __repr__(self):
        return f"K{repr('{')[1]}{self.agent}{repr('}')[1]}({self.arg})"

    def __len__(self):
        # The length of K{A} is 4
        return len(self.arg) + 4

class Box:
    # An announcement has 2 arguments.
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.order = 2

    def __repr__(self):
        return f"Box[{self.arg1}]({self.arg2})"

    def __len__(self):
        return len(self.arg1) + len(self.arg2) + 2

class Diamond:
    # An announcement has 2 arguments.
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.order = 2

    def __repr__(self):
        return f"Diamond<{self.arg1}>({self.arg2})"

    def __len__(self):
        return len(self.arg1) + len(self.arg2) + 2

class Expression:
    def __init__(self, string):
        # self.epistemic_operators = {"C": C, "K": K}
        self.encountered_pars = 0
        self.expr = self.parse(string)

    def __len__(self):
        return len(self.expr)

    def lpar_case(self, string):
        lpar_count = 1
        self.encountered_pars += 1
        par_index = 1
        while par_index < len(string) and lpar_count > 0:
            if string[par_index] == "(":
                lpar_count += 1
                self.encountered_pars += 1
                # If we find another (, we should look for another )

            if string[par_index] == ")":
                lpar_count -= 1
                self.encountered_pars += 1
                # The expression is balanced with respect to parentheses

            par_index += 1

        if lpar_count > 0:
            # IF the lpar_count is still higher than 0 after that whole while loop
            # We have at least one left parenthesis that is not closed
            raise ParseError(string, "Parentheses are not balanced! More ( than )")

        par_index = par_index - 1
        return par_index

    def order1_case(self, string):
        if string[0] == "(":
            rpar_index = self.lpar_case(string[0:])
            expr = Expression(string[1:rpar_index+0])
            string = string[rpar_index+1:]
        elif string[0].isalpha() and string[0].islower():
            expr = Atom(string[0])
            string = string[1:]
        else:
            subexpr = Expression(string[0:])
            expr = subexpr
            string = string[0 + len(subexpr) + subexpr.encountered_pars:]

        return expr, string

    def announcement_case(self, string):
        if string[0] == "[":
            lbrack_count = 1
            langle_count = 0
        elif string[0] == "<":
            langle_count = 1
            lbrack_count = 0


        index = 1
        while index < len(string) and (lbrack_count > 0 or langle_count > 0):
            if string[index] == "[":
                lbrack_count += 1

            if string[index] == "]":
                if lbrack_count == 0:
                    raise ParseError(string, "Brackets are not balanced! More ] than [")
                lbrack_count -= 1

            if string[index] == "<":
                langle_count += 1

            if string[index] == ">":
                if langle_count == 0:
                    raise ParseError(string, "Angled brackets are not balanced! More > than <")
                langle_count -= 1

            index += 1

        if lbrack_count > 0:
            # IF the lbrack_count is still higher than 0 after that whole while loop
            # We have at least one left bracket that is not closed
            raise ParseError(string, "Brackets are not balanced! More [ than ]")
        elif langle_count > 0:
            # IF the langle_count is still higher than 0 after that whole while loop
            # We have at least one left angled bracket that is not closed
            raise ParseError(string, "Angled brackets are not balanced! More < than >")

        index = index - 1
        return index        


    def parse(self, string):
        # If we see a ~ at the start (NOT)
        # We will add a NOT operator to the list,
        # But we have to know the argument of NOT
        # The argument of NOT can then be an atom,
        # or it can be a sub-expression

        expr = None

        while len(string) > 0:
            # ) case
            if string[0] == ")":
                raise ParseError(string, "Parentheses are not balanced! More ) than (")

            elif string[0] == "]":
                raise ParseError(string, "Brackets are not balanced! More ] than [")

            elif string[0] == ">":
                raise ParseError(string, "Angled brackets are not balanced! More > than <")

            # ( case
            elif string[0] == "(":
                rpar_index = self.lpar_case(string)
                expr = Expression(string[1:rpar_index])
                string = string[rpar_index+1:]

            # Atom case
            elif string[0].isalpha() and string[0].islower():
                expr = Atom(string[0])
                string = string[1:]

            # ~ case
            elif string[0] == "~":
                subexpr, string = self.order1_case(string[1:])
                expr = NOT(subexpr)

            # & case
            elif string[0] == "&":
                # The AND case has 2 arguments, the previous expression and the next
                next_subexpr = Expression(string[1:])
                expr = AND(expr, next_subexpr)
                string = string[len(next_subexpr) + next_subexpr.encountered_pars +1:]

            # | case
            elif string[0] == "|":
                # The OR operator also has 2 arguments
                next_subexpr = Expression(string[1:])
                expr = OR(expr, next_subexpr)
                string = string[len(next_subexpr) + next_subexpr.encountered_pars +1:]

            # The epistemic operator C case
            elif string[0] == "C":
                subexpr, string = self.order1_case(string[1:])
                expr = C(subexpr)

            # The epistemic operator K case
            elif string[0] == "K":
                # string[1] and string[3] should be the open and close braces {}
                agent = string[2]
                subexpr, string = self.order1_case(string[4:])
                expr = K(agent, subexpr)

            # Public announcement []
            elif string[0] == "[":
                rbrack_index = self.announcement_case(string)
                announcement = Expression(string[1:rbrack_index])
                subexpr, string = self.order1_case(string[1+rbrack_index:])
                expr = Box(announcement, subexpr)

            # Public announcement <>
            elif string[0] == "<":
                rangle_index = self.announcement_case(string)
                announcement = Expression(string[1:rangle_index])
                subexpr, string = self.order1_case(string[1+rangle_index:])
                expr = Diamond(announcement, subexpr)


        return expr

    def __repr__(self):
        return f"{self.expr}"


class ParseError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message