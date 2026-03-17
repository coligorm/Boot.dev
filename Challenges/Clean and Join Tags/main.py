RAW_TAGS = [
    "  Python ",
    "strings",
    "Python",
    " Loops ",
    "lists",
    "loops",
    "Lists  ",
]

LABEL_TAGS = "Tags: "
LABEL_TOTAL = "Total: "
SEPARATOR = ", "

def clean_tags(tags):
    cleaned_tags = []
    for tag in tags:
        tag = tag.strip().lower()
        if tag not in cleaned_tags:
            cleaned_tags.append(tag)
    return cleaned_tags

cleaned = clean_tags(RAW_TAGS)
print(LABEL_TAGS + SEPARATOR.join(cleaned))
print(LABEL_TOTAL + str(len(cleaned)))
