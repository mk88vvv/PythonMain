file1 = open("dataru.txt")
file2 = open("datanew.txt","w")
a="one"
b="two"
c="three"
d="four"
e="five"
a1="ODIN"
b1="два"
c1="TRU"
d1="четыре"
e1="пять"
words=[[a,a1],[b,b1],[c,c1],[d,d1],[e,e1]]
for line in file1:
    for i in range(len(words)):
        i1=words[i][0]
        i2=words[i][1]
        line=line.replace(i1,i2)
    file2.write(line)
    
    

