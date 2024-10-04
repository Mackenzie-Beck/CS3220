import random

vacuumWorldStates=['Dirty','Clean']
agenLocations=['Left','Right']

DDL=(vacuumWorldStates[0],vacuumWorldStates[0],agenLocations[0])
DDR=(vacuumWorldStates[0],vacuumWorldStates[0],agenLocations[1])
DCL=(vacuumWorldStates[0],vacuumWorldStates[1],agenLocations[0])
DCR=(vacuumWorldStates[0],vacuumWorldStates[1],agenLocations[1])
CDL=(vacuumWorldStates[1],vacuumWorldStates[0],agenLocations[0])
CDR=(vacuumWorldStates[1],vacuumWorldStates[0],agenLocations[1])
CCL=(vacuumWorldStates[1],vacuumWorldStates[1],agenLocations[0])
CCR=(vacuumWorldStates[1],vacuumWorldStates[1],agenLocations[1])

vacuumWorld = (dict(
    DDL=dict(Suck=CDL,Left=DDL, Right=DDR),
    DDR=dict(Suck=DCR, Left=DDL, Right=DDR),
    DCL=dict(Suck=CCL, Left=DCL, Right=DCR),
    DCR=dict(Suck=DCR, Left=DCL, Right=DCR),
    CDL=dict(Suck=CDL, Left=CDL, Right=CDR),
    CDR=dict(Suck=CCR, Left=CDL, Right=CDR),
    CCL=dict(Suck=CCL, Left=CCL, Right=CCR),
    CCR=dict(Suck=CCR, Left=CCL, Right=CCR)
))

results=[dict(Suck=CDL,Left=DDL, Right=DDR),dict(Suck=DCR, Left=DDL, Right=DDR),dict(Suck=CCL, Left=DCL, Right=DCR),dict(Suck=DCR, Left=DCL, Right=DCR),dict(Suck=CDL, Left=CDL, Right=CDR),dict(Suck=CCR, Left=CDL, Right=CDR),dict(Suck=CCL, Left=CCL, Right=CCR),dict(Suck=CCR, Left=CCL, Right=CCR)]

#d1 = {}
keyList = [DDL,DDR,DCL,DCR,CDL,CDR,CCL,CCR]


def makeData():
  d1 = {}
  for i in range(len(keyList)):
    d1[keyList[i]]=results[i]
  return d1



def vacuumStatesLocations():
  x = []
  y = []
  n=len(keyList)
  for _ in range(n):
    x.append(random.randint(0, n+1))
    y.append(random.randint(0, n+1))
  zipped = zip(x, y)
  return dict(zip(keyList, zipped))
  
