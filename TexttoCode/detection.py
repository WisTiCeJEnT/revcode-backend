def tran(i, tab):
    answer='\t'*tab  
    if('ข้างใน' in i):
        tab+=1
        return (None, tab)
    if('ข้างนอก' in i):
        tab-=1
        return (None, tab)
    if ('for' in i) : ## for
        answer+=f'for '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('ในช่วง' in i):
                order1=i.index('ในช่วง')
                answer+=f'in range({i[order1+1]},{i[order1+3]})'
            elif('ตั้งแต่' in i):
                order1=i.index('ตั้งแต่')
                answer+=f'in range({i[order1+1]},{i[order1+3]})'
            elif('ใน' in i):
                order1=i.index('ใน')
                for n in range(order1+1,len(i)):  
                    answer+=f'in {i[n]}'
        answer+=f':' 
        
    if(('if'  in i) or ('elif'  in i) or ('while' in i)) : ## if       
        if('if' in i ):
            answer+=f'if '
        if('elif' in i):
            answer+=f'elif '
        if('while' in i):
            answer+=f'while '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('>' in i):
                order1=i.index('>')
                answer+=f'>'
                if(i[order1+1] == '='):                   
                    answer+=f'='
                else:
                    answer+=f' {i[order1+1]}'
                answer+=' '
                if(len(i) > order1+2):
                    for n in range(order1+2,len(i)):  
                        if(i[n]=='ตัวแปร'):
                            continue
                        if(i[n]=='<'):
                            answer+=f'<'
                            continue
                        elif(i[n]=='>'):
                            answer+=f'>'
                            continue
                        if(i[n]=='='):
                            answer+=f'='
                            continue
                        answer+=f' {i[n]} '
            elif('<' in i):
                order1=i.index('<')
                answer+=f'<'
                if(i[order1+1] == '='):
                    answer+=f'='
                else:
                    answer+=f'{i[order1+1]}'
                answer+=' '
                if (len(i) > order1+2):
                    for n in range(order1+2,len(i)):  
                        if(i[n]=='ตัวแปร'):
                            continue
                        if(i[n]=='<'):
                            answer+=f'<'
                            continue
                        elif(i[n]=='>'):
                            answer+=f'>'
                            continue
                        if(i[n]=='='):
                            answer+=f'='
                            continue
                        answer+=f' {i[n]} '
                
            elif('=' in i):
                order1=i.index('=')
                answer+=f'== '
                for n in range(order1+1,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]} '
                
            if('ใน' in i):
                order1=i.index('ใน')
                answer+=f'in {i[order1+1]}'  
        answer+=f' :'
    if ('print' in i): ## print
        answer+=f'print'      
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            for n in range(order0+1,len(i)):  
                if(i[n]=='ตัวแปร'):
                    continue
                answer+=f'({i[n]})'
        elif('ข้อความ' in i):
            order0=i.index('ข้อความ')
            answer+=f"('{i[order0+1]}')"
   
    if(i[0]=='ประกาศ' or i[0]=='ตัวแปร' ) : ## declar
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} = '
            if('ข้อความ' in i):
                answer+=f'{i[order0+4]}'
            else:
                for n in range(order0+3,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]}'

    return (answer, tab)
"""
tab=0
listans=[]
for i in mylist:
    ans, tab = tran(i, tab)
    listans.append(ans)
##print(listans)
for i in listans:
    if i:
        print(i)
"""
