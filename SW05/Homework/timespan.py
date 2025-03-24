from time_exercise import Time
from numpy import abs

class Timespan(Time):
    def __init__(self,hours:Time,minutes:Time,seconds:Time,total_seconds:int):
        super().__init__(hours,minutes,seconds)
        self._total_seconds = total_seconds
        hours = self._total_seconds//3600
        minutes = (self._total_seconds%3600)//60
        seconds = self._total_seconds%60

    def __sub__(self:Time,other:Time):
        global difference
        if not isinstance(other, Time):
            raise TypeError("sub works only between Time instances")

        difference = abs((self._hours + self._minutes + self._seconds) - (other._hours + other._minutes + other._seconds))
        return Timespan(difference)
    
    def __str__(self):
        return f"{difference} sec of difference"
    
time1 = Time(0,1,30)
print(time1)

time2 = Time(0,0,500)
print(time2)

time3 = time1 - time2
print(time3)