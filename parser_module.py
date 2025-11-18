"""
Functions for Readable code parsing
"""


def parse_int(x):
    """Parse an integer literal"""
    res = 0
    while x:
        res = res * 2 + "-=".index(x[0])
        t = x[1]
        x = x[2:]
        if t == "=":
            break
    return res, x


def parse_string(x):
    """Parse a string"""
    n, x = parse_int(x)
    r = []
    for i in range(n):
        z, x = parse_int(x)
        r.append(chr(z))
    return ("".join(r), x)


def parse_expr(x):
    """Parse an expression"""
    tx, w, x = x, x[:4], x[4:]
    if w == "-===":
        return ("in",), x
    if w == "----":
        return ("inc",), x
    dct = {"--=-": "add", "--==": "sub", "-=--": "mul", "-=-=": "div", "-==-": "mod"}
    if w == "---=":
        y, x = parse_expr(x)
        return ("get", y), x
    elif w in dct:
        y, x = parse_expr(x)
        z, x = parse_expr(x)
        return (dct[w], y, z), x
    else:
        y, x = parse_int(tx)
        return ("int", y), x


def parse_top_level(x):
    """Parse a top-level command"""
    w, x = x[:4], x[4:]
    if w == "===-":
        y, x = parse_string(x)
        return ("print", y), x
    if w == "==--":
        y, x = parse_expr(x)
        return ("out", y), x
    if w == "==-=":
        y, x = parse_expr(x)
        return ("outc", y), x
    if w == "====":
        y, x = parse_expr(x)
        z, x = parse_expr(x)
        return ("set", y, z), x
    if w == "=---":
        insts = []
        e, x = parse_expr(x)
        while x[:4] not in ("=--=", "=-=="):
            w, x = parse_top_level(x)
            insts.append(w)
        if x[:4] == "=-==":
            x = x[4:]
            insts_else = []
            while x[:4] != "=--=":
                w, x = parse_top_level(x)
                insts_else.append(w)
            x = x[4:]
            return ("ifelse", e, insts, insts_else), x
        x = x[4:]
        return ("if", e, insts), x
    if w == "=-=-":
        insts = []
        e, x = parse_expr(x)
        while x[:4] != "=--=":
            w, x = parse_top_level(x)
            insts.append(w)
        x = x[4:]
        return ("while", e, insts), x
