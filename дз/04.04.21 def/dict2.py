string1 = "one two one tho three"
string1=string1.split()

dict = {}
for i in range (len(string1)):
    if string1[i] in dict:
        dict[string1[i]] += 1
    else:
        dict[string1[i]] = 1

print(dict)
