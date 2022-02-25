from game.casting.actor import Actor

class Gem(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._e_point = 1
    
    def set_e_point(self, e_point):

        self._e_point = e_point

    def get_e_point(self):

        return self._e_point