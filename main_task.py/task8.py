# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and
# print the total number of demerit points. 
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function 
# should print: “License suspended”.
speedof_car=int(input('enter speed of your car: '))
speed_limit=70
if speedof_car<=speed_limit:
   print('OK')
else:
    points=round((speedof_car-speed_limit)/5) #using floor operator so as not to have decimal points
    if points>12:
        print('licence suspended points',points)
    else:
        print('points:',points)    






