bad_words='hello black circle write square'
sentence='Writer writes: “Hello, my black circle. I want go to red square.”'
words=bad_words.split()
sentence2=sentence.lower()
for i in range(len(words)):
    sentence2=sentence2.replace(words[i],'*****')
print(sentence2)





