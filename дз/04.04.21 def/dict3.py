dict={"Hello":"Hi","Bye":"Goodbye","List":"Array"}
dict2=dict.copy()
for key in dict2:
    dict[dict2[key]]=key
print(dict)
