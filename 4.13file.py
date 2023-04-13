# _*_ encoding: utf-8 _*_   @author: ty  hery   2019/2/28
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
    else:
        ret.append(i)
    return ret

def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result
deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]
print(deep_flatten([1, [2], [[3], 4], 5]))  # [1,2,3,4,5]
