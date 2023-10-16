from MatrixModule import Matrix, Vector

def linear_combination(v_lst: list, k_list: list):
    if type(v_lst) == type(k_list) and isinstance(v_lst, list):
        return [[x[0] * k_list[row] for x in v_lst[row]] for row in range(len(v_lst))]
    return