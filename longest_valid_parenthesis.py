# https://www.youtube.com/watch?v=qC5DGX0CPFA Longest Valid Parentheses

def f(s):
    cst=[]
    ist=[-1]
    mxl=0
    for i in range(len(s)):
        if s[i]=='(': 
            cst.append('(')
            ist.append(i)
        else:
            if not cst: 
                ist.append(i)
            else:
                cst.pop()
                ist.pop()
                mxl = max(mxl, i-ist[-1])
    return mxl

# print(f(')()())()'))
# print(f('()))()((()))'))
# print(f(')()())'))
print(f('))()))(())((())))))())()(((((())())((()())(())((((())))())((()()))(()(((()()(()((()()))(())()))((('))
