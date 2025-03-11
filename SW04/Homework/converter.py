class Converter:
    INCH_TO_CM = 2.54

    @staticmethod
    def inches_to_cm(inches):
        return inches * Converter.INCH_TO_CM
     
    @staticmethod
    def cm_to_inches(cm):
        return cm / Converter.INCH_TO_CM
    
print(Converter.inches_to_cm(10), "cm")
print(Converter.cm_to_inches(25.4), "inches")