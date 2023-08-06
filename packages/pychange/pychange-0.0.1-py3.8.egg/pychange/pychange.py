
def to_list(str_u, typen, error_test=1):
    str_u_len = len(str_u)
    if typen == 0:
        str_n = str_u[1:str_u_len - 1]
        list_m = str_n.split(',')
    elif typen == 1:
        str_n = str_u[2:str_u_len - 2]
        list_m = str_n.split("','")
    elif typen == 2:
        str_n = str_u[2:str_u_len - 2]
        list_m = str_n.split('","')
    elif typen == 3:
        str_n = str_u[1:str_u_len - 1]
        list_m = str_n.split(',')
        for i in range(len(list_m)):
            list_m[i] = int(list_m[i])

    if (str_u[0] != '[' or str_u[str_u_len - 1] != ']') and error_test != 0:
        raise Exception("The value must can change to a list!")
    return list_m


def to_dict(str_u, typen, error_test=1):
    str_u_len = len(str_u)
    dict_m = {}
    if typen == 0:
        str_n = str_u[1:str_u_len - 1]
        str_n = str_n.split(',')
        for ns in str_n:
            key_s = ns.split(':')[0]
            dict_m[key_s] = ns.split(':')[1]
    elif typen == 1:
        str_n = str_u[2:str_u_len - 2]
        str_n = str_n.split("','")
        for ns in str_n:
            key_s = ns.split("':'")[0]
            dict_m[key_s] = ns.split("':'")[1]
    elif typen == 2:
        str_n = str_u[2:str_u_len - 2]
        str_n = str_n.split('","')
        for ns in str_n:
            key_s = ns.split('":"')[0]
            dict_m[key_s] = ns.split('":"')[1]
    elif typen == 3:
        str_n = str_u[1:str_u_len - 1]
        str_n = str_n.split(',')
        for ns in str_n:
            key_s = int(ns.split(':')[0])
            dict_m[key_s] = int(ns.split(':')[1])

    if (str_u[0] != '{' or str_u[str_u_len - 1] != '}') and error_test != 0:
        raise Exception("The value must can change to a dict!")
    return dict