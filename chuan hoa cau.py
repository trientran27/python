doc=''
while True:
    try:
        doc+=input()
        if doc[-1] not in '.?!':
            doc+=' .'
        else:
            if doc[-2]!=' ':
                doc=f'{doc[:-1]} {doc[-1]}'
        doc+=' '
    except:
        break
words = doc.split()
i=0
while i<len(words):
    res=''
    while i<len(words) and words[i] not in '.!?':
        res+=words[i]+' '
        i+=1
    if words[i] in '.!?':
        res=res[:-1]+words[i]
    i+=1
    print(res[0].upper()+res[1:].lower())