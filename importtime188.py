#<<<<<<<<create a time show program>>>>>>>>>>>

import time
hour=int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("good morning<<<<")
elif(hour>=12 and hour<17):
    print("good afternoon")
elif(hour>=17 and hour<24):
    print("good night ")

