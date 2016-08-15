import sys

def recursion(originalList,inSign,states,transition,transitionNum,inSignNum,hlp):

    transitionState=[[]]
    for i in range(len(states)):
        if i>0:
            transitionState.append([])
   
    
    for i in range(len(transition)):
          if transition[i][0]==states[i/inSignNum]:
               for j in range(len(originalList)):
                   if transition[i][2] in originalList[j]:
                      transitionState[i/inSignNum].append("yes")
                      transitionState[i/inSignNum].append(hlp[i/inSignNum])
                   else:
                      transitionState[i/inSignNum].append("no")
                      transitionState[i/inSignNum].append(hlp[i/inSignNum])
     
    statesList=[]
    for i in range(transitionNum):
        statesList.append([states[i]])

    transitionStateNum=len(transitionState)      
    for i in range(transitionStateNum):
        for j in range(transitionStateNum):
            if i!=j:
                if transitionState[i]==transitionState[j]:
                   statesList[i].append(states[j])
                   
    statesListNum=len(statesList)             
    for i in range(len(statesList)):
        statesList[i].sort()

    hlp=[]
    for i in range(transitionNum):
        hlp.append([])
        
    for i in range(transitionNum):
        for j in range(len(originalList)):
            if states[i] in originalList[j]:
                hlp[i].append(j)

    uniqueStatesList=[]
    for i in range(statesListNum):
        if statesList[i] not in uniqueStatesList:
            uniqueStatesList.append(statesList[i])

    if uniqueStatesList==originalList:
        return uniqueStatesList
    else:
        uniqueStatesList=recursion(uniqueStatesList,inSign,states,transition,transitionNum,inSignNum,hlp)
        return uniqueStatesList
    
def main():
	
    rows = [row[:-1] for row in sys.stdin.readlines()]
    
    states=rows[0].split(',')
    transitionNum=len(states)
    inSign=rows[1].split(',')
    inSignNum=len(inSign)
    acceptable=rows[2].split(',')
    acceptableNum=len(acceptable)
    start=rows[3].split(',')
    stateDefinition="/n"
    transitionNum=len(rows)-4 
    transition = [[0,0,0]]
    
    for i in range(len(rows)):
        if i>3:
            stateDefinition=rows[i]
            current=stateDefinition[:stateDefinition.find(',')]
            trans=stateDefinition[stateDefinition.find(',')+1:stateDefinition.find('->')]
            next=stateDefinition[stateDefinition.find('->')+2:]
            transition.append([current,trans,next])

    transition.pop(0)
    reachable=start[:]
    
    counter=1
    var=0
    while var<counter:
       for i in range(len(transition)):
          if transition[i][0]==reachable[var] and transition[i][2] not in reachable:
             reachable.append(transition[i][2])
             counter=counter+1
       var=var+1        
    reachable.sort()
    
    var=0
    for i in range(len(transition)):
        if transition[var][0] not in reachable:
             del transition[var]
             var=var-1
        var=var+1

    var=0
    for i in range(len(states)):
        if states[var] not in reachable:
            del states[var]
            var=var-1
        var=var+1

    var=0
    for i in range(len(acceptable)):
        if acceptable[var] not in reachable:
            del acceptable[var]
            var=var-1
        var=var+1

    transitionNum=len(transition)
    transitionNum=len(states)
    acceptableNum=len(acceptable)
    
    acc=[]
    notAcc=[]
    originalList=[]
    for i in range(len(transition)):
        if transition[i][0] in acceptable and transition[i][0] not in acc:
           acc.append(transition[i][0])
        elif transition[i][0] not in acceptable and transition[i][0] not in notAcc:
            notAcc.append(transition[i][0])
    originalList.append(acc)
    originalList.append(notAcc)
    originalList.sort()

    hlp=[]
    for i in range(transitionNum):
        hlp.append([])
        
    for i in range(transitionNum):
        for j in range(len(originalList)):
            if states[i] in originalList[j]:
                hlp[i].append(j)

    
    solution=recursion(originalList,inSign,states,transition,transitionNum,inSignNum,hlp)

    for i in range(len(solution)):
        for j in range(len(states)):
            if states[j] in solution[i]:
                states[j]=solution[i][0]
        for k in range(len(acceptable)):
            if acceptable[k] in solution[i]:
                acceptable[k]=solution[i][0]
        if start[0] in solution[i]:
            start[0]=solution[i][0]
        for l in range(len(transition)):
            if transition[l][0] in solution[i]:
                transition[l][0]=solution[i][0]
            if transition[l][2] in solution[i]:
                transition[l][2]=solution[i][0]
             
    listOfStates=[]
    for i in range(len(states)):
        if states[i] not in listOfStates:
            listOfStates.append(states[i])
    listOfAcceptable=[]
    for i in range(len(acceptable)):
        if acceptable[i] not in listOfAcceptable:
            listOfAcceptable.append(acceptable[i])
    listOfTransition=[]      
    for i in range(len(transition)):
        if transition[i] not in listOfTransition:
            listOfTransition.append(transition[i])

    listOfStates.sort()
    inSign.sort()
    listOfAcceptable.sort()
    listOfTransition.sort()

    print ",".join(listOfStates[i] for i in xrange(len(listOfStates)))
    print ",".join(inSign[i] for i in xrange(len(inSign)))
    print ",".join(listOfAcceptable[i] for i in xrange(len(listOfAcceptable)))
    print start[0]
    for i in range(len(listOfTransition)):
            print listOfTransition[i][0]+','+listOfTransition[i][1]+'->'+listOfTransition[i][2]

main()
