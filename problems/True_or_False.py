'''
Given a string containing only "T", "F", "()", "|", "&", "!"
representing True, False, bracket precedence, or, and, not

If the string is illegal, return -1
If the string is evaluated as True/False, return 1/0
Evaluation follows boolean expression evaluation process

Use stack to keep track of current bracket layer
T, F, |, & should appear alone
!, (, ) can appear multiple as neighbors

Some illegal expressions:
(), ||, |&, &&, TT, TF, FF, !), (T)), )F(, empty string, (T)!F, T!F
'''

import pytest

def bool_eval(s: str) -> int:
    # deal with brackets only
    # return '0' means illegal, '-1' has 2 chars
    # return 'T' means True
    # return 'F' means False
    stack = []
    for c in s:
        if c != ')':
            stack.append(c)
            continue
        exp = []
        while stack and stack[-1] != '(':
            # exp is saved expression or temp result, reversed
            exp.append(stack.pop())
        if not stack:
            return -1
        stack.pop()
        exp.reverse()
        val = eval_or(''.join(exp))
        if val == '0':
            return -1
        stack.append(val)
    
    if '(' in stack:
        return -1
    
    val = eval_or(''.join(stack))
    if val == '0':
        return -1

    return 'FT'.index(val)
    

def eval_or(expr: str) -> str:
    # deal with | only
    # 3rd precedence
    # expr won't contain any ()
    if not expr or expr[0] == '|' or expr[-1] == '|':
        return '0'
    if len(expr) == 1:
        return expr
    exprs = expr.split('|')
    res = 0
    for exp in exprs:
        val = eval_and(exp)
        if val == '0':
            return val
        res |= 'FT'.index(val)
    # print('or', expr, 'FT'[res])
    return 'FT'[res]

def eval_and(expr: str) -> str:
    # deal with & only
    # 2nd precedence
    if not expr or expr[0] == '&' or expr[-1] == '&':
        return '0'
    if len(expr) == 1:
        return expr
    exprs = expr.split('&')
    res = 1
    for exp in exprs:
        val = eval_not(exp)
        if val == '0':
            return val
        res &= 'FT'.index(val)
    # print('and', expr, 'FT'[res])
    return 'FT'[res]

def eval_not(expr: list) -> int:
    # deal with ! only
    # 1st precedence
    if not expr or expr[-1] == '!':
        return '0'
    if len(expr) == 1:
        return expr
    cnt = 0
    for i, c in enumerate(expr):
        if c == '!':
            cnt += 1
        else:
            break
    if i < len(expr) - 1:
        return '0'
    cnt &= 1
    res = 'FT'.index(c)
    if cnt:
        res = not res
    # print('not', expr, 'FT'[res])
    return 'FT'[res]



if __name__ == "__main__":
    test = ['(F&T|!F)|(T|F&!!F)']
    for t in test:
        print(t)
        print(bool_eval(t))

def test_true():
    exprs = ['T', '(!F)', 'F|T', 'T&T', '!F|F&F|F', '(F&T|!F)|(T|F&!!F)', '(!(T&F))|(T&!F)', \
             '(!T|!F)&(T|F)', '(T&(!T|F))|!F', '(!T&(T|F))|(!F)', '(T|F)&(!T|!F)']
    for expr in exprs:
        assert bool_eval(expr) == 1

def test_false():
    exprs = ['F', '(!T)', 'F|F', 'T&F', 'T&!T&F', '(!!F)&((((T))))', '(!T|F)&(T|!F)', \
             '(T|!F)&(!T|F)', '(!T&!F)|(T&F)', '(!(T|F))&(T|!F)', '(!(T&F))&(!T|F)']
    for expr in exprs:
        assert bool_eval(expr) == 0

def test_illegal():
    exprs = ['(!!F!)', '()', '', '||', '|&', '&|', '&&', 'TT', 'TF', 'FT', \
             'FF', '!)', '(', ')', '(T))', ')F(', '(T)!F', 'T!F']
    for expr in exprs:
        assert bool_eval(expr) == -1
