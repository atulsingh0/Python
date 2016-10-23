

class RestorePointDoesNotExist(Error):
    pass


class Memento(object):
    """Memento class"""
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        """Returns the state object."""
        return self.__state


class CareTaker(object):
    """CareTaker class."""
    def __init__(self):
        self.__states = []

    def save(self, memento):
        """Save the memento object"""
        self.__states.push(memento)

    def restore(self):
        """Restore the originator state"""
        if self.__states:
            return self.__states.pop()
        raise RestorePointDoesNotExist


class Originator(object):
    def __init__(self, state):
        self.state = state

    def save_to_momento(self):
        return Memento(self.state)

    def restore_from_momento(self, memento):
        self.state = memento.get_state()


caketaker = CareTaker()
originator = Originator("Initialized")
originator.state = "State1"
# Let's save the actual state
caketaker.save(originator.save_to_momento())
# Let's modify the originator state
originator.state = "State2"
# and so on ...
originator.state = "State5"
# Let's save the actual state
caketaker.save(originator.save_to_momento())
# Restore originator
originator.restore_from_momento(caketaker.restore())

# Thanks
# Atul Singh
# www.datagenx.net

