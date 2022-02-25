from game.casting.actor import Actor

class Rocks(Actor):


    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._lose_point = -1
    
    def set_lose_point(self, lose_point):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._lose_point = lose_point

    def get_lose_point(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._lose_point