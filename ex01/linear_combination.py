from MatrixModule import Matrix, Vector

def linear_combination(v_lst: list, k_list: list):
    if type(v_lst) == type(k_list) and isinstance(v_lst, list) and len(v_lst) == len(k_list):
        ret = Vector([[0] for _ in range(v_lst[0].shape[1])])
        for row in range(len(v_lst)):
            ret+= (v_lst[row] * k_list[row]).T()
        return ret
    return