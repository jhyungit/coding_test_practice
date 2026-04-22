def solution(p):
    answer = ''
    if p == '':
        return ''
    
    left = right = 0
    for i, c in enumerate(p):
        if c == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    def is_valid(u):
        return u[0] == '('
    
    if is_valid(u):
        return u + solution(v)
    else:
        inner = u[1:-1]
        flipped = ''.join(')' if c == '(' else '(' for c in inner)
        return "(" + solution(v) + ")" + flipped
    
    return answer
