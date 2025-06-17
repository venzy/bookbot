from stats import get_num_words, count_chars

def main():
    # Grab entire book text as string
    book_text = get_book_text("books/frankenstein.txt")

    # Calculate
    word_count = get_num_words(book_text)
    lchar_counts = count_chars(book_text)

    # Report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    # Convert to list of dictionaries
    lchar_counts_list = [{'char': k, 'count': v} for k, v in lchar_counts.items()]
    lchar_counts_list.sort(reverse=True, key=sort_on_count)
    print()
    for count_entry in lchar_counts_list:
        if count_entry['char'].isalpha():
            print(f"The \'{count_entry['char']}\' character was found {count_entry['count']} times")
    
    print('--- End report ---')

def get_book_text(filepath):
    with open("books/frankenstein.txt") as f:
        # Ingest
        file_contents = f.read()
        return file_contents


def sort_on_count(dict):
    return dict['count']

main()