from exp import Val,Add,Sub,Mul,Div

def parse(s: str):
    num=int(s)
    return Val(num)

'''
e = parse("123")
print(e)

s = "123+456"
pos = s.find('+') # + 記号で探す
print('pos', pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s,s1,s2) # +記号を探す
'''

def parse(s: str):
    if s.find('-') > 0:
        pos = s.find('-')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Sub(parse(s1),parse(s2))
    if s.find('+') > 0:
        pos = s.find('+')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1),parse(s2))
    if s.find('*') > 0:
        pos = s.find('*')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Mul(parse(s1),parse(s2))
    if s.find('/') > 0:
        pos = s.find('/')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Div(parse(s1),parse(s2))
    return Val(int(s))

e = parse("1-2-3")
print(e, e.eval()) # -4
assert e.eval() == -4