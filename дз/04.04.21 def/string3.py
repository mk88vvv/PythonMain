string = 'молоко капуста'
word1=string[0:string.index(' ')]
word2=string[string.index(' '):]
newstring=word2+' '+word1
print(newstring)
