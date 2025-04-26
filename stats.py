def word_counter (text):
    total_words = 0
    words = text.split()
    for word in words:
        total_words += 1
    return total_words

def character_counter(text):
    text = text.lower()
    characters = {}
    words = text.split()
    for word in words:
        #print(word)
        for letter in word:
            #print(letter)
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sorting(dictonary):
    #dictonary.sort(reverse=True, key=None)
    buchstaben = []
    for letter in dictonary:
        buchstaben.append({"Letter": letter, "count": dictonary[letter]})
    buchstaben.sort(reverse=True, key=sort_on)
    return buchstaben