school={"1a":30,"1b":28,"2b":26,"7v":33}
school["1a"]=29
school["1g"]=25
school.pop("1a")
c=0
for key in school:
    c+=school[key]
print(c)