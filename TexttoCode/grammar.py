import deepcut
import dialogflow_api
import detection
'''
def greater(lis):
    ans=[]
    i=0
    while i<len(lis):
        if lis[i]=='มาก' and lis[i+1]=='กว่า':
            ans.append('')
            ans[i]=ans[i].replace('','มากกว่า')
            i+=2
        else:
            ans.append(lis[i])
            i+=1
'''
def grammar(s):
    x = deepcut.tokenize(s)
    #x=grammar(s)
    ans=[]
    stringans=''
    check=False
    for i in x:
        if check:
            stringans+=i
            continue
        if i!='ข้อความ':
            check=False
            ans.append(dialogflow_api.detect_intent_texts(i))
        else:
            check=True
            ans.append(i)
    #greater(ans)
    #lesser(ans)
   # equal(ans)

    print(ans)
    ans.append(stringans)
    ans = detection.tran(ans,0)
    return ans

#print(grammar('สวัสดีครับมากกว่าข้อความมากกว่านี้มาจากจุ้ยเอง'))
#dialogflow_api.detect_intent_texts(i)