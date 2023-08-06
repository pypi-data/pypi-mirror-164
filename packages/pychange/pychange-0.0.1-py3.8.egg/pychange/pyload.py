
def list_to_dict(list_m):
    dict_m = {}
    for i in range(len(list_m)):
        dict_m[i] = list_m[i]
        print(i)
    return dict_m


def _is_num_(dict_m):
    for dict_t in dict_m.keys():
        if type(dict_t) != type(1):
            return False
    return True


def _max_key(dict_m):
    return max(list(dict_m.keys()))


def dict_to_list(dict_m):
    list_m = []
#     j = 0
#     if _is_num_(dict_m) is True:
#         for i in range(len(dict_m)):
#             while i != int(list(dict_m.keys())[j]):
#                 if i == 0:
#                     list_m[i] = 0
#                     print('ap', i, j)
#                     print('list', list_m)
#                     i += 1
#                 else:
#                     i += 1
#                     list_m[i-1]=0
#                     print('ap', i, j)
#                     print('list', list_m)
#             j += 1
#             list_m[i] = dict_m[list(dict_m.keys())[j-1]]
#             print('out', dict_m[list(dict_m.keys())[j-1]], i)
#             print('list', list_m)

    for i in range(len(dict_m)):
        list_m.append(dict_m[list(dict_m.keys())[i]])
    return list_m


dict_n = {1: 'a', 2: 'c', 5: 'a'}

print(dict_to_list(dict_n))