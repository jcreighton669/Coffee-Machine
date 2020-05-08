consonant = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
string = input()

for ch in string:
    if ch in consonant:
        print("consonant")
    elif ch in vowels:
        print("vowel")
    else:
        break
