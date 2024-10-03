def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = wordCount(text)
    character_counts = charCount(text)
    charsSortedList = charCountToSortedList(character_counts)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for y in charsSortedList:
        if not y["char"].isalpha():
            continue
        print(f"The '{y['char']}' character was found {y['num']} times")

    print("--- End report ---")


       


def get_book_text(path):
    with open(path) as f:
        return f.read()

def wordCount(path):
    words = path.split()
    return len(words)

def charCount(text):
    lowerString = text.lower()
    chars = {}
    for letter in lowerString:
        if letter not in chars:
            chars[letter] = 1
        else:
            chars[letter] += 1
    return chars

def charCountToSortedList(charCountDict):
    sortedList =[]
    for x in charCountDict:
        sortedList.append({"char":x, "num":charCountDict[x]})
    sortedList.sort(reverse=True, key=sortChars)
    return(sortedList)

def sortChars(dict):
    return dict["num"]

main()