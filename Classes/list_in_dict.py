favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name in favorite_languages.keys():
    print(name.title()+" Favrate languages are")
    if(len(favorite_languages[name])>1):
        for lang in favorite_languages[name]:
            print("\t"+lang+" ")
    else:
        print("learn more languages")

