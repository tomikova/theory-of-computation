import sys

def parseLine(f):	
	tmp = f.split('|')
	parsedList = []
	for x in range(len(tmp)):
		parsedList.append(tmp[x].split(','))
    return parsedList

def epsilon(originalList,listX,existing,transition):
    originalList.sort()
    tmpList=[]
    listXTmp=[]
    for i in range(len(originalList)):
        tmpList.append(originalList[i])
        
    for i in range(len(listX)):
        for j in range(len(transition)):
            if listX[i]==transition[j][0] and transition[j][1]=='$':
                for k in range(len(transition[j][2])):
                               if transition[j][2][k] not in existing:
                                   existing.append(transition[j][2][k])
                                   tmpList.append(transition[j][2][k])
                                   listXTmp.append(transition[j][2][k])
    solution=[]
    for i in range(len(tmpList)):
        if tmpList[i] not in solution:
            solution.append(tmpList[i])
    solution.sort()
    listXTmp.sort()
    listX=listXTmp
    if solution==originalList:
        return solution
    else:
        solution=epsilon(solution,listX,existing,transition)
        return solution
                                    
def main():
    
    rows = [row[:-1] for row in sys.stdin.readlines()]
    
    inSequence=parseLine(rows[0])
    states=rows[1].split(',')
    inSign=rows[2].split(',')
    acceptable=rows[3].split(',')
    start=rows[4].split(',')
	transition =[] 

    for i in range(len(rows)):
        if i>4:
            stateDefinition=rows[i]
            current=stateDefinition[:stateDefinition.find(',')]
            trans=stateDefinition[stateDefinition.find(',')+1:stateDefinition.find('->')]
            next=stateDefinition[stateDefinition.find('->')+2:].split(',')
            transition.append([current,trans,next])

    for i in range(len(inSequence)):
        _exit=[[]]
        for z in range(len(inSequence[i])+1):
            if z>0:
                _exit.append([])

        pom=[]
        _exit[0]=epsilon(start,start,pom,transition)
        counter=0
        hlp1=0
        written=0
        for j in range(len(inSequence[i])):
            for l in range(len(_exit[j])):
                for k in range(len(transition)):
                    if _exit[j][l]==transition[k][0]:
                        hlp1=1
                        if _exit[j][l]==transition[k][0] and inSequence[i][j]==transition[k][1]:
                           listOfEpsilon=[]
                           for m in range(len(transition[k][2])):
                                          listOfEpsilon.append(transition[k][2][m])
                           existing=[]
                           listOfStates=epsilon(listOfEpsilon,listOfEpsilon,existing,transition)
                           for n in range(len(listOfStates)):
                               if listOfStates[n] not in _exit[j+1]:
                                    _exit[j+1].append(listOfStates[n])
                           written=1
                if (hlp1==1 or hlp1==0) and written==0:
                       if len(_exit[j+1])==0:                          
                           _exit[j+1].append("#")              
                hlp1=0
                written=0
        hlp2=0
        for y in range(len(_exit)):
            if "#" in _exit[y] and len(_exit[y])>1:
                del _exit[y][0]
            if (y+1)<len(_exit):
                if "#" in _exit[y] and len(_exit[y+1])<2:
                    hlp2=1
            if hlp2 and (y+1)<len(_exit):
                    _exit[y+1].append("#")
        
        for y in range(len(_exit)):
            _exit[y].sort()
        outputString=''
        for y in range(len(_exit)):
            for x in range(len(_exit[y])):
                if x<len(_exit[y])-1:
                    outputString=outputString+str(_exit[y][x])+','                
                else:
                    if y<len(_exit)-1:
                       outputString=outputString+str(_exit[y][x])+"|"
                    else:
                        outputString=outputString+str(_exit[y][x])
        print outputString
      
main()
                    