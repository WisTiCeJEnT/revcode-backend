import deepcut
import dialogflow_api
import detection
CAREFUL_WORD = [['มาก', 'กว่า'], ['น้อย', 'กว่า']]
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
    return ans

def grammar(s):
    x = deepcut.tokenize(s)
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
    ans = mergecarefulword(ans)
    ans.append(stringans)
    ans = detection.tran(ans,0)
    return ans

#