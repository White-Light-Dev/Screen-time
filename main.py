import time
import os
from config import *

os.system("chmod +x notification.sh") # выдаём право на исполнение

# преобразование минут в секунды
if working_hours >= 1:
    working_hours_n = round(60 * int(working_hours) + (working_hours - int(working_hours)) * 100)
else:
    working_hours_n = working_hours * 100

if time_relax >= 1:
    time_relax_n = round(60 * int(time_relax) + (time_relax - int(time_relax)) * 100)
else:
    time_relax_n = time_relax * 100

time.sleep(working_hours_n)
os.system("./notification.sh {0} {1}".format(working_hours, time_relax))
print('\a')
working_hours_n += time_relax_n

while 1:
    time.sleep(working_hours_n)
    os.system("./notification.sh {0} {1}".format(working_hours - time_relax, time_relax))
    print('\a')
