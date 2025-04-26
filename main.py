from stats import word_counter
from stats import character_counter
from stats import sorting
import sys

#def get_filepath(bookpath):
    

def get_book_text (filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(text)} total words")
    print("--------- Character Count -------")
    #print(sorting(character_counter(text)))
    tolle_liste = sorting(character_counter(text))
    for letter in tolle_liste:
        #print(letter)
        print(f"{letter["Letter"]}: {letter["count"]}")
    print("============= END ===============")

main()