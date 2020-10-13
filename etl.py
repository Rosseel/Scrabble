def transform(input_dic):
    res = {}
    for (key, value) in input_dic.items():
        for value2 in value:
            res[value2.lower()] = key
    return res


old = {1: ['WORLD']}
new = transform(old)
print(old)
print(new)