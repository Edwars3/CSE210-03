from game.casting.actor import Actor

class Gem(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._e_point = 1
    
    def set_earn_point(self, e_point):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._e_point = e_point

    def get_earn_point(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._e_point