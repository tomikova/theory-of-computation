import sys

def S(_list,output,stop):
    hlp=[_list,output,stop]
    if stop==0:
        output=output+'S'
        hlp=[_list,output,stop]
        if _list[0]=='a':
            del _list[0]
            hlp=A(_list,output,stop)
            _list=hlp[0]
            output=hlp[1]
            stop=hlp[2]
            hlp=B(_list,output,stop)
            _list=hlp[0]
            output=hlp[1]
            stop=hlp[2]
        elif _list[0]=='b':
            del _list[0]
            hlp=B(_list,output,stop)
            _list=hlp[0]
            output=hlp[1]
            stop=hlp[2]
            hlp=A(_list,output,stop)
            _list=hlp[0]
            output=hlp[1]
            stop=hlp[2]
        else:
            stop=1
            hlp=[_list,output,stop]
    return hlp
        
def A(_list,output,stop):
    hlp=[_list,output,stop]
    if stop==0:
        output=output+'A'
        hlp=[_list,output,stop]
        if _list[0]=='b':
            del _list[0]
            hlp=C(_list,output,stop)
            _list=hlp[0]
            output=hlp[1]
            stop=hlp[2]
        elif _list[0]=='a':
            del _list[0]
            hlp=[_list,output,stop]
        else:
            stop=1
            hlp=[_list,output,stop]
    return hlp

def B(_list,output,stop):
    hlp=[_list,output,stop]
    if stop==0:
        output=output+'B'
        hlp=[_list,output,stop]
        if len(_list)>=3:
            if _list[0]=='c' and _list[1]=='c':
                del _list[0]
                del _list[0]
                hlp=S(_list,output,stop)
                _list=hlp[0]
                output=hlp[1]
                stop=hlp[2]
                if len(_list)>=3 and stop==0:
                    if _list[0]=='b' and _list[1]=='c':
                        del _list[0]
                        del _list[0]
                        hlp=[_list,output,stop]
                    else:
                        stop=1
                        hlp=[_list,output,stop]
                else:
                        stop=1
                        hlp=[_list,output,stop]
    
    return hlp

def C(_list,output,stop):
    hlp=[_list,output,stop]
    if stop==0:
        output=output+'C'
        hlp=[_list,output,stop]
        hlp=A(_list,output,stop)
        _list=hlp[0]
        output=hlp[1]
        stop=hlp[2]
        hlp=A(_list,output,stop)
    return hlp
    

def main():
   
    rows = [row[:] for row in sys.stdin.readlines()]
    _list=list(rows[0])
    output=''
    stop=0
    hlp=[_list,output,stop]
    hlp=S(_list,output,stop)
    if hlp[0][0]=='\n' and len(hlp[0])==1 and hlp[2]==0:
        print hlp[1]
        print 'YES'
    elif len(hlp[0])>1 or hlp[2]==1:
        print hlp[1]
        print 'NO'
        
    
main()    
