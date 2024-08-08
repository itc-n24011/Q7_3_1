class MyDictKeyError(Exception):
    pass

def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictKeyError(f"Key '{key}' is not registered in the dictionary")
    return dict_tbl[key]

# 使用例
dict_tbl = {'a': 1, 'b': 2, 'c': 3}

try:
    value = get_dict_value(dict_tbl, 'd')
    print(f"Value for key 'd': {value}")
except MyDictKeyError as e:
    print(e)

