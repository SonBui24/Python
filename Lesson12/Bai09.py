def extract_characters(*file):
    a = set()
    for i in file:
        with open(i, 'r', encoding='utf-8') as f:
            a.update(set(f.read()))
    return a
