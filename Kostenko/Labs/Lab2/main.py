data = ["apple", "banana", "cherry", "dog", "elephant", "fish", "giraffe", "hat", "icecream", "jungle", 
         "kangaroo", "lion", "mmonkey", "notebook", "orange", "penguin", "queen", "rabbit", "sun", "tiger"]

def check_choice(argument = None, strings = None) -> list:
    if argument:
        selected_strings = [s for s in strings if any(c.lower() in s.lower() for c in argument)]
    else:
        selected_strings = [s for s in strings if len(set(s)) != len(s)]
    
    return selected_strings

def check_duplicate(duplicate: int, data: list) -> list:
    lastLetter = ""
    k = 0

    for v in data[0]:
        if v != lastLetter:
            v = lastLetter
            k += 1
        else:
            break

    if k >= duplicate:
        return [data[0]]

def check_differents(differents: bool, data: list) -> list:
    toReturn = []

    for word in data:
        word = word.lower()
        if differents == True and word[0] != word[1]:
            toReturn.append(word)
        elif differents == False and word[0] == word[1]:
            toReturn.append(word)

    return toReturn

def check_fsort(f_sort: bool, data: list) -> list:
    if f_sort:
        return sorted(data, key=len)
    else:
        return sorted(data, key=len, reverse=True)

def processing_words(passingData: list, choice: str = None, duplicate: int = None, differents: bool = None, f_sort: bool = None) -> list:
    toReturn = passingData

    if choice != None:
        toReturn = check_choice(choice, toReturn)
        print(toReturn)
    if duplicate != None:
        toReturn = check_duplicate(duplicate, toReturn)
        print(toReturn)
    if differents != None:
        toReturn = check_differents(differents, toReturn)
        print(toReturn)
    if f_sort != None:
        toReturn = check_fsort(f_sort, toReturn)
        print(toReturn)

    return list(toReturn)

newData = processing_words(data, f_sort=False, differents=True)
print(newData)
