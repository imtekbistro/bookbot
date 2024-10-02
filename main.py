def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = wordCount(text)
    character_counts = charCount(text)


    print(text)
    print(f"{words} words found in the document")
    print(character_counts)


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

main()