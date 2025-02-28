import time
import hw5Operations

"""
  Homework#5

  Add your name here: James Hering

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.
"""


def readZips(zipFileName):
    zipsRead = open("./zipcodes.txt", "r")
    lineList = zipsRead.readlines()
    lineList.pop(0)
    statesDict = dict()
    for line in lineList:
        line = line.split('\t')
        statesDict.setdefault(line[4], {line[1]: []}).setdefault(
            line[1], []).append((line[3], line[6], line[7]))
    zipsRead.close()
    return statesDict


if __name__ == "__main__":
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inisde the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    # write your code here
    statesDict = readZips("./zipcodes.txt")
    hw5Operations.LatLon("./LatLon.txt").outText(statesDict)
    hw5Operations.CommonCities("./CommonCityNames.txt").outText(statesDict)
    hw5Operations.CityStates("./CityStates.txt").outText(statesDict)
    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")
