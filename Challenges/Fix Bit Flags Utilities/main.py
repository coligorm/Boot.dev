def to_8bit_binary(n):
    n = n & 0xFF
    result = ""
    bit_index = 7
    while bit_index >= 0:
        bit = (n >> bit_index) & 1
        result += str(bit)
        bit_index -= 1
    return result


def has_all_flags(value, flags):
    return (value & flags) == flags


def add_flags(value, flags):
    return value | flags
