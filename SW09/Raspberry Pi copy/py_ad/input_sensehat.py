from input_base import InputBase, Keys
from enum import Enum
from sense_hat import SenseHat

class InputSenseHat(InputBase):
    """
    Input handler for the SenseHat using joystick input.
    """
    sense = SenseHat()

    def read_key(self) -> Enum:
        """
        Read a key from the SenseHat joystick and return its corresponding key code.

        Returns:
            Enum: The key code corresponding to the pressed key.
        """
        event = self.sense.stick.wait_for_event()

        if event.action == "pressed":
            if event.direction == "up":
                return Keys.UP
            elif event.direction == "down":
                return Keys.DOWN
            elif event.direction == "left":
                return Keys.LEFT
            elif event.direction == "right":
                return Keys.RIGHT
            elif event.direction == "middle":
                return Keys.SELECT
        
        return None

if __name__ == "__main__":
    print("press any key")
    c = InputSenseHat()
    while True:
        key =c.read_key()
        if key == None:
            continue
        else:
            print(f"Taste: {key}, Type: {type(key)}")