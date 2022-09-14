import os
import  time


for adress, dirs, files in os.walk('C:\\'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 18000:
            print(full)