"""Calculator tool — basic math expressions."""

import ast
import operator

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def evaluate(expression: str) -> float:
    """Safely evaluate a math expression."""
    tree = ast.parse(expression, mode="eval")
    return _eval(tree.body)


def _eval(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        return OPS[type(node.op)](left, right)
    else:
        raise ValueError(f"unsupported: {type(node)}")
