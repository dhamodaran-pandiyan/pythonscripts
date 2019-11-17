#place this code in the path
#C:\Users\<User Name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
from datetime import datetime
file1 = open("D:\starttime.txt", "a+")
now = datetime.now()
current_time = now.strftime("Date: %a, %d-%m-%Y      Time: %I:%M:%S %p")
file1.write(current_time)
file1.write("\n")
file1.close()