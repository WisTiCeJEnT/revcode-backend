mylist=[['loop','for','ตัวแปร','x','ใน','ช่วง','welist','','asd'],['ข้างในลูป'],['print','สตริง', 'x'],['ข้างนอกลูป'],['print','ตัวแปร', 'x']]

def tran(i, tab):
    if('ข้างในลูป' in i):
        tab+=1
        return (None, tab)
    if('ข้างนอกลูป' in i):
        tab-=1
        return (None, tab)
    answer='\t'*tab   
    if ('for' in i) : ## for
        answer+=f'for '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if(('ใน' and 'ช่วง') in i):
                order1=i.index('ช่วง')
                answer+=f'in range({i[order1+1]},{i[order1+3]})'
            elif('ใน' in i):
                order1=i.index('ใน')
                answer+=f'in {i[order1+1]}'
        answer+=f':'
    if('while' in i ) : ## while
        answer+=f'while '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('มากกว่า' in i):
                order1=i.index('มากกว่า')
                answer+=f'>'
                if(i[order1+1] == 'เท่ากับ'):
                    order2=i.index('เท่ากับ')
                    answer+=f'='
                answer+=' '
            if('น้อยกว่า' in i):
                order1=i.index('น้อยกว่า')
                answer+=f'<'
                if(i[order1+1] == 'เท่ากับ'):
                    order2=i.index('เท่ากับ')
                    answer+=f'='
                answer+=' '
            if('เท่ากับ' in i):
                order2=i.index('เท่ากับ')
                answer+=f'= '
            answer+=f'{i[order2+1]}'
            
    if('if' in i ) : ## if
        answer+=f'if '

    if ('print' in i): ## print
        answer+=f'print'      
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            answer+=f'({i[order0+1]})'
        elif('สตริง' in i):
            order0=i.index('สตริง')
            answer+=f"('{i[order0+1]}')"
    return (answer, tab)

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
    if any('loop while' in s for s in i):
        print('while ')

    if ('if' in i):
        print('if ')

    if ('if else' in i):
        print('if else ')

    if ('else' in i):
        print('else ')

    """