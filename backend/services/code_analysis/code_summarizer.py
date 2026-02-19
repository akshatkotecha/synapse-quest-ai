def summarize_code(code: str):
    functions = []
    classes = []

    for line in code.split("\n"):
        stripped = line.strip()

        if stripped.startswith("def "):
            functions.append(stripped)

        if stripped.startswith("class "):
            classes.append(stripped)

    return {
        "functions": functions,
        "classes": classes,
        "length": len(code)
    }
