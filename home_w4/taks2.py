def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hash(key) == -1:
            key_str = str(key)
        else:
            key_str = key
        result[value] = key_str
    return result

output = create_dict(a=10, b='hello', c=str([1, 2, 3]))
print(output)
