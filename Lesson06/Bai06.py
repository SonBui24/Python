def is_pangram(str_, alphabet):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str_.lower():
            return False
    return True
