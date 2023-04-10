'''
def leftOf(c: str) -> str:
    if c == '}': 
        return '{'
    elif c == ')':
        return '('
    else:
        return '['
'''
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        left = [] # 存放左括号
        for c in s:
            if c == '(' or c == '{' or c == '[': # 判断是否为左括号
                left.append(c) # 是左括号则加入列表
            else: # 是右括号
                if left and leftOf(c) == left[-1]: # 判断是否与最近的左括号匹
                    left.pop() # 匹配则将最近的左括号弹出
                else:
                    return False # 不匹配则直接返回 false
        return not left # 是否所有的左括号都被匹配了
        '''
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True
