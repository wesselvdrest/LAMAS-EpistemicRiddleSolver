class Model:

    def __init__(self, states, valuations, relations):
        self.states = set(states)
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
        valuations = dict()
        relations = dict()

        with open(filename, 'r') as f:
            contents = f.readlines()
            parse_state = "States"

            for c in contents[1:]:
                c = c.rstrip("\n")
                if c == "":
                    continue

                if parse_state is "States":
                    if c == "Valuations:":
                        parse_state = "Valuations"
                        continue

                    states.add(c)
                elif parse_state is "Valuations":
                    if c == "Relations:":
                        parse_state = "Relations"
                        continue

                    split = c.split(" ")
                    for i, s in enumerate(split):
                        s = s.strip(" ")
                        split[i] = s

                    state = split[0].rstrip(":")
                    valuations[state] = split[1:]

                elif parse_state is "Relations":
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


        return cls(states, valuations, relations)
