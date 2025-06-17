from stats import get_num_words, count_chars

def main():
    with open("books/frankenstein.txt") as f:
        # Ingest
        file_contents = f.read()

        # Calculate
        word_count = get_num_words(file_contents)
        lchar_counts = count_chars(file_contents)

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

def sort_on_count(dict):
    return dict['count']

main()