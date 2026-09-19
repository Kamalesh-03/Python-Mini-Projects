word = input("Enter a word: ")

reverse = ""

for i in word:
    reverse = i + reverse

if word == reverse:
    print("output success")

else:
    print("Not success")