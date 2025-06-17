from stats import get_num_words, count_chars, sort_on_count

def main():
    # Grab entire book text as string
    book_text = get_book_text("books/frankenstein.txt")

    # Calculate
    word_count = get_num_words(book_text)
    lchar_counts = count_chars(book_text)

    # Report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # Convert to list of dictionaries
    lchar_counts_list = [{'char': k, 'count': v} for k, v in lchar_counts.items()]
    lchar_counts_list.sort(reverse=True, key=sort_on_count)
    print()
    for count_entry in lchar_counts_list:
        if count_entry['char'].isalpha():
            print(f"{count_entry['char']}: {count_entry['count']}")
    
    print('============= END ===============')

def get_book_text(filepath):
    with open("books/frankenstein.txt") as f:
        # Ingest
        file_contents = f.read()
        return file_contents


main()