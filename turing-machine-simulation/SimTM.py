import sys

def main():
    
    rows = [row[:-1] for row in sys.stdin.readlines()]

    states=rows[0].split(',')
    symbols=rows[1].split(',')
    symbolTape=rows[2].split(',')
    _empty=rows[3]
	tape=[]
    for i in range (len(rows[4])):
        tape.append(rows[4][i])
    acceptable=rows[5].split(',')
    start=rows[6]
    headStart=int(rows[7])
    transition =[]
    for i in range(len(rows)):
        if i>7:
            stateDefinition=rows[i]
            current=stateDefinition[:stateDefinition.find(',')]
            trans=stateDefinition[stateDefinition.find(',')+1:stateDefinition.find('->')]
            next=stateDefinition[stateDefinition.find('->')+2:].split(',')
            transition.append([current,trans,next])
    flag=1
    while(1):     
       if flag==1:
           flag=0
           for i in range(len(transition)):
               if transition[i][0]==start and transition[i][1]==tape[headStart]:
                   if (headStart==0 and transition[i][2][2]=='L') or (headStart==(len(tape)-1) and transition[i][2][2]=='R'):
                       flag=0;
                       break;
                   else:
                       tape[headStart]=transition[i][2][1]
                       if transition[i][2][2]=='L':
                           headStart=headStart-1
                       elif transition[i][2][2]=='R':
                           headStart=headStart+1
                       start=transition[i][2][0]
                       flag=1
                       break;
       else:
            break;

    outputString=str(start)+'|'+str(headStart)+'|'
    for i in range(len(tape)):
        outputString=outputString+str(tape[i])
    if start in acceptable:
        outputString=outputString+'|1'
    else:
        outputString=outputString+'|0'
    print outputString
            
main()
