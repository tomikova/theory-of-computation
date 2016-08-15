import sys

def parseLine(f):
    tmp = f.split('|')
	parsedList = []
	for x in range(len(tmp)):
		parsedList.append(tmp[x].split(','))
    return parsedList

def splitLine(f):
	parsedList = f.split(',')
	parsedList[1] = list(parsedList[1])
	parsedList[1].reverse()
	return parsedList

def main():

    rows = [row[:-1] for row in sys.stdin.readlines()]
    
    inSequence=parseLine(rows[0])
    states=rows[1].split(',')
    inSign=rows[2].split(',')
    stackStates=rows[3].split(',')
    acceptable=rows[4].split(',')
    start=rows[5].split(',')
    startStack=rows[6].split(',')
	transition =[]
	
    for i in range(len(rows)):
        if i>6:
             stateDefinition=rows[i]
             current=stateDefinition[:stateDefinition.find(',')]
             trans=stateDefinition[stateDefinition.find(',')+1:stateDefinition.find('->')].split(',')
             next=splitLine(stateDefinition[stateDefinition.find('->')+2:])
             transition.append([current,trans,next])

    for i in range(len(inSequence)):
        outputString=''
        outputString=outputString+str(start[0])+'#'+str(startStack[0])+'|'
        stack=[]
        stack.append(startStack[0])
        currentState=start[0]
        for j in range(len(inSequence[i])):
            flag1=0
            flag5=0
            for k in range(len(transition)):
                if len(stack)>0:
                    if currentState==transition[k][0] and inSequence[i][j]==transition[k][1][0] and stack[0]==transition[k][1][1]:
                        currentState=transition[k][2][0]
                        del stack[0]
                        stack.reverse()
                        for l in range(len(transition[k][2][1])):
                            if transition[k][2][1][l]!='$':
                                stack.append(transition[k][2][1][l])
                        if len(stack)==0:
                                stack.append('$')
                        stack.reverse()
                        outputString=outputString+str(currentState)+'#'
                        for m in range(len(stack)):
                            outputString=outputString+str(stack[m])
                        outputString=outputString+'|'
                        if len(stack)==1:
                                if stack[0]=='$':
                                    del stack[0]
                        flag1=1
                        break
            if(flag1==0):
                flag2=1
                flag3=0
                while (flag2==1 and flag3==0):
                    flag2=0
                    for k in range(len(transition)):
                        if len(stack)>0:
                            if currentState==transition[k][0] and '$'==transition[k][1][0] and stack[0]==transition[k][1][1]:
                                currentState=transition[k][2][0]
                                flag2=1
                                del stack[0]
                                stack.reverse()
                                for l in range(len(transition[k][2][1])):
                                    if transition[k][2][1][l]!='$':
                                        stack.append(transition[k][2][1][l])
                                if len(stack)==0:
                                       stack.append('$')
                                stack.reverse()
                                outputString=outputString+str(currentState)+'#'
                                for m in range(len(stack)):
                                    outputString=outputString+str(stack[m])
                                outputString=outputString+'|'
                                if len(stack)==1:
                                    if stack[0]=='$':
                                        del stack[0]
                                break
                    if (flag2==1):
                        for k in range(len(transition)):
                            if len(stack)>0:
                                if currentState==transition[k][0] and inSequence[i][j]==transition[k][1][0] and stack[0]==transition[k][1][1]:
                                    currentState=transition[k][2][0]
                                    del stack[0]
                                    stack.reverse()
                                    for l in range (len(transition[k][2][1])):
                                        if transition[k][2][1][l]!='$':
                                            stack.append(transition[k][2][1][l])
                                    if len(stack)==0:
                                        stack.append('$')
                                    stack.reverse()
                                    outputString=outputString+str(currentState)+'#'
                                    for m in range(len(stack)):
                                        outputString=outputString+str(stack[m])
                                    outputString=outputString+'|'
                                    if len(stack)==1:
                                        if stack[0]=='$':
                                            del stack[0]
                                    flag3=1
                                    break
                    if (flag2==0):
                        outputString=outputString+'fail|0'
                        flag5=5
            if(flag5==5):
                break
                        
        flag4=0
        if(flag1==1 or flag3==1 and flag5==0):
            if currentState in acceptable:
                outputString=outputString+'1'
                flag4=1
        if((flag1==1 or flag3==1) and flag4==0):
            flag2=1
            while(flag2==1):
                flag2=0
                for k in range(len(transition)):
                    if len(stack)>0:
                        if currentState==transition[k][0] and '$'==transition[k][1][0] and stack[0]==transition[k][1][1]:
                            flag2=1
                            currentState=transition[k][2][0]
                            del stack[0]
                            stack.reverse()
                            for l in range(len(transition[k][2][1])):
                                 if transition[k][2][1][l]!='$':
                                    stack.append(transition[k][2][1][l])
                            if len(stack)==0:
                                stack.append('$')
                            stack.reverse()
                            outputString=outputString+str(currentState)+'#'
                            for m in range(len(stack)):
                                outputString=outputString+str(stack[m])
                            outputString=outputString+'|'
                            if len(stack)==1:
                                if stack[0]=='$':
                                    del stack[0]
                            break
                if currentState in acceptable:
                        outputString=outputString+'1'
                        break
                if flag2==0:
                    outputString=outputString+'0'
                    break                         
                
        print outputString
main()
   
