mylist=[['while','asdf'],['ข้างในลูป'],['print','ข้อความ', 'x'],['for','ตัวแปร','i','ใน','ช่วง','1','ถึง','9'],['ข้างในลูป'],['print','ข้อความ','ควายกัดหมา'],['ข้างนอกลูป'],['elif','ตัวแปร','x','เท่ากับ','1'],['ข้างในลูป'],['print','ตัวแปร','x+1'],['ข้างนอกลูป'],['print','ตัวแปร', 'x'],['ประกาศ','ตัวแปร','x' ,'เท่ากับ','ตัวแปร','y','+','ตัวแปร','z','+','1']]

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

    if 'while' in i  : ## while
        answer+=f'while '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('มากกว่า' in i):
                order1=i.index('มากกว่า')
                answer+=f'>'
                if(i[order1+1] == 'เท่ากับ'):
                    order1+=1
                    answer+=f'='
                answer+=' '
                answer+=f'{i[order1+1]}'
            elif('น้อยกว่า' in i):
                order1=i.index('น้อยกว่า')
                answer+=f'<'
                if(i[order1+1] == 'เท่ากับ'):
                    order1+=1
                    answer+=f'='
                answer+=' '
                answer+=f'{i[order1+1]}'
            elif('เท่ากับ' in i):
                order1=i.index('เท่ากับ')
                answer+=f'== '
                answer+=f'{i[order1+1]}'
            elif('ใน' in i):
                order1=i.index('ใน')
                answer+=f'in {i[order1+1]}'
        else :
            order0=i.index('while')
            answer+=f'{i[order0+1]}'
        answer+=f' :'    
        
    if(('if'  in i) or ('elif'  in i) ) : ## if
        print('qqqqqqqqqqqq')
        if('if' in i ):
            answer+=f'if '
        if('elif' in i):
            answer+=f'elif '
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('มากกว่า' in i):
                order1=i.index('มากกว่า')
                answer+=f'>'
                if(i[order1+1] == 'เท่ากับ'):
                    order1+=1
                    answer+=f'='
                answer+=' '
                answer+=f'{i[order1+1]}'
            elif('น้อยกว่า' in i):
                order1=i.index('น้อยกว่า')
                answer+=f'<'
                if(i[order1+1] == 'เท่ากับ'):
                    order1+=1
                    answer+=f'='
                answer+=' '
                answer+=f'{i[order1+1]}'
            elif('เท่ากับ' in i):
                order1=i.index('เท่ากับ')
                answer+=f'== '
                answer+=f'{i[order1+1]}'
            if('ใน' in i):
                order1=i.index('ใน')
                answer+=f'in {i[order1+1]}' 
        if('ข้อความ' in i):
            order0=i.index('ข้อความ')
            answer+=f"'{i[order0+1]}' "
            if('ใน' in i):
                order1=i.index('ใน')
                answer+=f'in {i[order1+1]}' 
        answer+=f' :'
    if('ประกาศ' in i) : ## declar
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} = '
            if('ข้อความ' in i):
                answer+=f'{i[order0+3]}'
            else:
                for n in range(order0+3,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]} '


    if ('print' in i): ## print
        answer+=f'print'      
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            answer+=f'({i[order0+1]})'
        elif('ข้อความ' in i):
            order0=i.index('ข้อความ')
            answer+=f"('{i[order0+1]}')"
    return (answer, tab)


    