def find_num_words(text):
    num_words = len(text.split())
    return num_words

def find_each_char(text):
    char_count = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char not in char_count.keys():
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

# INPUT: dictionary with char:Int
# OUTPUT: sorted list of dicts that contain two dicts, one identifying character and other value
def sort_dictionary(dictionary):
    dict_as_list = []
    for key in dictionary:
        char_dict = {"char" : key, "count" : dictionary[key]}
        dict_as_list.append(char_dict)
    dict_as_list.sort(reverse=True, key=lambda value: value["count"])
    return dict_as_list


