def run_quality_checks(code: str):
    results = {
        "has_functions": False,
        "has_tests": False,
        "too_small": False,
        "line_count": 0
    }

    lines = code.split("\n")
    results["line_count"] = len(lines)

    if "def " in code:
        results["has_functions"] = True

    if "test_" in code:
        results["has_tests"] = True

    if len(code.strip()) < 50:
        results["too_small"] = True

    return results
