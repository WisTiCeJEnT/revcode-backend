import deepcut
import dialogflow_api
import detection
def dialogflow(s):
    return s
def grammar(s):
    list_word = deepcut.tokenize(s)
    ans=[]
    for word in list_word:
        ans.append(dialogflow_api.detect_intent_texts(word))
    detection.tran(ans,0)
    return ans

'''
stringpattern='ข้อความ'
intpattern='ตัวเลข'
printpattern='พิมพ์'
test='พิมพ์ข้อความควายกัดหมา'
test2='ตัวแปรxเท่ากับข้อความควายกัดหมา'
keyword=[]
keyword.append((stringpattern,intpattern,printpattern))
z=[]
x=cutword(test2)
j=0
k=0
for i in x:
    if i in keyword[0]:
        z.append(i)
        j+=1
        k+=1
    elif len(z)==j:
        z.append(x[j])
    else:
        z[k]+=x[j+1]
        j+=1
print(x)
print(z)
#if 'เท่า' in x and 'กับ' in x and 'ข้อความ' in x:   
#z=z1.split('แสดงผล')
'''
