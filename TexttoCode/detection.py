mylist=[['while','asdf'],['ข้างในลูป'],['print','ข้อความ', 'x'],
['for','ตัวแปร','i','ใน','ช่วง','1','ถึง','9'],
['ข้างในลูป'],
['print','ข้อความ','ควายกัดหมา'],
['ตัวแปร','x' ,'เท่ากับ','x','*','9'],
['ข้างนอกลูป'],['elif','ตัวแปร','x','เท่ากับ','1'],
['ข้างในลูป'],['print','ตัวแปร','x+1'],['ข้างนอกลูป'],
['print','ตัวแปร', 'x'],

['ประกาศ','ตัวแปร','x' ,'เท่ากับ','ตัวแปร','y','+','ตัวแปร','z','+','1']]

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
        
    if(('if'  in i) or ('elif'  in i) or ('while' in i)) : ## if       
        if('if' in i ):
            answer+=f'if '
        if('elif' in i):
            answer+=f'elif '
        if('while' in i):
            answer+=f'while'
        if ('ตัวแปร' in i) :
            order0=i.index('ตัวแปร')
            answer+=f'{i[order0+1]} '
            if('มากกว่า' in i):
                order1=i.index('มากกว่า')
                answer+=f'>'
                if(i[order1+1] == 'เท่ากับ'):                   
                    answer+=f'='
                answer+=' '
                for n in range(order1+2,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]} '
            elif('น้อยกว่า' in i):
                order1=i.index('น้อยกว่า')
                answer+=f'<'
                if(i[order1+1] == 'เท่ากับ'):
                    answer+=f'='
                answer+=' '
                for n in range(order1+2,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]} '
                
            elif('เท่ากับ' in i):
                order1=i.index('เท่ากับ')
                answer+=f'== '
                for n in range(order1+1,len(i)):  
                    if(i[n]=='ตัวแปร'):
                        continue
                    answer+=f'{i[n]} '
                
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
    if ('print' in i): ## print
        answer+=f'print'      
        if('ตัวแปร' in i):
            order0=i.index('ตัวแปร')
            for n in range(order0+1,len(i)):  
                if(i[n]=='ตัวแปร'):
                    continue
                answer+=f'{i[n]} '
        elif('ข้อความ' in i):
            order0=i.index('ข้อความ')
            answer+=f"('{i[order0+1]}')"
   
    if(i[0]=='ประกาศ' or i[0]=='ตัวแปร') : ## declar
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
