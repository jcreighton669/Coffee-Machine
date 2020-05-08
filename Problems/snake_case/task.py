phrase = input()
translation = ""
for i in phrase:
    if i.islower():
        translation = translation + i
    if i.isupper():
        translation = translation + "_" + i.lower()

print(translation)
