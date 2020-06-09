def charAt(i):
    def ap(s):
        if i >= 0 and i < len(s):
            return s[i]

        raise IndexError("Data.String.Unsafe.charAt: Invalid index.")

    return ap


def char(s):
    if len(s) == 1:
        return s[0]
    raise ValueError("Data.String.Unsafe.char: Expected string of length 1.")
