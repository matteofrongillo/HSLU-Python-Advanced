class Time:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

        try:
            self._hours = int(self._hours)
            self._minutes = int(self._minutes)
            self._seconds = int(self._seconds)
        except:
            raise ValueError("Time attributes must be integers")

        if self._seconds >= 60:
            extra_minutes = self._seconds // 60
            self._seconds %= 60
            self._minutes += extra_minutes

        if self._minutes >= 60:
            extra_hours = self._minutes // 60
            self._minutes %= 60
            self._hours += extra_hours

        if self._hours >= 24:
            self._hours %= 24

    def __add__(self,other:int):
        try:
            other._hours = int(other._hours)
            other._minutes = int(other._minutes)
            other._seconds = int(other._seconds)
        except:
            raise ValueError("Time attributes must be integers")
        return Time(self._hours+other._hours,self._minutes+other._minutes,self._seconds+other._seconds)

    def __str__(self):
        if self._hours < 10:
            self._hours = f"0{self._hours}"
        
        if self._minutes < 10:
            self._minutes = f"0{self._minutes}"
        
        if self._seconds < 10:
            self._seconds = f"0{self._seconds}"
        
        return f"{self._hours}:{self._minutes}:{self._seconds}"

time1 = Time(15,23,50)
print(time1)

time2 = Time(53,73,71)
print(time2)

time3 = time1 + time2
print(time3)

