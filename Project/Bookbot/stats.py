def count_words(s):
    num_words = len(s.split())
    return num_words

def count_characters(s):
    count = {}

    for c in s:
        c = c.lower()
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    
    return count

def sort_on(items):
    return items["num"]

def get_sorted_dict(d):
    sorted_dicts = []
    for k,v in d.items():
        if k.isalpha():
            tmp_d = {}
            tmp_d["char"] = k
            tmp_d["num"] = v
            sorted_dicts.append(tmp_d)
    
    sorted_dicts.sort(reverse=True, key=sort_on)

    return sorted_dicts