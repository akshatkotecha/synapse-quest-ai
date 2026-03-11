import ast
from radon.complexity import cc_visit


# ---------------------------------
# BUG PREDICTION HEATMAP
# ---------------------------------

def bug_prediction_heatmap(code):

    try:
        blocks = cc_visit(code)
        results = []

        for block in blocks:

            if block.complexity >= 10:
                risk = "HIGH 🔴"
            elif block.complexity >= 5:
                risk = "MEDIUM 🟠"
            else:
                risk = "LOW 🟢"

            results.append({
                "function": block.name,
                "line": block.lineno,
                "complexity": block.complexity,
                "risk": risk
            })

        return results

    except Exception as e:
        return {"error": str(e)}


# ---------------------------------
# AUTO CODE REFACTOR
# ---------------------------------

class RefactorTransformer(ast.NodeTransformer):

    def visit_For(self, node):

        if (
            isinstance(node.iter, ast.Call)
            and isinstance(node.iter.func, ast.Name)
            and node.iter.func.id == "range"
        ):

            args = node.iter.args

            if (
                len(args) == 1
                and isinstance(args[0], ast.Call)
                and isinstance(args[0].func, ast.Name)
                and args[0].func.id == "len"
            ):

                array_name = args[0].args[0]

                node.target = ast.Name(id="item", ctx=ast.Store())
                node.iter = array_name

        return node


def auto_refactor(code):

    try:
        tree = ast.parse(code)

        transformer = RefactorTransformer()
        new_tree = transformer.visit(tree)

        refactored = ast.unparse(new_tree)

        return {
            "original": code,
            "refactored": refactored
        }

    except Exception as e:
        return {"error": str(e)}