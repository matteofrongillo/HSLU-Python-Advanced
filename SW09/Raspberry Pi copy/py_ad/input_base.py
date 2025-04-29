from enum import Enum

class Keys(Enum):
    UP = -2
    DOWN = -3
    LEFT = -4
    RIGHT = -5
    SELECT = 13
    
class InputBase:
    """
    Base class for handling input operations.

    This class defines the interface for reading key inputs.
    Subclasses must implement the `read_key` method.
    """

    def read_key(self) -> Keys:
        """
        Read a key input and return its corresponding key code.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError()
