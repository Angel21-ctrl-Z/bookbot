def main():
    file = 'github.com/Angel21-ctrl-Z/bookbot/books/frankenstein.txt'
    text = read_file(file)
    n_w = len(text.split())
    c_d = char_dict(text)
    char_ls = chars_sorted_ls(c_d)
    create = open('github.com/Angel21-ctrl-Z/bookbot/output.txt', 'w')
    create.write(f" --- Begin report of {file} ---" + '\n')
    create.write(f"{n_w} words found in the document" + '\n')
    print(f" --- Begin report of {file} ---")
    print(f"{n_w} words found in the document")
    
    for item in char_ls:
        if not item["char"].isalpha():
            continue
        create.write(f"The '{item['char']} character was found {item['num']} times" + '\n')
        print(f"The '{item['char']} character was found {item['num']} times")
    create.write("--- End report ---")
    print("--- End report ---")
    print(" --- saved results ---")

def sort_on(d):
    return d["num"]

def chars_sorted_ls(char_dict):
    sorted_ls = []
    for ch in char_dict:
        sorted_ls.append({"char": ch, "num": char_dict[ch]})
    sorted_ls.sort(reverse=True, key=sort_on)
    return sorted_ls

def char_dict(text):
    char = {}
    for c in text:
        low = c.lower()
        if low in char:
            char[low] += 1
        else:
            char[low] = 1
    return char

def read_file(file):
    with open(file) as f:
        return f.read()

main()