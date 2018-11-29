#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


print ('started')
def distance():

    print ('called distance function')
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    #StopTime = time.time()
    #print( 'original stop time was', StopTime)

    print(GPIO.input(GPIO_ECHO))

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:

        StartTime = time.time()
        #print ('start time from scratch bcos no signal')


    print('start time is: ', StartTime)
    # save time of arrival
    if GPIO.input(GPIO_ECHO) == 1:

        StopTime = time.time()
        print('stop time taken. Is: ', StopTime)
##    else:
##        return "Nothing Found"

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    print('time elapsed is', TimeElapsed, "with S and S times", StartTime,'and', StopTime)
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print ('distance as such is', distance)

    return distance
distlist=[]

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if distlist!=[]:
               index = len(distlist)-1

               if (distlist[index] - dist) <= 15 :
                   # append the new distance value only if its difference from the previous value in the Distance List is less than or equal to 20 cm.
                   distlist.append(dist)
                   print ("Measured Distance = %.1f cm" % dist)
            else:
                distlist.append(dist)
                print ("Measured Distance = %.1f cm" % dist)







            time.sleep(0.01)



        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print(distlist)
        print("Measurement stopped by User")
        GPIO.cleanup()
