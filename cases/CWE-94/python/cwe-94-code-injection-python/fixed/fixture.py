# CONTROLLED REMEDIATED TEST FIXTURE
# CWE-94: Improper Control of Generation of Code
import ast
import operator
OPS={ast.Add:operator.add, ast.Sub:operator.sub}
def calculate(expression: str):
    node=ast.parse(expression, mode='eval').body
    if not isinstance(node, ast.BinOp) or type(node.op) not in OPS or not all(isinstance(x, ast.Constant) for x in (node.left,node.right)):
        raise ValueError('unsupported expression')
    return OPS[type(node.op)](node.left.value,node.right.value)
