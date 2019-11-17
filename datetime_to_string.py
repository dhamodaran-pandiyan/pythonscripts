from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print(datetime_object)

print(datetime.strptime('Thu, 16 Dec 2010 12:14:05', '%a, %d %b %Y %H:%M:%S').isoformat())
print(type(datetime_object))