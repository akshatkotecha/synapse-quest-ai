# import json
# from openai import OpenAI


# def verify_code_with_llm(task, code_summary, api_key):

#     if not api_key:
#         return {
#             "correctness_score": 50,
#             "missing_components": [],
#             "reason": "API key not found"
#         }

#     client = OpenAI(api_key=api_key)

#     prompt = f"""
# You are a strict software code evaluator.

# TASK:
# {task.get("title")}

# EXPECTED OUTPUTS:
# {task.get("expected_outputs")}

# CODE SUMMARY:
# Functions: {code_summary['functions']}
# Classes: {code_summary['classes']}
# Length: {code_summary['length']}

# Return JSON only:
# {{
#   "correctness_score": number between 0-100,
#   "missing_components": [],
#   "reason": "short explanation"
# }}
# """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )

#     content = response.choices[0].message.content

#     try:
#         return json.loads(content)
#     except:
#         return {
#             "correctness_score": 50,
#             "missing_components": [],
#             "reason": "LLM parsing failed"
#         }
from openai import OpenAI
import json

def verify_code_with_llm(task, code_summary, api_key):

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
Evaluate this code summary against task.

TASK: {task.get("title")}
EXPECTED: {task.get("expected_outputs")}
FUNCTIONS: {code_summary['functions']}
CLASSES: {code_summary['classes']}
"""
            }],
            temperature=0.2
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print("LLM ERROR:", e)

        return {
            "correctness_score": 60,
            "missing_components": [],
            "reason": "LLM unavailable - fallback mode"
        }
