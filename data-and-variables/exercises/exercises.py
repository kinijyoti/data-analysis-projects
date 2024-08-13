# 1. Declare and assign the variables here:
nameOfSpaceShuttle = "Determination"
shuttleSpeedInMPH = 17500
distanceToMarsinKM = 225000000
distanceToTheMoonInKM = 384400
milesPerKilometer = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print (type(nameOfSpaceShuttle))
print(type(shuttleSpeedInMPH))
print(type(distanceToMarsinKM))
print(type(distanceToTheMoonInKM))
print(type(milesPerKilometer))

# Code your solution to exercises 3 and 4 here:
#Create and assign a miles to Mars variable. You can get the miles to Mars by multiplying the distance to Mars in kilometers by the miles per kilometer.
distanceToMarsInMPH = distanceToMarsinKM * milesPerKilometer
print(distanceToMarsInMPH)
hrsToMars = distanceToMarsInMPH/shuttleSpeedInMPH
print(hrsToMars)
daysToMars = hrsToMars/24
print(daysToMars)
print(nameOfSpaceShuttle + " will take " + str(daysToMars) + " days to reach the Mars.")


# Code your solution to exercise 5 here
distanceToTheMoonInMPH = distanceToTheMoonInKM * milesPerKilometer
print(distanceToTheMoonInMPH)
hrsToMoon = distanceToTheMoonInMPH/shuttleSpeedInMPH
print(hrsToMoon)
daysToMoon = hrsToMoon/24
print(daysToMoon)
print(nameOfSpaceShuttle + " will take " + str(daysToMoon) + " days to reach the Moon.")