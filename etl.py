def transform(data):
    new_dict={}
    for k,v in data.items():
        print(k,v)
        for item_v in sorted(v):
            new_dict[item_v.lower()]=k
    return new_dict

