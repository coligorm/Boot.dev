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
    pass

cleaned = clean_tags(RAW_TAGS)
print(LABEL_TAGS + SEPARATOR.join(cleaned))
print(LABEL_TOTAL + str(len(cleaned)))
