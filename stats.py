def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def letter_frequency (text):
    total_lowered = text.lower()
    character_frequency = {}
    for char in total_lowered:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1
    return character_frequency

                    
def sort_on(items):
    return items["num"]

def sort_by_count(character_count):
    listed_char = [{"char":char, "num":num } for char , num in character_count.items()]
    listed_char.sort(reverse=True, key=sort_on)
    return listed_char  
