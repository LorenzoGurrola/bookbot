def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)
    report = create_report(relative_path, word_count, letter_counts)
    print(report)

def get_book_text(relative_path):
    with open(relative_path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letter_dict = {}
    for c in book_text:
        c = c.lower()
        if(c in letter_dict):
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1
    return letter_dict

def convert_dictionary(dict):
    dict = removeNonAlphabetCharacters(dict)
    list_of_dict = []
    for key in dict:
        new_dict = {"letter": key, "occurrences": dict[key]}
        list_of_dict.append(new_dict)
    return list_of_dict

def removeNonAlphabetCharacters(dict):
    keys_to_remove = []
    for key in dict:
        if not key.isalpha():
            keys_to_remove.append(key)
    for key in keys_to_remove:
        if key in dict:
            del dict[key]
    return dict

def letter_occurrences(dict):
    return dict["occurrences"]

def format_dictionary(letter_counts):
    formmatted_list = []
    for dict in letter_counts:
        s = f"The letter {dict["letter"]} was found {dict["occurrences"]} times"
        formmatted_list.append(s)

    return formmatted_list

def create_report(relative_path, word_count, letter_counts):
    letter_counts = convert_dictionary(letter_counts)
    letter_counts.sort(reverse=True, key=letter_occurrences)
    letter_counts_formatted = format_dictionary(letter_counts)

    report = "\n--- Begin report of " + relative_path + " ---"
    report += "\n" + str(word_count) + " words found in the document"
    for line in letter_counts_formatted:
        report += "\n" + line
    report += "\n--- End report ---"
    return report



main()