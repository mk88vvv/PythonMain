string1='In the hole in the ground there lived a hobbit'
string2=string1[string1.index('h'):string1.rindex('h')]
string2=string2[::-1]
string3=string1[:string1.index('h')+1]+string2+string1[string1.rindex('h')-1:]
print(string3)
