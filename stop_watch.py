''' to start the stop watch: press Enter
             Split Lap Time: press Enter
                   to quit : press CTRL+C
                                     '''
import time

print('Start ->')
startTime = time.time()
lastTime = startTime
lapNum = 1             # lap number initialized to 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)  # rounds the time up to two decimal places
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time, as it gives difference of time between the laps
except KeyboardInterrupt:
    print('\nSTOP.')
