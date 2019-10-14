
class Expr(object):
    pass


class Val(Expr):
    __slots__ = ['value']
    def __init__(self,value = 0):
        self.value = value
    
    def __repr__(self):
        return f'Val({self.value})'

    def eval(self):
        return self.value
    
v =Val(1)
print(v)
assert v.eval() ==1

assert isinstance(v, Expr) #==> True
assert isinstance(v, Val) #==> True
assert not isinstance(v, int) #==> False

def toExpr(a):
    if not isinstance(a,Expr):
        a = Val(a)
    return a

class Binary(Expr):
    def __repr__(self):
        classname = self.__class.__name__
        return f'{classname}({self.left},{self.right})'

class Add(Binary):
    __slots__=['left','right']
    def __init__(self,a,b):
       # if not isinstance(a,Expr):
        #    a =Val(a)
        #if not isinstance(b,Expr):
         #   b =Val(b)
        self.left = toExpr(a)
        self.right = toExpr(b)
    
    def eval(self):
        return self.left.eval()+ self.right.eval()

e = Add(1,Add(1,2))
print(e.eval())
assert e.eval() ==4

e = Add(Val(1),Val(2))
assert e.eval() == 3

e=Add(1,2)
assert e.eval() ==3

e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6


print()
print()
