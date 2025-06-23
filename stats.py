def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    letters = {}
    myText = text.lower()
    for letter in myText:
        if letter.isalpha():  # Optional: count only letters
            letters[letter] = 1 + letters.get(letter, 0)
    return sort_dictionary(letters)

def sort_on(item):
    return item["num"]

def sort_dictionary(d):
    list_of_dicts = [{"letter": key, "num": value} for key, value in d.items()]
    return sorted(list_of_dicts, key=sort_on, reverse=True)
