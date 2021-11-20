class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def int_to_time(self):
        time = self.hour * 3600 + self.minute * 60 + self.second
        return time

    @classmethod
    def time_to_int(cls, seconds):
        hour = seconds // 3600
        minute = (seconds % 3600) // 60
        second = (seconds % 3600) % 60
        return cls(hour, minute, second)

    def add_time(self, other):
        time_1 = self.int_to_time() + other.int_to_time()
        time_2 = Time.time_to_int(time_1)
        return f"time is: {time_2.hour} : {time_2.minute} : {time_2.second}"

    def __repr__(self):
        return f"time is {self.hour} : {self.minute} : {self.second}"


t1 = Time(21, 14, 18)
print(t1.int_to_time())
print(Time.time_to_int(3600))
t2 = Time(13, 34, 45)
print(t1.add_time(t2))
