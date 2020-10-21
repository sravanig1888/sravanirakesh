l=[1,2,3,4,5,7]
print (l)
a=l[1]
l.remove(l[1])
print (l)
b=l[4]
l.remove(l[4])
print (l)
l.insert(1,b)
print (l)
l.insert(4,a)
print (l)




f=open("C:\\Users\\srgajjel\\Desktop\\count.txt","r+")
wordcount={}
for word in f.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
f.close();
