def get_verse(book, chapter, verse, filename="bible.txt.txt"):
    with open("bible.txt.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        if f"{book} {chapter}:{verse}" in line:
            return line.strip()
    
    return f"Verse not found: {book} {chapter}:{verse}"

def main():
    book = input("Enter the name of book: ")
    chapter = input("Enter the name of the chapter: ")
    verse = input("Enter the verse: ")

    result = get_verse(book, chapter, verse)

    print(result)

if __name__ == "__main__":
    main()