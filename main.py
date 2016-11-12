# -*- coding: utf-8 -*-
import time

MAXINT = 2


def dp_mult(dim, char):
    length = len(dim)
    
    dp_table = [[0 for i in range(length-1)] for j in range(length-1)]
    sep_table = [[0 for i in range(length-1)] for j in range(length-1)]
    
    for size in range(2, length):
        for l_idx in range(length-size):
            # l_idx is index for left side
            # r_idx is index for right side
            r_idx = l_idx+size-1
            
            # initialize the element of dp_table
            dp_table[l_idx][r_idx] = MAXINT
            
            for m_idx in range(l_idx, r_idx):
                # m_idx is index for splitter between l_idx and r_idx
                # calculate the cost of (l_idx ~ m_idx) & (m_idx+1 ~ r_idx)
                cost = dp_table[l_idx][m_idx]+dp_table[m_idx+1][r_idx]
                cost += dim[l_idx] * dim[m_idx+1] * dim[r_idx+1]
                
                if cost < dp_table[l_idx][r_idx]:
                    # save the lowest cost
                    dp_table[l_idx][r_idx] = cost
                    
                    # save the index when the cost is the lowest
                    sep_table[l_idx][r_idx] = m_idx
    
    # for pretty output
    def expr_with_bracket(l, r):
        if l == r:
            # directly output the corresponding expression of a matrix
            return char[l]
        else:
            m = sep_table[l][r]
        
            l_expr = expr_without_bracket(l, m)
            r_expr = expr_with_bracket(m+1, r)
            return "(" + l_expr + r_expr + ")"

    # we don't need brackets for left expression
    def expr_without_bracket(l, r):
        if l == r:
            return char[l]
        else:
            m = sep_table[l][r]
            
            l_expr = expr_without_bracket(l, m)
            r_expr = expr_with_bracket(m+1, r)
            return l_expr + r_expr
    
    return dp_table[0][-1], expr_without_bracket(0, length-2)


def recursive_mult(dim, char):
    length = len(dim)
    if length < 2:
        return 0, ""
    elif length == 2:
        return 0, char
    elif length == 3:
        return dim[0] * dim[1] * dim[2], char
    else:
        lowest_cost = MAXINT
        expr = ""
        for i in range(1, length-1):
            l_cost, l_expr = recursive_mult(dim[:i+1], char[:i])
            r_cost, r_expr = recursive_mult(dim[i:], char[i:])
            cost = dim[0] * dim[i] * dim[-1]
            cost += l_cost+r_cost
            if cost < lowest_cost:
                lowest_cost = cost
                
                # for pretty output
                if len(r_expr) == 1:
                    expr = l_expr+r_expr
                else:
                    expr = l_expr+"("+r_expr+")"
        return lowest_cost, expr


if __name__ == "__main__":
    # TEST
    characters = "".join(chr(ord('A')+i) for i in range(26))
    # print(characters)
    
    chain = [10, 5, 20, 7, 6, 8, 9, 10]
    chain = [10, 30, 5, 60]
    chain = [2, 3, 4, 5, 7]
    chain = [3, 5, 4, 2, 5]
    chain = [5, 35, 15, 5, 10, 20, 25]
    chain = [6, 35, 15, 5, 10, 20, 25]
    chain = [7, 35, 15, 5, 10, 20, 25]
    chain = [30, 35, 15, 5, 10, 20, 25, 2, 3]
    for t in chain:
        MAXINT *= t
    
    rec_time = time.clock()
    rec_cost, rec_expr = recursive_mult(chain, characters[:len(chain)-1])
    rec_time = time.clock() - rec_time
    print("REC: %d %s %e" % (rec_cost, rec_expr, rec_time))
    
    dp_time = time.clock()
    dp_cost, dp_expr = dp_mult(chain, characters[:len(chain)-1])
    dp_time = time.clock() - dp_time
    print("DP : %d %s %e" % (dp_cost, dp_expr, dp_time))
    
    """
    SAMPLE INPUT & OUTPUT
        chain = [10, 5, 20, 7, 6, 8, 9, 10]
        >>  REC: 2460 A(BCDEFG) 3.277294e-04
        >>  DP : 2460 A(BCDEFG) 6.307244e-05
        
        chain = [3, 5, 4, 2, 5]
        >>  REC: 100 A(BC)D 2.009661e-05
        >>  DP : 100 A(BC)D 2.349758e-05
        
        chain = [5, 35, 15, 5, 10, 20, 25]
        >>  REC: 6750 ABCDEF 1.156328e-04
        >>  DP : 6750 ABCDEF 4.452173e-05
        
        chain = [7, 35, 15, 5, 10, 20, 25]
        >>  REC: 8225 A(BC)(DEF) 1.193430e-04
        >>  DP : 8225 A(BC)(DEF) 4.668598e-05
        
        chain = [30, 35, 15, 5, 10, 20, 25, 2, 3]
        >>  REC: 4980 A(B(C(D(E(FG)))))H 1.101604e-03
        >>  DP : 4980 A(B(C(D(E(FG)))))H 9.615456e-05
    """
    pass
