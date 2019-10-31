import deepcut
import dialogflow_api
import detection
import sys
sys.path.insert(1, '../')
import firebase_api

constant = firebase_api.load_carefulword()
CAREFUL_WORD = constant["careful_word"]#[['มาก', 'กว่า'], ['น้อย', 'กว่า'], ['เท่า', 'กับ'], ['ตัว', 'แปร']]
firstpriority = constant["firstpriority"]#['มากกว่า','น้อยกว่า','เท่ากับ','ตัวแปร']
def mergecarefulword(lis):
    for j in range (len(CAREFUL_WORD)):
        i=0
        ans=[]
        while i<len(lis):
            if lis[i]==CAREFUL_WORD[j][0] and lis[i+1]==CAREFUL_WORD[j][1]:
                ans.append('')
                ans[i]=ans[i].replace('',CAREFUL_WORD[j][0]+CAREFUL_WORD[j][1])
                i+=2
            else:
                ans.append(lis[i])
                i+=1
        lis=ans
    realans=[]
    for i in ans:
        if i==' ' or i=='':
            pass
        else:
            realans.append(i)
    return realans

def grammar(s, indent):
    for i in range (len(firstpriority)):
        if firstpriority[i] in s:
            s=s.replace(firstpriority[i],' '+firstpriority[i]+' ')
    x = deepcut.tokenize(s)
    newarrayfordeepcut=[]
    for i in x:
        if i==' ' or i=='':
            pass
        else:
            newarrayfordeepcut.append(i)
    ans=[]
    stringans=''
    check=False
    for i in newarrayfordeepcut:
        if check:
            stringans+=i
            continue
        if i!='ข้อความ':
            check=False
            ans.append(i)
        else:
            check=True
            ans.append(i)
    ans.append(stringans)
    ans = mergecarefulword(ans)
    before_detect = []
    before_df = ans
    for i in ans:
        before_detect.append(dialogflow_api.detect_intent_texts(i))
    ans = detection.tran(before_detect, indent)
    return (ans[0], ans[1], before_df, before_detect)
