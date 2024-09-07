def main():
    with open("books/frankenstein.txt") as f:
        # Ingest
        file_contents = f.read()

        # Calculate
        words = file_contents.split()
        word_count = len(words)
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

def count_chars(str):
    lchar_counts = {}
    for lchar in str.lower():
        if lchar in lchar_counts:
            lchar_counts[lchar] += 1
        else:
            lchar_counts[lchar] = 1
    return lchar_counts

def sort_on_count(dict):
    return dict['count']

main()