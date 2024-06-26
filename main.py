def main():
    book_path = 'github.com/Angel21-ctrl-Z/bookbot/books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sort = chars_sorted_ls(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in chars_sort:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_sorted_ls(num_chars_dict):
    sorted_ls = []
    for ch in num_chars_dict:
        sorted_ls.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_ls.sort(reverse=True, key=sort_on)
    return sorted_ls

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
