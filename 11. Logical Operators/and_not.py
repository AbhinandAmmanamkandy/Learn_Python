# Range - if the temp is greater than zero and less than 28 
#  We can type 0 < temp < 28

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside🥵")
    print("It is SUNNY ☀")
elif temp <=0 and is_sunny:
    print("Its is cold outside 🥶")
    print("It is sunny ☀")
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is sunny ☀")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside🥵")
    print("It is CLOUDY 🌥")
elif temp <=0 and not is_sunny:
    print("Its is cold outside 🥶")
    print("It is CLOUDY 🌥")
elif 0 < temp < 28 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY 🌥")