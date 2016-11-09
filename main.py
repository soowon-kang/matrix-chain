# -*- coding: utf-8 -*-


MAXINT = 2


# TODO
def dp_mult(matrices):
    pass


def recursive_mult(matrices, char):
    length = len(matrices)
    if length < 2:
        return 0, ""
    elif length == 2:
        return 0, char
    elif length == 3:
        return matrices[0]*matrices[1]*matrices[2], char
    else:
        lowest_cost = MAXINT
        expr = ""
        for i in range(1, length-1):
            l_cost, l_expr = recursive_mult(matrices[:i+1], char[:i])
            r_cost, r_expr = recursive_mult(matrices[i:], char[i:])
            cost = matrices[0] * matrices[i] * matrices[-1]
            cost += l_cost + r_cost
            if cost < lowest_cost:
                lowest_cost = cost
                
                # for pretty output
                if len(r_expr) == 1:
                    expr = l_expr + r_expr
                else:
                    expr = l_expr + "(" + r_expr + ")"
        return lowest_cost, expr
    

if __name__ == "__main__":
    # TEST
    characters = "".join(chr(ord('A')+i) for i in range(26))
    # print(characters)
    
    # chain = [10, 5, 20, 7, 6, 8, 9, 10]
    # chain = [10, 30, 5, 60]
    # chain = [2, 3, 4, 5, 7]
    # chain = [30, 35, 15, 5]
    chain = [3, 5, 4, 2, 5]
    for t in chain:
        MAXINT *= t
    c, e = recursive_mult(chain, characters[:len(chain)-1])
    print(c, e)

    """
    SAMPLE INPUT & OUTPUT
        chain = [10, 5, 20, 7, 6, 8, 9, 10]
        >> 2460 A(BCDEFG)
        
        chain = [3, 5, 4, 2, 5]
        >> 100 A(BC)D
    """
    pass

