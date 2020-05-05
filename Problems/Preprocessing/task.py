phrase = input()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in phrase:
    if x in punctuations:
        phrase = phrase.replace(x, '')

print(phrase.lower())
