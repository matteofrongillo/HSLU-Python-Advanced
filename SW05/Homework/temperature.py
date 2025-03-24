class Temperature:
    def __init__(self, celsius:float, fahrenheit:None):
        """
        The class stores a temperature in celsius degrees

        Variable:
            celsius(float): The temperature in Celsius degrees
        """
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    @property
    def celsius(self):
        """
        
        """
        return f"Temperature: {round(self._celsius,3)}°C"
    
    @celsius.setter
    def celsius(self, value:float):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        self._fahrenheit = self._celsius * 1.8 + 32
        return f"Temperature: {round(self._fahrenheit,3)}°F"
    
    @fahrenheit.setter
    def fahrenheit(self,value:float):
        self._fahrenheit = value
        
    
t1 = Temperature(100, None)
print(t1.fahrenheit)
