def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    
    print(f"{num_words} words found in the document")
    print(f"{letter_count}'s found in the document")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_count(text):
    letters = text.lower()
    counts = {}
    for letter in letters:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    return counts
        


main()