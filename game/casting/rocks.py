from game.casting.actor import Actor

class Rocks(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._lose_point = -1
    
    def set_lose_point(self, lose_point):

        self._lose_point = lose_point

    def get_lose_point(self):

        return self._lose_point