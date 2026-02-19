import ast

def check_python_syntax(code: str):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)
