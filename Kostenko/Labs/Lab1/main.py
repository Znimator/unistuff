data = ['a','b','c']

def checkChoice(choice: str, word: str) -> str:
    k = 0
    for v in choice:
        if v in word:
            k += 1
            if k >= 2:
                return word

def checkDuplicate(duplicate: int, word: str) -> str:
    lastLetter = ""
    k = 0

    for v in word:
        if v != lastLetter:
            v = lastLetter
            k += 1
        else:
            break

    if k >= duplicate:
        return word

def checkDifferent(different: bool, word: str) -> str:
    word = word.lower()
    
    pass

def checkFSort(f_sort: bool, data: list) -> list:
    
    pass

def processing_words(passingData: list, choice: str, duplicate: int, differents: bool, f_sort: bool) -> list:

    pass

newData = processing_words(data)
print(newData)