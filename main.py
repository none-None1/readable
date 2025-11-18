"""
Main interpreter
"""
from parser_module import *
import sys
from collections import defaultdict

mem = defaultdict(lambda: 0)
preproc = lambda x: "".join(
    "".join(filter(lambda _: _ in "=-", (i + "|")[: (i + "|").find("|")]))
    for i in x.replace("\u2212", "=").split("\n")
)
op_dict = {}
op_dict["get"] = lambda _: mem[eval_expr(_[1])]
op_dict["inc"] = lambda _: ord(sys.stdin.read(1))
op_dict["add"] = lambda _: eval_expr(_[1]) + eval_expr(_[2])
op_dict["sub"] = lambda _: eval_expr(_[1]) - eval_expr(_[2])
op_dict["mul"] = lambda _: eval_expr(_[1]) * eval_expr(_[2])
op_dict["div"] = lambda _: eval_expr(_[1]) // eval_expr(_[2])
op_dict["mod"] = lambda _: eval_expr(_[1]) % eval_expr(_[2])
op_dict["in"] = lambda _: int(input())
op_dict["print"] = lambda _: print(_[1])
op_dict["out"] = lambda _: print(eval_expr(_[1]))
op_dict["outc"] = lambda _: print(chr(eval_expr(_[1])), end="")
op_dict["set"] = lambda _: exec(f"mem[{eval_expr(_[1])}]={eval_expr(_[2])}")
op_dict["if"] = lambda _: (execute(_[2]) if eval_expr(_[1]) else None)
op_dict["ifelse"] = lambda _: (execute(_[2]) if eval_expr(_[1]) else execute(_[3]))
op_dict["int"] = lambda _: _[1]


def f(_):
    while eval_expr(_[1]):
        execute(_[2])


op_dict["while"] = f


def eval_expr(x):
    """Evaluate an expression or a top-level-command"""
    return op_dict[x[0]](x)


def execute(x):
    """Execute a list of top-level commands"""
    for i in x:
        eval_expr(i)


def interpret(x):
    """Interpret code"""
    x = preproc(x)
    t = []
    while x:
        z, x = parse_top_level(x)
        t.append(z)
    execute(t)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        interpret(open(sys.argv[1], encoding="utf-8").read())
    else:
        interpret(sys.stdin.read())
