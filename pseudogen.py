"""
Usage:
python pseudogen.py
"""


class Expr:
    def __init__(self, x):
        if x == 0:
            self.res = "--======"
        elif isinstance(x, int):
            self.res = bin(x)[2:].replace("0", "--").replace("1", "=-")[:-1] + "="
        elif isinstance(x, Expr):
            self.res = x.res
        else:
            self.res = x

    def __str__(self):
        return self.res

    __repr__ = __str__

    def __add__(self, b):
        return Expr("--=-" + str(Expr(self.res)) + str(Expr(b.res)))

    def __sub__(self, b):
        return Expr("--==" + str(Expr(self.res)) + str(Expr(b.res)))

    def __mul__(self, b):
        return Expr("-=--" + str(Expr(self.res)) + str(Expr(b.res)))

    def __truediv__(self, b):
        return Expr("-=-=" + str(Expr(self.res)) + str(Expr(b.res)))

    __floordiv__ = __truediv__

    def __mod__(self, b):
        return Expr("-==-" + Expr(self.res) + Expr(b.res))


Inc = lambda: Expr("----")
In = lambda: Expr("-===")
Get = lambda x: Expr("---=" + str(Expr(x)))
Out = lambda x: Expr("==--" + str(Expr(x)))
Outc = lambda x: Expr("==-=" + str(Expr(x)))
Print = lambda x: Expr(
    "===-" + str(Expr(len(x))) + "".join(str(Expr(ord(i))) for i in x)
)
If = lambda x: Expr("=---" + str(Expr(x)))
Else = lambda: Expr("=-==")
End = lambda: Expr("=--=")
While = lambda x: Expr("=-=-" + str(Expr(x)))
Set = lambda x, y: Expr("====" + str(Expr(x)) + str(Expr(y)))
_ = Expr

import sys

if __name__ == "__main__":
    c = sys.stdin.read()
    r, s = [], []
    for i in c.split("\n"):
        ti, i = i, i.strip()
        if i:
            r.append(str(eval(i)))
            s.append(ti)
    maxlen = max(map(len, r))
    for i, j in enumerate(r):
        print(f"%-{maxlen+1}s" % j + "| " + s[i])
