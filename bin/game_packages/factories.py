import fantasynames


class NameFactory:
    def __init__(self, gender):
        self.name = fantasynames.human(gender)


class NpcFactory:
    pass
