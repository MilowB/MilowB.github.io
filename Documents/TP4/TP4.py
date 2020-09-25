import random
import math

def getHackCode(travel_year):
    return int(math.pow(travel_year, 4))

def verifyHackCode(d, hackCode):
    if hackCode < math.pow(d["neolithic"][0], 4):
        return True
    return False

def rescale(max_out, max_in, value):
    return value * max_out / max_in

def hack(max_year, travel_year, current_year):
    loading = 0
    printing = True
    while loading < 100:
        current_year -= 2
        loading = rescale(100, max_year - travel_year, current_year - travel_year)
        loading = 100 - loading
        if int(loading) % 10 == 0 and printing:
            print(int(loading), "%")
            printing = False
        elif int(loading) % 10 != 0:
            printing = True
    return True

def hack_time(epoch_to_travel):
    d = {"neolithic" : (-10000, -3000), 
        "ancient age" : (-2999, 476), 
        "medieval age" : (477, 1492), 
        "modern age" : (1493, 1789),
        "contemporary age" : (1790, 2020)}
    max_year = 2020
    current_year = 2020
    years_interval = d[epoch_to_travel]
    travel_year = random.randint(years_interval[0], years_interval[1])
    hackCode = getHackCode(travel_year)
    print("Initializing a travel to the year",travel_year)
    if verifyHackCode(d, hackCode):
        print("The HackCode ", hackCode, "is correct")
        print("Launching time travel")
        if hack(max_year, travel_year, current_year):
            print("Time travel to the",epoch_to_travel,"COMPLETE")
    else:
        print("HackCode incorrect")
        print("Aborting the time travel")

if __name__ == "__main__":
    # execute only if run as a script
    hack_time("medieval age")