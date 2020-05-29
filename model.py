class Model:

    def __init__(self, states, pointed_state, valuations, relations):
        self.states = set(states)
        self.pointed_state = pointed_state

        self.valuations = dict(valuations)
        self.relations = dict(relations)


    def __repr__(self):
        return (f"Kripke Model:\n"
                f"States: {self.states}\n"
                f"Valuations: {self.valuations}\n"
                f"Relations: {self.relations}\n"
                )

    @classmethod
    def fromtxtfile(cls, filename):
        """This function parses a file and returns a Kripke model.
        TODO: Use JSON instead of txt"""
        states = set()
        pointed_state = None
        valuations = dict()
        relations = dict()

        with open(filename, 'r') as f:
            contents = f.readlines()
            parse_state = "States"

            for c in contents[1:]:
                c = c.rstrip("\n")
                if c == "":
                    continue

                if parse_state == "States":
                    if c == "Valuations:":
                        parse_state = "Valuations"
                        continue

                    # Pointed states are denoted by !
                    if "!" in c:
                        if pointed_state != None:
                            raise StateParseError(states,
                                                  "Too many ! detected (max 1).")

                        c = c.replace("!", "")
                        pointed_state = int(c)

                    states.add(int(c))

                elif parse_state == "Valuations":
                    if c == "Relations:":
                        parse_state = "Relations"
                        continue

                    split = c.split(" ")
                    for i, s in enumerate(split):
                        s = s.strip(" ")
                        split[i] = s

                    state = split[0].rstrip(":")
                    valuations[state] = split[1:]

                elif parse_state == "Relations":
                    agent = c.split(":")[0]
                    tuples = c.split(":")[1]
                    tuples = tuples.replace("(", "")
                    tuples = tuples.replace(")", "")
                    tuples = tuples.split(",")
                    for r in tuples:
                        r = r.strip(" ")
                        new_relation = (int(r[0]), int(r[2]))

                        try:
                            relations[agent].add(new_relation)
                        except KeyError:
                            relations[agent] = {new_relation}

        return cls(states, pointed_state, valuations, relations)


class StateParseError(Exception):
    def __init__(self, states, message):
        self.states = states
        self.message = message