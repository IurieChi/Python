from datetime import  datetime, timezone

def astimezone(self, tz):
    """_summary_

    Args:
        tz (_type_): _description_

    Returns:
        _type_: _description_
    """
    if self.tzinfo is tz:
        return self
    # Convert self to UTC, and attach the new timezone object.
    utc = (self - self.utcoffset()).replace(tzinfo=tz)
    # Convert from UTC to tz's local time.
    return tz.fromutc(utc)


print(datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat())
print(datetime(2019, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat())
print(datetime.now().isoformat(timespec='minutes'))
print(datetime.now(timezone.utc) )

# Using datetime.strptime()
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt = datetime.now()

# Date in ISO format
ic = dt.isocalendar()
for it in ic:
    print(it)
# Using datetime.timetuple() to get tuple of all attributes 
tt = dt.timetuple()
for it in tt:
    print(it)
