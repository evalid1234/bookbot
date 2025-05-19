def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    alphabet_dictionary = {}
    for char in text: 
        if char.isalpha():
            char = char.lower()
        if char in alphabet_dictionary:
            alphabet_dictionary[char] += 1
        else:
            alphabet_dictionary[char] = 1
    return alphabet_dictionary

def sorted_dicts(dict):
    res= []
    for key, value in dict.items():
         if key.isalpha():
            temp = {}
            # make a dictionary of the character and its count and add it to the list directly
            temp["char"] = key
            temp["num"] = value
            res.append(temp)
    
    res.sort( key=lambda x: x["num"], reverse=True)
    return res
export = word_count, char_count, sorted_dicts