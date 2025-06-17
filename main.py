from stats import get_num_words, count_chars, sort_on_count
import sys

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Grab entire book text as string
    book_text = get_book_text(book_path)

    # Calculate
    word_count = get_num_words(book_text)
    lchar_counts = count_chars(book_text)

    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
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
    with open(filepath) as f:
        # Ingest
        file_contents = f.read()
        return file_contents


main()