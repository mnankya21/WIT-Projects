vowels="aeiou"

count=0
word="Hello How are you?"
for i in word:
    if i in vowels:
        count=count+1
print(count)